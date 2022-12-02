#!/usr/bin/python3
''''return something'''
import json
import requests
import sys
if __name__ == '__main__':
    identity = sys.argv[1]
    payload = {"userId": identity}
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(identity)).json()
    to_do_list = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params=payload).json()

    dic = {}

    for i in user:
        ident = user.get('id')
        to_do_list = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params=payload).json()
        for task in to_do_list:
            dic.update({user.get("id"): [{"task": task.get("task"),
                                          "completed": task.get("completed"),
                                          "username": user.get("username")}]})

    with open("todo_all_employees.json", "w") as f:
        json.dump(dic, f)