#!/usr/bin/python3
""" Uses REST API to return information about a given employee ID """

import requests
import sys
import csv


if __name__ == "__main__":
    employeeID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = "{}users/{}".format(url, employeeID)
    response = requests.get(user)
    tasks = response.json()
    name = tasks.get('username')

    todos = "{}todos?userId={}".format(url, employeeID)
    response = requests.get(todos)
    tasks = response.json()
    done_tasks = []

    for task in tasks:
        done_tasks.append([employeeID, name,
                            task.get('completed'),
                            task.get('title')])

    filename = '{}.csv'.format(employeeID)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                        delimiter=',',
                                        quotechar='"',
                                        quoting=csv.QUOTE_ALL)
        for task in done_tasks:
            employee_writer.writerow(task)
