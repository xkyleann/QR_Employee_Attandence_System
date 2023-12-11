import json


def create_employee_json():
    json_file_path = "employee_data.json"

    try:
        with open(json_file_path, 'r') as json_file:
            content = json_file.read()

        if not content.strip():
            employee_data = {"employees": []}
        else:
           employee_data = json.loads(content)
    except (FileNotFoundError, json_file_path):
        employee_data = {"employees": []}
    while True:
        employee = {}

        employee["name"] = input("Enter employee name (or 'exit' to finish): ")
        if employee["name"].lower() == 'exit':
            break

        employee["id"] = input("Enter employee ID: ")
        employee["position"] = input("Enter employee position: ")

        employee_data["employees"].append(employee)

    with open(json_file_path, 'w') as json_file:
        json.dump(employee_data, json_file, indent=2)

    print(f"Employee data has been saved to {json_file_path}")

if __name__ == "__main__":
    create_employee_json()
