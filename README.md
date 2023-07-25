# Company Task Manager - Django Project

Welcome to the Company Task Manager Django project! This web application allows users to register, login, create tasks, and assign them to other users. It simplifies task management within a company or organization, making it easier to track and collaborate on various tasks.

## Check it out!

[Company Task Manager deployed to Render](https://task-manager-rucp.onrender.com/)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Shutdown](#shutdown)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)



## Introduction

Managing tasks within a company can become challenging when multiple team members are involved. The Company Task Manager aims to streamline this process by providing an efficient web-based solution for creating, assigning, and tracking tasks. It allows team members to collaborate effectively and ensure tasks are completed on time.

## Features

- User Registration: New users can create an account and register to access the application.
- User Login: Registered users can log in to their accounts securely.
- Task Creation: Users can create new tasks, specifying details like title, description, due date, etc.
- Task Assignment: Tasks can be assigned to specific users within the company.
- Task Status Tracking: Users can update the status of tasks, such as "Active", "Pending" or "Completed".
- Task Searching: Users can search for tasks based on their titles, making it easy to find specific tasks.
- User Management: Administrators can manage user accounts, position, task types in admin panel (superuser required).

## Requirements

To run this Django project locally, you'll need the following:

- Python (version 3.11)
- Django (version 4.0.10)
- Other dependencies mentioned in requirements.txt


## Installation
1. Clone the repository to your local machine:
```
git clone https://github.com/Altahoma/company-task-manager.git
```
2. Change into the project directory:
```
cd company-task-manager
```
3. Create a virtual environment (optional but recommended):
```
python -m venv venv
```
4. Activate the virtual environment (skip this step if you didn't create a virtual environment):
```
# On Windows
venv\Scripts\activate

# On macOS or Linux
source venv/bin/activate
```
5. Install the project dependencies:
```
pip install -r requirements.txt
```
6. Run database migrations:
```
python manage.py migrate
```
7. Create a superuser (admin) account to access the Django admin interface:
```
python manage.py createsuperuser
```
8. Start the development server:
```
python manage.py runserver
```
9. Open your web browser and navigate to http://localhost:8000/ to access the application.


## Shutdown

If you are currently running the server in the terminal, press "CTRL + C" (Windows) or "COMMAND + C" (macOS/Linux).

## Usage

- Visit the application in your web browser.
- Register a new account or log in with your existing credentials.
- Create tasks by providing all necessary details and assign them to other registered users by selecting their usernames from a list.
- Track the status of tasks and update them accordingly.

## Contributing

Contributions to the Company Task Manager project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

The Company Task Manager project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms of the license.