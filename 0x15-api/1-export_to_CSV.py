#!/usr/bin/python3
""" convert json to csv file """

if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

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
                filename = f"{argv[1]}.csv"
                with open(filename, mode='w') as csvfile:
                    for paras in todos:
                        title = paras['title']
                        status = paras["completed"]
                        csvfile.write(
                                '"{}","{}","{}","{}"\n'.format(
                                                        argv[1],
                                                        username,
                                                        status,
                                                        title
                                                        ))
