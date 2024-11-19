'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''
import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.delete(url + "/8180")
print(f"Response code: {response.status_code}")

response_conf = requests.get(url)
print(f"Response content: {response_conf.content}") #correct confirmation?