#!/usr/bin/python3
"""extends the script 0-gather_data_from_an_API.py
    to export data in the CSV format
"""

import csv
import requests
import sys

emp_id = int(sys.argv[1])
print('retrieving data')
url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
user_url = "https://jsonplaceholder.typicode.com/users"

data = requests.get(url)
usr_data = requests.get(user_url)
info = data.json()
usr_info = usr_data.json()

for user in usr_info:
    user_id = int(user.get('id'))
    if user_id == emp_id:
        USERNAME = user.get('username')

result = []
for user in info:
    USER_ID = user.get('userId')
    TASK_COMPLETED_STATUS = user.get('completed')
    TASK_TITLE = user.get('title')
    ln = list(f'{USER_ID}, {USERNAME}, {TASK_COMPLETED_STATUS}, {TASK_TITLE}')
    result.append(ln)

with open(f'{USER_ID}.csv', 'w',) as csfile:
    write = csv.writer(csfile)
    write.writerows(result)
