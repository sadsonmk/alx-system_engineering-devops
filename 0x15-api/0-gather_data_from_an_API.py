#!/usr/bin/python3
"""using a REST API, for a given employee ID, returns
    information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url_users = "https://jsonplaceholder.typicode.com/users"

    data = requests.get(url)
    usr = requests.get(url_users)

    TOTAL_NUMBER_OF_TASKS = len(data.json())
    done_tasks = [x for x in data.json() if x.get('completed') is True]
    NUMBER_OF_DONE_TASKS = len(done_tasks)

    for user in usr.json():
        user_id = int(user.get('id'))
        if user_id == employee_id:
            EMPLOYEE_NAME = user.get('name')
    print(f"Employee {EMPLOYEE_NAME} is done with\
 tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    for info in done_tasks:
        my_tasks = info.get('title')
        print(f"\t {my_tasks}")
