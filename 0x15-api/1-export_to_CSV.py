#!/usr/bin/python3
""" Export api to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    """ANYTHING"""
    user_name = res.json().get('username')
    tk = url_user + '/todos'
    res = requests.get(task)
    tks = res.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for tk in tks:
            completed = tk.get('completed')
            """Complete"""
            title_tk = tk.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_tk))
