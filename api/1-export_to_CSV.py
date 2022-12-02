#!/usr/bin/python3
''''return something'''
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

    nameFile = str(eval(sys.argv[1])) + ".csv"

    f = open(nameFile, "x")
    for task in to_do_list:
        s = ('"' + str(user.get("id")) + '","' + str(
            user.get("username")) + '","' +
            str(task.get("completed")) + '","' +
            str(task.get("title")) + '"' + "\n")
        f.write(s)
