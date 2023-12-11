import cv2
import json


def check_employee_name(qr_code_data, json_file_path):
    with open(json_file_path, 'r') as file:
        employee_data = json.load(file)

    employees = employee_data.get("employees", [])

    for employee in employees:
        stored_name = employee['name'].strip().lower()

        # Extract name from QR code data
        qr_code_lines = qr_code_data.split('\n')
        if len(qr_code_lines) > 0:
            qr_code_name_parts = qr_code_lines[0].split(': ')
            if len(qr_code_name_parts) > 1:
                qr_code_name = qr_code_name_parts[1].strip().lower()

                if stored_name == qr_code_name:
                    return True

    return False


def check_qr_codes_from_camera(json_file_path):
    camera = cv2.VideoCapture(0)  # Use 0 for the default camera

    # Load the QR code detector
    qr_detector = cv2.QRCodeDetector()

    while True:
        ret, frame = camera.read()

        if ret:
            # Convert the frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect QR codes in the frame
            retval, decoded_info, points, straight_qrcode = qr_detector.detectAndDecodeMulti(gray_frame)

            if retval:
                for qr_code_data in decoded_info:
                    qr_code_data = qr_code_data.strip()
                    print(f"QR Code Data: {qr_code_data}")

                    # Check if the name is in the JSON file
                    is_employee = check_employee_name(qr_code_data, json_file_path)

                    if is_employee:
                        print("The QR code corresponds to an employee in the JSON file.")
                    else:
                        print("The QR code does not match any employee in the JSON file.")

            # Display the frame (optional)
            cv2.imshow("QR Code Scanner", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    camera.release()
    cv2.destroyAllWindows()



