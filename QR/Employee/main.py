from json_creator import create_employee_json
from qr_code_maker import create_qr_codes_from_json
from checker import check_qr_codes_from_camera


def initiator():
    condition = True

    while condition:
        temp = input("Choose the input \n 1. Json Creator \n 2. Checker \n 3. quit\n ")
        if temp == '1':
            create_employee_json()
            json_file_path = "/Users/minkhantsoeoke/Documents/Software Studio II/Employee/employee_data.json"
            output_folder = "/Users/minkhantsoeoke/Documents/Software Studio II/Employee"
            create_qr_codes_from_json(json_file_path, output_folder)
        elif temp == "2":
            json_file_path = "/Users/minkhantsoeoke/Documents/Software Studio II/Employee/employee_data.json"  # Replace with your JSON file path
            check_qr_codes_from_camera(json_file_path)
        elif temp == "3":
            condition = False



if __name__ == "__main__":
    initiator()