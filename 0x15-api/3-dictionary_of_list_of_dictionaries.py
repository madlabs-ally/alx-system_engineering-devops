import requests
import json


def get_employee_todo_list(employee_id):
    # Get the todo list for the specified employee
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    todos = response.json()
    return todos


def get_employee_name(employee_id):
    # Get the name of the specified employee
    response = requests.get(f'https://jsonplaceholder.typicode.com/users?id={employee_id}')
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    user_data = response.json()
    employee_name = user_data[0]['name']
    return employee_name


def export_employee_todo_list_to_csv(employee_id, employee_name, todos):
    # Export the employee's todo list to a CSV file
    file_name = f"{employee_id}.csv"
    with open(file_name, "w") as f:
        f.write('"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"\n')
        for todo in todos:
            task_completed_status = "complete" if todo['completed'] else "incomplete"
            task_title = todo['title']
            f.write(f'"{employee_id}","{employee_name}","{task_completed_status}","{task_title}"\n')


def export_employee_todo_list_to_json(employee_id, employee_name, todos, all_todos):
    # Export the employee's todo list to a JSON file
    tasks = []
    for todo in todos:
        task = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee_name
        }
        tasks.append(task)

    all_todos[str(employee_id)] = tasks


def export_all_employee_todo_lists_to_json():
    all_todos = {}
    # Get the todo list for all employees
    for employee_id in range(1, 11):
        todos = get_employee_todo_list(employee_id)
        if todos is not None:
            employee_name = get_employee_name(employee_id)
            export_employee_todo_list_to_csv(employee_id, employee_name, todos)
            export_employee_todo_list_to_json(employee_id, employee_name, todos, all_todos)

    # Export all the employee's todo lists to a single JSON file
    file_name = "todo_all_employees.json"
    with open(file_name, "w") as f:
        json.dump(all_todos, f)

    print(f"JSON file {file_name} has been created successfully.")


if __name__ == "__main__":
    export_all_employee_todo_lists_to_json()

