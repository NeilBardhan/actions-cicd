import os
import json
import requests
from pprint import pprint


APP_NAME = "tracker_gc"
CONSUMER_KEY = "WgeOV3lfT4TfOcXeVCcyAMelQyyA21gf"
CONSUMER_KEY_SECRET = "DOnHJk3ezOru5EOm"
CASE_NUMBER_ACTUAL = "LIN2412352133"
CASE_NUMBER_TEST = "LIN9999106498"
ACCESS_TOKEN_URL = "https://api-int.uscis.gov/oauth/accesstoken"
CASE_URL = "https://api-int.uscis.gov/case-status/{}"


def get_access_token():
    data = {
    'grant_type': 'client_credentials',
    'client_id': CONSUMER_KEY,
    'client_secret': CONSUMER_KEY_SECRET,
    }
    response = requests.post(ACCESS_TOKEN_URL, data=data)
    if response.status_code == 200:
        response_json = response.json()
        if response_json['status'] == 'approved':
            print("Access Token Granted")
            return response_json['access_token']
        else:
            print("Access Token Denied")
            return None
    else:
        print("Access Token Denied")
        return None


def get_case_status(access_token):
    header = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Accept': 'application/json'
    }
    response = requests.get(CASE_URL.format(CASE_NUMBER_TEST), headers=header)
    if response.status_code == 200:
        print('Received case status')
        text_lines = response.text.split('\n')
        for line in text_lines:
            if "current_case_status_text_en" in line:
                line = line.strip()
                case_status = line.split(':')[1].strip()[1:-2]
                return case_status
    else:
        print('Failed to get case status')
        print(response.text)
        return None

if __name__ == '__main__':
    access_token = get_access_token()
    if access_token is not None:
        case_status = get_case_status(access_token)
        if case_status is not None:
            print("CASE STATUS FOR {receipt}: {status}".format(receipt=CASE_NUMBER_TEST, status=case_status))
    else:
        print("failed to get case status")