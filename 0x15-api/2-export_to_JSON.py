#!/usr/bin/python3
"""Returns informations about an employee in a csv file"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    u_id = argv[1]

    url_id = '{}users/{}'.format(url, u_id)
    res = requests.get(url_id)
    user = res.json()

    url_todo = '{}todos?userId={}'.format(url, u_id)
    res = requests.get(url_todo)
    tasks = res.json()

    user_task = {
            u_id: [{
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.get('username'),
                } for task in tasks]
            }
    user_file = '{}.json'.format(u_id)
    with open(user_file, mode='w') as file_json:
        json.dump(user_task, file_json)

    print('Json file "{}" has been successfully created.'.format(user_file))
