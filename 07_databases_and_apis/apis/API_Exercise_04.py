'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "updated first",
    "last_name": "updated last",
    "email": "newemail@email.com"
}

response = requests.put(url + "/8180", json=body)

print(f"Response code: {response.status_code}")

response_conf = requests.get(url)

pprint(f"Response content: {response_conf.content}")