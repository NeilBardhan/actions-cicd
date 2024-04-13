import requests
from datetime import datetime
r = requests.get('http://worldtimeapi.org/api/timezone/America/Los_Angeles')

if r.status_code == 200:
    response = r.json()
    prefix = datetime.strftime(datetime.now(), '%m-%d::%H-%M')
    print("TIME: {tm}\nRESPONSE: {dt}".format(tm = prefix, dt = response['datetime']))