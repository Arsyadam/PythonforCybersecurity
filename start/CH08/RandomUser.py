# RandomUser.py - reference version for comparison
import requests

URL = "https://randomuser.me/api/"

response = requests.get(URL, timeout=10)

if response.status_code == 200:
    data = response.json()
    user = data["results"][0]

    name = user["name"]
    location = user["location"]
    street = location["street"]

    print("===== Random User =====")
    print("Name:     ", name["title"], name["first"], name["last"])
    print("Gender:   ", user["gender"])
    print("Age:      ", user["dob"]["age"])
    print("Email:    ", user["email"])
    print("Phone:    ", user["phone"])
    print("Cell:     ", user["cell"])
    print("Address:  ", street["number"], street["name"])
    print("City:     ", location["city"] + ",", location["state"], location["postcode"])
    print("Country:  ", location["country"])
    print("Username: ", user["login"]["username"])
    print("Nat:      ", user["nat"])
    print("=======================")
else:
    print("Error: could not get a user. Status code:", response.status_code)
