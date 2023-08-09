#!/usr/bin/python3
""" Uses REST API to return information about a given employee ID """

import json
import requests
import sys


if __name__ == "__main__":
    employeeID = sys.argv[1]
    baseurl = "https://jsonplaceholder.typicode.com/users"
    url = baseurl + "/" + employeeID

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {employeeID: []}

    for task in tasks:
        dictionary[employeeID].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
            })
    with open('{}.json'.format(employeeID), 'w') as f:
        json.dump(dictionary, f)
