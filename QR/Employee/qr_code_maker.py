import json
import qrcode
import os

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)


def create_qr_codes_from_json(json_file_path: object, output_folder: object) -> object:
    with open(json_file_path, 'r') as file:
        employee_data = json.load(file)

    employees = employee_data.get("employees", [])

    for employee in employees:
        employee_id = employee.get("id", "")
        if employee_id:
            qr_code_data = f"Name: {employee['name']}\nID: {employee_id}\nPosition: {employee['position']}"
            qr_code_file_path = os.path.join(output_folder, f"qr_code_{employee_id}.png")
            generate_qr_code(qr_code_data, qr_code_file_path)
            print(f"QR code generated for employee {employee['name']} (ID: {employee_id})")

