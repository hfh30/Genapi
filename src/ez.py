import requests
from requests.auth import HTTPBasicAuth

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
   
    data = {"message": "Hello from Python!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050')

url = 'https://www.training.cam.ac.uk/api/v1/event/182276?fetch=bookings&format=json'

username = 'hfh30'
password = 'QZrxgTgR7HK5b8hyf3279F3C4xTfXPft'

response = requests.get(url, auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    print('Successfully authenticated!')
    data = response.json()
    print(data)
else:
    print('couldnt authenticate')


