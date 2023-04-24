import json
import requests
import sys


def get_employee_todo_list(employee_id):
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    return user['id'], user['username'], todos


def export_to_json(employee_id, username, todos):
    filename = f"{employee_id}.json"
    data = {
        str(employee_id): [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            } for todo in todos
        ]
    }
    with open(filename, mode='w') as file:
        json.dump(data, file, indent=2)
    print(f"JSON file {filename} has been created successfully.")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    user_id, username, todos = get_employee_todo_list(employee_id)
    total_tasks = len(todos)
    done_tasks = sum(todo['completed'] for todo in todos)
    print(f"Employee {username} is done with tasks ({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")
    export_to_json(user_id, username, todos)

