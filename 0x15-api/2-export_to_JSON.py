#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script
 to export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    user_parameters = {'id': argv[1]}
    response = requests.get(url2, params=user_parameters)
    if response.status_code == 200:
        user = response.json()
        for i in user:
            username = i['username']
            todo_parameters = {'userId': argv[1]}
            response = requests.get(url, params=todo_parameters)
            if response.status_code == 200:
                todos = response.json()
                filename = f"{argv[1]}.json"
                dictionary = {argv[1]: []}
                for paras in todos:
                    title = paras['title']
                    status = paras["completed"]
                    dictionary[argv[1]].append({"task": title,
                                                "completed": status,
                                                "username": username})
                with open(filename, mode='w') as jsonfile:
                    json.dump(dictionary, jsonfile)
