'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''

# input statements
# function for each task


# how do I get the user id from the new task and carry it forward to the update task
# Is status code for successful post always 201?

import requests
from pprint import pprint
import time

users_url = "http://demo.codingnomads.co:8080/tasks_api/users"
tasks_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"

user_id = ''

def new_account():
    global user_id
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    email = input('Enter your email: ')
    body = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }
    response = requests.post(users_url, json = body)
    if response.status_code == 201:
        users_data = response.json()
        pprint(users_data)
        pprint(f"user_id = {users_data['data']['id']}")
        user_id = users_data['data']['id']
    else:
        print(f"Failed to create new account: {response.status_code}")
    return user_id

def view_tasks(user_id):
    unique_task_url = f"http://demo.codingnomads.co:8080/tasks_api/tasks?userId={user_id}"
    response = requests.get(unique_task_url)
    if response.status_code == 200:
        tasks_data = response.json()
        pprint(tasks_data)
    else:
        print(f"Failed to fetch tasks: {response.status_code}")

def task_status(user_id, status):
    status_url = f"http://demo.codingnomads.co:8080/tasks_api/tasks?userId={user_id}&complete={status}"
    response = requests.get(status_url)
    if response.status_code == 200:
        data = response.json()
        pprint(data)
    else:
        print(f"Failed to get task status: {response.status_code}")

def new_task():
    timestamp = int(time.time())
    task_name = input('Name the task: ')
    task_description = input('Describe the task: ')
    complete = input('Complete? Enter true or false: ')
    body = {
        'id': '',
        'userId': user_id,
        'name': task_name,
        'description': task_description,
        'createdAt': timestamp,
        'updatedAt': timestamp,
        'completed': complete,
    }
    response = requests.post(tasks_url, json = body)
    if response.status_code == 201:
        users_data = response.json()
        pprint(users_data)
    else:
        print(f"Failed to create new task: {response.status_code}")

def update_task():
    view_tasks(user_id)
    id = input('From the tasks available, which task id would you like to update?: ')
    update_task_url = f"http://demo.codingnomads.co:8080/tasks_api/tasks/{id}"
    task_user = int(input('Enter the user id: '))
    task_name = input('Enter the name of the task: ')
    task_description = input('Enter the description of the task: ')
    task_status = input('Is the task complete? Enter true for yes. Enter false for no.: ')
    body = {
        "userId": task_user,
        "name": task_name,
        "description": task_description,
        "completed": task_status
    }
    try:
        response = requests.put(update_task_url, json = body)
        response.raise_for_status()
        if response.status_code == 200:
            update_task_data = response.json()
            pprint(update_task_data)
        else:
            print(f"Unexpected status code: {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}.")
    # update = input('What part of the task do you want to update? Enter name, description, or status: ')
    # if update == 'name':
    #     task_name = input('What is the new name for the task?: ')
    #     body = {
    #         'name': task_name,
    #         }
    # elif update == 'description':
    #     task_description = input('What is the new description for the task?: ')
    #     body = {
    #         'description': task_description,
    #         }
    # elif update == 'status':
    #     complete = input('Is the task complete? Enter true for yes. Enter false for no.: ')
    #     if complete == 'true' or complete == 'false':
    #         body = {
    #             'completed': complete
    #             }
    #     else:
    #         print('Please enter true or false.')
    # else:
    #     input('Please enter name, description, or status: ')
    # response = requests.patch(update_task_url, json = body)
    # if response.status_code == 200:
    #     update_task_data = response.json()
    #     pprint(update_task_data)
    # else:
    #     print(f"Failed to update task: {response.status_code}")

def delete_task():
    view_tasks(user_id)
    id = input('Which id do you want to delete?: ')
    delete_url = f"http://demo.codingnomads.co:8080/tasks_api/tasks"
    response = requests.delete(delete_url + f'/{id}')
    if response.status_code == 200:
        print(f'Task {id} was successfully deleted.')
    else:
        print(f"Failed to delete task. Response code: {response.status_code}")

in_app = True

while in_app:

    print("""
    1) Create a new account (POST)
    2) View all your tasks (GET)
    3) View your completed tasks (GET)
    4) View only your incomplete tasks (GET)
    5) Create a new task (POST)
    6) Update an existing task (PATCH/PUT)
    7) Delete a task (DELETE)
    8) Exit App""")

    user_choice = int(input("\nHello, please select an option from the menu above, entering the number of the action you would like to take: "))

    if user_choice == 1:
        new_account()
    elif user_choice == 2:
        view_tasks(user_id)
    elif user_choice == 3:
        task_status(user_id, 'true')
    elif user_choice == 4:
        task_status(user_id, 'false')
    elif user_choice == 5:
        new_task()
    elif user_choice == 6:
        update_task()
    elif user_choice == 7:
        delete_task()
    elif user_choice == 8:
        in_app = False
    else:
        print("Please enter a number 1 through 8.")

# print(user_id)

# delete_url = f"http://demo.codingnomads.co:8080/tasks_api/users/8905"
# response = requests.delete(delete_url)
# if response.status_code == 200:
#     print(f'User was successfully deleted.')
# else:
#     print(f"Failed to delete task. Response code: {response.status_code}")

# update_task_url = f"http://demo.codingnomads.co:8080/tasks_api/tasks/8712"

# body = {
#     "userId": 8878,
#     "name": 'homework',
#     "description": 'read chapter 8',
#     "completed": 'false'
# }

# response = requests.put(update_task_url, json = body)
      
# update_task_data = response.json()
# pprint(update_task_data)