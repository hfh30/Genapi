import requests
from requests.auth import HTTPBasicAuth
import json
import urllib.parse
import sys
sys.stdout = open('console_output.txt', 'w')
def getEventDetails():
    url = "https://www.training.cam.ac.uk/api/v1/event/4809025"
    params = {"fetch": "bookings", "format": "json"}
    username = 'hfh30'
    password = 'QZrxgTgR7HK5b8hyf3279F3C4xTfXPft'

    response = requests.get(url, params=params, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        print('Successfully authenticated!')
        data = response.json()
        crsids = []
        for booking in data['result']['event']['bookings']:
            if 'participant' in booking and 'crsid' in booking['participant']:
                crsid = booking['participant']['crsid']
                if crsid.startswith('#'):
                    crsid = urllib.parse.quote(crsid)  # Replace # with %23
                print(crsid)
                crsids.append(crsid)
            if 'bookedBy' in booking and 'crsid' in booking['bookedBy']:
                crsid = booking['bookedBy']['crsid']
                if crsid.startswith('#'):
                    crsid = urllib.parse.quote(crsid)  # Replace # with %23
                print(crsid)
                crsids.append(crsid)
        return crsids
    else:
        print('Could not authenticate')
# Get event details gathers the json file from a class based on the event in the URL. It then parses through the data and puts out the CRSID/External ID for each user on the class
printed_names = set()

def getPersonDetails(crsid):
    global printed_names
    url = f"https://www.training.cam.ac.uk/api/v1/person/{crsid}?format=json"
    username = 'hfh30'  # replace with your username
    password = 'QZrxgTgR7HK5b8hyf3279F3C4xTfXPft'  # replace with your password

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        try:
            data = response.json()
            if 'person' in data['result'] and 'name' in data['result']['person']:
                person_name = data['result']['person']['name']
                if person_name not in printed_names:
                    print(person_name) 
                    with open('person_names.txt', 'a') as file:
                        file.write(person_name + '\n')  
                    printed_names.add(person_name)
        except json.JSONDecodeError:
            print(response.text)
    else:
        print('Could not retrieve person details')

# getPersonDetails retrieves each individual CRSIDs name from the API. It parses through each CRSID value generated in getEventDetails and then exports it into a local text document with each name. Names are also put into a list so they are not exported again to prevent duplicates.
crsids = getEventDetails()
for crsid in crsids:
    getPersonDetails(crsid)
sys.stdout.close()