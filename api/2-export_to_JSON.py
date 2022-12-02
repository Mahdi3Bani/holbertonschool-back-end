#!/usr/bin/python3
''''return something'''
import requests
import sys
import json
if __name__ == '__main__':
    identity = sys.argv[1]
    payload = {"userId": identity}
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(identity)).json()
    to_do_list = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params=payload).json()
    jsonn = {}
    for task in to_do_list:
        jsonn = jsonn.update({user.get("id"): [{"task": task.get("title"),
                                         "completed": task.get("completed"),
                                         "username": user.get("username")}]})
    with open(identity + ".json", 'w') as f:
        jsonn.dump(jsonn,f)