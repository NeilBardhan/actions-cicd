import os
import json
import requests
from pprint import pprint
from secrets import CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN_URL, CASE_URL, CASE_NUMBER_TEST


def get_access_token():
    data = {
    'grant_type': 'client_credentials',
    'client_id': os.environ['CONSUMER_KEY'],
    'client_secret': os.environ['CONSUMER_KEY_SECRET'],
    }
    response = requests.post(os.environ['ACCESS_TOKEN_URL'], data=data)
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


def get_case_status():
    header = {
        'Authorization': 'Bearer {}'.format(os.environ['USCIS_ACCESS_TOKEN']),
        'Accept': 'application/json'
    }
    response = requests.get(CASE_URL.format(os.environ['CASE_NUMBER_TEST']), headers=header)
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
        os.environ['USCIS_ACCESS_TOKEN'] = access_token
        case_status = get_case_status()
        if case_status is not None:
            print("CASE STATUS FOR {receipt}: {status}".format(receipt=os.environ['CASE_NUMBER_TEST'], status=case_status))
    else:
        print("failed to get case status")