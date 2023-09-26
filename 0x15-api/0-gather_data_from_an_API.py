#!/usr/bin/python3
"""Returns informations about an employee todo list progress"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    url_id = '{}users/{}'.format(url, argv[1])
    res = requests.get(url_id)
    user = res.json()
    print("Employee {} is done with tasks".format(user.get('name')),
          end="")

    url_todo = '{}todos?userId={}'.format(url, argv[1])
    res = requests.get(url_todo)
    todo_tasks = res.json()
    com_task = []
    for task in todo_tasks:
        if task.get('completed'):
            com_task.append(task)

    print("({}/{}):".format(len(com_task), len(todo_tasks)))
    for task in com_task:
        print("\t {}".format(task.get("title")))
