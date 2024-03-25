import requests
import sys

def fetch_todo_list_progress(employee_id):
    try:
        # Fetch user info
        user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data['name']

        # Fetch user's TODO list
        todo_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
        todo_data = todo_response.json()

        # Calculate progress
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task['completed'])

        # Print progress report
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
