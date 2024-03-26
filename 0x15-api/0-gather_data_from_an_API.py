#!/usr/bin/python3
'''gather employee data from API'''

import requests
import sys
import re
import csv

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            tk_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = req.get('name')
            tks = list(filter(lambda x: x.get('userId') == id, tk_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tks)
                )
            )
            if len(completed_tasks) > 0:
                for tk in completed_tasks:
                    print('\t {}'.format(tk.get('title')))
