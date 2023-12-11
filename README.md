# QR Based Attendance Record System  | AGH Software Studio Project 2
*  **By**: Edibe Tutku Gayda, Min Khant, Małgorzata Kuczera, Kaung Sithu

| No. | Table of Contents                                                                   |
| --- | ----------------------------------------------------------------------- |
| 1   | [**Project Description**]()  
| 2   | [**User Stories**](https://github.com/Etutku/QRBarcode-Based-Employee-Attendance-Record-System/blob/main/User_Stories.md) |
| 3   | [**Instruction**]()   |
| 4   | [**Project Base**]()   |
| 5   | [**QR Implementation**](https://github.com/Etutku/QRBarcode-Based-Employee-Attendance-Record-System/tree/main/QR/Employee)   |
| 6   | [**Acceptance Criteria**](https://github.com/Etutku/QRBarcode-Based-Employee-Attendance-Record-System/blob/main/Acceptance_Criteria.md)   |  
| 7   | [**Graphics/Modes**](https://github.com/Etutku/QRBarcode-Based-Employee-Attendance-Record-System/tree/main/Graphics)   |
| 8   | [**Firebase**](https://console.firebase.google.com/u/1/project/employee-attendance-syst-4e7a6/overview?pli=1) |

## Project Description 
  * QR Code Employee Attendance System is a highly efficient, swift, and user-friendly tool designed for monitoring employee attendance within a company. It leverages the power of QR codes to streamline the process. For instance, when an employee is working online, it logs their login and logout times as timestamps. Our project utilizes **_HTML, CSS, and JavaScript_** to create a web-based interface, making attendance management convenient and accessible. This system seamlessly operates when devices are connected to the same local network.

  * The company can present the QR code through a webpage, or in situations like conferences, attendance can be collected using a projector, allowing present employees to effortlessly scan and record their attendance.


## Key Features

1. **Automatic IP Fetching**: This system automatically fetches your IPv4 address and generates a QR code based on that IP, facilitating easy connections within the same local network.

2. **Company Panel**: The system includes a Company View Panel, giving managers the ability to manage attendances by removing duplicate or proxy entries, ensuring accurate attendance records.

3. **User-Friendly Interface**: With a user-centric design, the interface is intuitive and easy to use, minimizing the learning curve for employees and managers.

4. **Real-Time Tracking**: Attendance can be marked by scanning QR codes with real-time updates, providing immediate and accurate attendance data.

5. **Accessibility**: Attendance records are easily accessible, allowing quick reference and analysis to support decision-making and compliance.
   
## Technological Stack 
1. **Front-end Technology**:
  - **_HTML_**:  For creating the structure of the web-based interface.
  - **_CSS_**: For styling and layout design.
  - **_JavaScript_**: To add interactivity and handle client-side operations, such as QR code scanning.
 
2. **Back-end Technology**:
   -  **_Pyhton_**: As the primary programming language for back end.

3. **Database**: [X]
   - **_Relational Datavase Management System (RDBMS)_**:  To store employee attendance data. Popular choices include:
   - 
4. **Networking**: [X]
   - **_Local Network Configuration_**: To ensure that devices can communicate within the same local network.

5. **QR Code Generation**:
   - **_QR Code Library_**: To generate QR codes based on the IP addresses.

6. **Real-Time Updates**:
   - **_WebSockets_**: To enable real-time updates for attendance tracking.

7. **User Interface Design**:
   - **_Front-End Frameworks_**: You may consider using front-end frameworks like **React**, **Vue.js**, or **Angular** for a more dynamic and responsive user interface.

8. **Security**:
   - **_Authentication and Authorization_**: Implement user authentication and authorization mechanisms for secure access.
   - **_HTTPS_**: Enforce secure communication using HTTPS for data transmission.
   - **_CORS (Cross-Origin Resource Sharing)_**: Configure CORS settings to manage web page access to resources on different domains.

9. **Project Management and Version Control**:
   - **_Git_**: To manage the project's source code and collaborate with a development team.
   - **GitHub**

10. **Deployment**:
    - **_Web Hosting_**:  **Google Cloud Platform (GCP)**.

