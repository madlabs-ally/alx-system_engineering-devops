import requests
import sys

EMPLOYEES_API_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_API_URL = "https://jsonplaceholder.typicode.com/todos"


def get_employee_name(employee_id):
    response = requests.get(f"{EMPLOYEES_API_URL}/{employee_id}")
    if response.ok:
        employee = response.json()
        return employee['name']
    else:
        response.raise_for_status()


def get_employee_todos(employee_id):
    response = requests.get(TODOS_API_URL, params={'userId': employee_id})
    if response.ok:
        todos = response.json()
        return todos
    else:
        response.raise_for_status()


def display_todo_progress(employee_name, todos):
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")


def main(employee_id):
    try:
        employee_name = get_employee_name(employee_id)
        todos = get_employee_todos(employee_id)
        display_todo_progress(employee_name, todos)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    main(employee_id)

