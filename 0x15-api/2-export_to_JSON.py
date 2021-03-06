#!/usr/bin/python3
""" Gather API Information """
import csv
import json
import requests
import sys
import urllib


def get_deserialised_json(inputurl):
    """
        inputurl: url which return a json formated string
        return: the deserialised Json
    """
    response = requests.get(inputurl).content.decode('UTF-8')
    # or return (requests.get(input).content.decode('UTF-8').json())
    try:
        obj = json.loads(response)
    except valueError:
        return ('input is not a json')
    return (obj)

if __name__ == '__main__':
    """
        Script which get data from a jsonplaceholder api
        and create a JSON file.
    """
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    url_employee = '{}/users/{}'.format(url, user_id)
    url_task = '{}/users/{}/todos'.format(url, user_id)

    data_employee = get_deserialised_json(url_employee)
    data_task = get_deserialised_json(url_task)

    employee_name = data_employee.get('name')
    user_name = data_employee.get('username')
    task_counter = 0
    complete_counter = 0
    title_all = []

    json_dict = {}
    json_dict[user_id] = [{"task": task.get("title"),
                           "completed": task.get("completed"),
                           "username": user_name} for task in data_task]

    with open('{}.json'.format(user_id), mode='w') as jsonfile:
        json.dump(json_dict, jsonfile)
