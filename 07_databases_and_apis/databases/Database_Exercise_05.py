'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''
import requests
import sqlalchemy
from pprint import pprint

users_url = "http://demo.codingnomads.co:8080/tasks_api/users"
users_response = requests.get(users_url)
if users_response.status_code == 200:
    users_data = users_response.json()
    # for user in users_data['data']:
    #     print(f"{user['id']}: {user['last_name']}, {user['first_name']}")
else:
    print(f"Failed to fetch users: {users_response.status_code}")
# pprint(users_data)

tasks_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
tasks_response = requests.get(tasks_url)
if tasks_response.status_code == 200:
    tasks_data = tasks_response.json()
    # pprint(tasks_data)
    # for user in tasks_data['data']:
    #     print(f"{user['userId']}: {user['name']}")
else:
    print(f"Failed to fetch tasks: {tasks_response.status_code}")


def create_user(id, first_name, last_name):
    return {
        'id': id, 
        'first_name': first_name, 
        'last_name': last_name
    }


engine = sqlalchemy.create_engine("mysql+pymysql://root:PASSWORD@localhost/database_exercise_five")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table('users', metadata,
                              sqlalchemy.Column('id', sqlalchemy.String(100)),
                              sqlalchemy.Column('first_name', sqlalchemy.String(100)),
                              sqlalchemy.Column('last_name', sqlalchemy.String(100))
                              )

tasks = sqlalchemy.Table('tasks', metadata,
                              sqlalchemy.Column('userId', sqlalchemy.String(100)),
                              sqlalchemy.Column('name', sqlalchemy.String(100))
                              )

metadata.create_all(engine)

#pprint(users_data)

user_records = [
    create_user(user['id'], user['first_name'], user['last_name'])
    # {
    #     'id': user['id'], 
    #     'first_name': user['first_name'], 
    #     'last_name': user['last_name']
    # }
    for user in users_data['data']
]
users_query = sqlalchemy.insert(users)
user_proxy = connection.execute(users_query, user_records)

#pprint(tasks_data)

tasks_records = [
    {
        'userId': task['userId'],
        'name': task['name']
    }
    for task in tasks_data['data']
]
tasks_query = sqlalchemy.insert(tasks)
tasks_proxy = connection.execute(tasks_query, tasks_records)

connection.commit()