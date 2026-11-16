# GetDadJoke.py - reference version for comparison
import requests

URL = "https://icanhazdadjoke.com/"
HEADERS = {"Accept": "application/json"}

response = requests.get(URL, headers=HEADERS, timeout=10)

if response.status_code == 200:
    data = response.json()
    print(data["joke"])
else:
    print("Error: could not get a joke. Status code:", response.status_code)
