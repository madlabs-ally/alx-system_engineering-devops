import csv
import requests
import sys


def get_employee_todo_list(employee_id):
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    return user['id'], user['username'], todos


def export_to_csv(employee_id, username, todos):
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, username, todo['completed'], todo['title']])
    print(f"CSV file {filename} has been created successfully.")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    user_id, username, todos = get_employee_todo_list(employee_id)
    total_tasks = len(todos)
    done_tasks = sum(todo['completed'] for todo in todos)
    print(f"Employee {username} is done with tasks ({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")
    export_to_csv(user_id, username, todos)

