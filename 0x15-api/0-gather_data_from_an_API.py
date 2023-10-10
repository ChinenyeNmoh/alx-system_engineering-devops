#!/usr/bin/python3
""" make a request to a url and extract data """

if __name__ == '__main__':
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    todo_parameters = {'userId': argv[1]}
    response = requests.get(url, params=todo_parameters)
    if response.status_code == 200:
        todos = response.json()
        count = 0
        completed = 0
        title_list = []
        for i in todos:
            count = count + 1
            if i["completed"]:
                completed += 1
                title_list.append(i['title'])
        user_parameters = {'id': argv[1]}
        response = requests.get(url2, params=user_parameters)
        if response.status_code == 200:
            user = response.json()
            for i in user:
                names = i['name']
                print('Employee {} is done with tasks({}/{}):'.format(
                    names,
                    completed,
                    count
                ))
                for line in title_list:
                    print(f"\t {line}")
