<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Leave Management System</h3>

  <p align="center">
    A comprehensive desktop application designed to streamline the leave application process for students, teachers, and principals in educational institutions.
    <br />
    <a href="#usage"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#getting-started">View Demo</a>
    ·
    <a href="#contributing">Report Bug</a>
    ·
    <a href="#contributing">Request Feature</a>
  </p>
</div>

<!-- BADGES -->
<div align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img alt="SQLite" src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img alt="License" src="https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge" />
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#database-structure">Database Structure</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The **Leave Management System** is a graphical user interface (GUI) based application built using Python and Tkinter. It provides a centralized platform for handling leave requests within a college or educational institution. The system divides users into three primary roles: Students, Teachers, and the Principal (Administrator), ensuring a structured and accountable process for leave approval.

### Key Features

* **Multi-Role Authentication**: Secure login and registration systems customized for Students, Teachers, and Principals.
* **Student Dashboard**: 
  * Apply for various types of leaves (Casual Leave, Personal Work, Emergency, Sick Leave).
  * View leave balance and the status of applications (Granted or Rejected).
* **Teacher Dashboard**:
  * Apply for leaves and track application status.
  * Dedicated interface separated from students' records.
* **Principal / Admin Panel**:
  * View all pending leave applications from students and teachers across different departments.
  * Access detailed applicant information.
  * Approve or reject leave requests with a simple click.
* **Automated Data Processing**: Uses SQLite databases for robust local data storage and tracking of users, leave balances, and request histories.

### Built With

This project relies on core Python libraries, ensuring minimal setup requirements and maximum portability.

* **[Python 3.x](https://www.python.org/)** - Core programming language.
* **Tkinter** - Standard Python interface to the Tk GUI toolkit used for building the desktop application interface.
* **SQLite3** - C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You need to have Python installed on your Windows, macOS, or Linux machine.
* Download and install the latest version of Python from [python.org](https://www.python.org/downloads/). (Ensure that the "Add Python to PATH" option is checked during installation).

### Installation

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/shubhamauti9/leave-management-system.git
   ```
2. Navigate into the project directory:
   ```sh
   cd leave-management-system
   ```
3. Run the main application file:
   ```sh
   python OSTL_MAIN.py
   ```
   *(Note: Depending on your Python installation, you might need to use `python3 OSTL_MAIN.py`)*

<!-- USAGE -->
## Usage

Once the application is launched, you will be greeted by the Main Login Page. From here, you can navigate based on your role:

1. **New Users (Students & Teachers)**:
   * Click on `STUDENT LOGIN` or `TEACHER LOGIN`.
   * Click on the `REGISTER` button to create a new profile.
   * Fill in your Name, Email ID, Branch, Username, Password, and role.
2. **Applying for Leave**:
   * Login with your registered credentials.
   * Fill in the leave reason and date.
   * Click `APPLY` to submit the application to the Principal.
   * Use the `VIEW PRINCIPAL's MESSAGE` button to check if your leave was approved.
3. **Principal Control**:
   * Select `PRINCIPAL LOGIN`.
   * Default Admin credentials (if applicable) are Username: `admin` and Password: `admin`.
   * View pending applications in the list boxes.
   * Select an application, optionally view applicant details, and choose to `GRANT` or `REJECT` the leave.

*(Placeholder for Screenshots)*
> **Tip:** You can replace this section with actual screenshots of the application interfaces (e.g., login screen, dashboard, etc.) using `image1.png` and `image2.png` provided in the directory.

<!-- DATABASE STRUCTURE -->
## Database Structure

The application utilizes three separate SQLite databases to manage distinct datasets securely:

* `COLLEGE.db`: Stores registration credentials and personal details of all users (Students and Teachers).
* `LEAVE.db`: Temporarily stores incoming leave applications that are pending approval from the Principal.
* `LEAVE_ACESS.db`: Stores processed leave applications along with the decision (Granted/Rejected) made by the Principal, acting as a historical log.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the Apache License 2.0. See [`LICENSE`](LICENSE) for more information.

<!-- CONTACT -->
## Contact

Shubham Auti - [GitHub Profile](https://github.com/shubhamauti9)

Project Link: [https://github.com/shubhamauti9/leave-management-system](https://github.com/shubhamauti9/leave-management-system)