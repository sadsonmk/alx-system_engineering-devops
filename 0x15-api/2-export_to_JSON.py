#!/usr/bin/python3
""" extends script 0-gather_data_from_an_API.py
    to export data in the JSON format
"""

import json
import requests
import sys

if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    print('retrieving data')
    url = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    usr_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

    data = requests.get(url).json()
    usr_data = requests.get(usr_url).json().get('username')

    data_list = []
    data_len = len(data)
    for info in data:
        info.pop('userId')
        info.pop('id')
        info['task'] = info['title']
        info.pop('title')
        info['username'] = usr_data
        data_list.append(info)
    my_dict = {emp_id: data_list}

    with open(f'{emp_id}.json', 'w') as my_file:
        json.dump(my_dict, my_file)
