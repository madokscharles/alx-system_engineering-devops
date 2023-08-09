#!/usr/bin/python3
""" Uses REST API to return information about a given employee ID """

import requests
import sys
import csv


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = '{}users/{}'.format(url, user_id)
    response = requests.get(user)
    username = response.json().get('username')

    todos = todos = '{}todos?userId={}'.format(url, user_id)
    response = requests.get(todos)
    tasks = response.json()
    done_tasks = []

    for task in tasks:
        done_tasks.append([user_id,
                       username,
                       task.get('completed'),
                       task.get('title')])

    filename = '{}.csv'.format(user_id)

    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in done_tasks:
            employee_writer.writerow(task)
