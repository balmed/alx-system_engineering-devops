#!/usr/bin/python3
""" Python to get data from API and convert to Json"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(url_to_user)
    """Documentation"""
    USERNAME = res.json().get('username')
    """Documentation"""
    url_to_tk = url_to_user + '/todos'
    res = requests.get(url_to_tk)
    tks = res.json()

    dict_data = {USER_ID: []}
    for tk in tks:
        TASK_COMPLETED_STATUS = tk.get('completed')
        TASK_TITLE = tk.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    """print(dict_data)"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)

