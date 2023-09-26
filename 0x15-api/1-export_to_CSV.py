#!/usr/bin/python3
"""Returns informations about an employee in a csv file"""
import requests
from sys import argv
import csv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    u_id = argv[1]

    url_id = '{}users/{}'.format(url, u_id)
    res = requests.get(url_id)
    user = res.json()

    url_todo = '{}todos?userId={}'.format(url, u_id)
    res = requests.get(url_todo)
    tasks = res.json()

    user_file = '{}.csv'.format(u_id)
    with open(user_file, mode='w', newline='') as csv_ufile:
        csv_write = csv.writer(csv_ufile, quoting=csv.QUOTE_ALL)

        for task in tasks:
            csv_write.writerow([u_id, user.get('username'),
                               task.get('completed'), task.get('title')])

    print('CSV file "{}" has been created.'.format(user_file))
