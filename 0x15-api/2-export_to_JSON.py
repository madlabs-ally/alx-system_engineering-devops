#!/usr/bin/env python3

import requests
import json
import sys


def get_todos(user_id):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
        response.raise_for_status()  # raise an exception if the request failed
        todos = response.json()
        return todos
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []


def get_username(user_id):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        response.raise_for_status()
        user = response.json()
        return user['username']
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def filter_completed_tasks(todos):
    return [todo for todo in todos if todo['completed']]


def generate_tasks_dict(user_id, todos, username):
    tasks = []
    for todo in todos:
        tasks.append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        })

    return { str(user_id): tasks }


def write_tasks_to_file(tasks_dict, user_id):
    filename = f"{user_id}.json"
    with open(filename, "w") as f:
        json.dump(tasks_dict, f)
    print(f"JSON file {filename} has been created successfully.")


def main(user_id):
    todos = get_todos(user_id)
    if not todos:
        return

    username = get_username(user_id)
    if not username:
        return

    completed_tasks = filter_completed_tasks(todos)
    tasks_dict = generate_tasks_dict(user_id, todos, username)
    write_tasks_to_file(tasks_dict, user_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    main(user_id)

