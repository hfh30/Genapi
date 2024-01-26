import requests
from requests.auth import HTTPBasicAuth
import json

# url = 'https://www.training.cam.ac.uk/api/v1/event/3917128?fetch=bookings&format=json'
url = "https://www.training.cam.ac.uk/api/v1/event/4809025?fetch=bookings&format=json"

username = 'hfh30'

password = 'QZrxgTgR7HK5b8hyf3279F3C4xTfXPft'

response = requests.get(url, auth=HTTPBasicAuth(username, password))


if response.status_code == 200:
    print('Successfully authenticated!')
    resp = response.json()
    data = response.json()
    print(resp)
    with open('output.json', 'w') as f:
        json.dump(data, f)

else:
    print('couldnt authenticate')
