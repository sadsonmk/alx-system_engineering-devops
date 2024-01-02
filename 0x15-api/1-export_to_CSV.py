#!/usr/bin/python3
"""extends the script 0-gather_data_from_an_API.py
    to export data in the CSV format
"""

import csv
import requests
import sys

if __name__ == '__main__':
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
            USRNAME = user.get('username')

    result = []
    for user in info:
        USER_ID = str(user.get('userId'))
        TSK_COMPLETED = str(user.get('completed'))
        TSK_TITLE = user.get('title')
        ln = f'{USER_ID},{USRNAME},{TSK_COMPLETED},{TSK_TITLE}'
        result.append(ln.split(','))

    with open(f'{USER_ID}.csv', 'w',) as csfile:
        write = csv.writer(csfile, quoting=csv.QUOTE_ALL)
        write.writerows(result)
