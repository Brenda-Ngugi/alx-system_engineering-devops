#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
Imported modules
requests
load
sys
"""
from json import dump, load
import requests
from sys import argv


if __name__ == '__main__':
    def request(resource, param=None):
        """
        Retrieve user data using API
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        key = param[0]
        value = param[1]
        if param:
            url += ('?' + key + '=' + value)

        r = requests.get(url)
        r = r.json()
        return r

    user = request('users', ('id', argv[1]))[0]
    tasks = request('todos', ('userId', argv[1]))

    # Prep for .json export
    user_id = user['id']
    export = {user_id: []}
    filename = argv[1] + '.json'
    # Export to .json format
    for task in tasks:
        export[user_id].append({'task': task['title'],
                                'completed': task['completed'],
                                'username': user['username']})
        with open(filename, mode='w') as f:
            dump(export, f)
