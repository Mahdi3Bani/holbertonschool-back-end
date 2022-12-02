#!/usr/bin/python3
''''return something'''
import requests
import sys
if __name__ == '__main__':
    identity = sys.argv[1]
    payload = {"userId": identity}
    user = requests.get(
        "https://jsonplaceholder.typicode.com/user/{}".format(identity)).json()
    to_do_list = requests.get(
        "https://jsonplaceholder.typicode.com/user/todos", params=payload).json()

    l = []
    for i in to_do_list:
        if i.get['l'] is True:
            l.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'), len(l),len(to_do_list)))
    for i in l:
        print("\t {}".format(i))