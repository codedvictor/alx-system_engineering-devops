#!/usr/bin/python3
"""Returns informations about an employee in a csv file"""
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    users_url = '{}users/'.format(url)
    res = requests.get(users_url)
    users = res.json()
    users_fil = {}

    for user in users:
        user_id = user.get('id')
        user_name = user.get('username')
        url_todo = '{}todos?userId={}'.format(url, user_id)
        res = requests.get(url_todo)
        tasks = res.json()
        list_tasks = []
        for task in tasks:
            fil = {}
            fil['username'] = user_name
            fil['task'] = task.get('title')
            fil['completed'] = task.get('completed')
            list_tasks.append(fil)

        users_fil[str(user_id)] = list_tasks

    user_file = 'todo_all_employees.json'
    with open(user_file, mode='w') as file_json:
        json.dump(users_fil, file_json)
