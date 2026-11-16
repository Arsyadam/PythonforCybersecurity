#!/usr/bin/env python3
# Script that gets a random dad joke from icanhazdadjoke.com
# By Arsyad Mahardika
# date: 11/15

# Import Python modules
import requests
import json

def get_dad_joke():
    # Setup the URL and the Accept header so the API returns JSON
    request_uri = "https://icanhazdadjoke.com/"
    headers = { 'Accept' : "application/json" }
    # Perform the request
    r = requests.get(request_uri, headers=headers)
    # Convert the JSON to Python objects
    items = r.json()
    return items

joke = get_dad_joke()

# print "pretty" json
print( json.dumps(joke, indent=2) )

# print only the joke
print("Here's your dad joke: {0}".format(joke["joke"]))
