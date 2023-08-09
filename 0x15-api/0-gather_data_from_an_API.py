#!/usr/bin/python3
""" Uses REST API to return information about a given employee ID """

import requests
import sys


if __name__ == "__main__":
    employeeID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = "{}users/{}".format(url, employeeID)
    response = requests.get(user)
    tasks = response.json()
    print("Employee {} is done with tasks".format(tasks.get('name')), end="")

    todos = "{}todos?userId={}".format(url, employeeID)
    response = requests.get(todos)
    tasks = response.json()
    done_tasks = []

    for task in tasks:
        if task.get('completed') is True:
            done_tasks.append(task)

    print("({}/{}):".format(len(done_tasks), len(tasks)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
