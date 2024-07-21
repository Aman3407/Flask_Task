# How to Run?

This guide will help you set up and run a Flask application using a `requirements.txt` file to manage dependencies.

## Prerequisites

Before starting, make sure you have the following installed:
- Python 3.x (and pip)
- Git (optional, for version control)

1. Create a virtual Environment:
```
  python3 -m venv env
```

2. Activate the Virtural Environment
```

```
3. 


## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aman3407/Flask_Task/
   cd Flask_Task

# Employee Management System (CRUD Application) with Flask

This is a CRUD application built on the Spring Boot framework. The purpose of this application is to efficiently manage employee information by providing users with the ability to add, view, update, and delete employee data.
## Features

1. **Add Employee**
   - **Endpoint**: `/employees`
   - **Method**: POST
   - **Description**: Adds a new employee to the system.
   - **Screenshot**:

<img width="1012" alt="image" src="https://github.com/user-attachments/assets/f598a6c2-311c-4840-a3a2-ca88c86c29ae">



2. **Get Specific Employee**
   - **Endpoint**: `/employees/{id}`
   - **Method**: GET
   - **Description**: Retrieves the details of a specific employee using their ID.
   - **Screenshot**:

<img width="1021" alt="image" src="https://github.com/user-attachments/assets/2939d189-e528-4dfe-90ad-10b5e00c1a90">



3. **Get All Employees**
   - **Endpoint**: `/employees`
   - **Method**: GET
   - **Description**: Retrieves the details of all employees.
   - **Screenshot**:

<img width="1011" alt="image" src="https://github.com/user-attachments/assets/ba036c15-2e1a-468a-bf72-e00f136c49c0">


4. **Update Employee's Data**
   - **Endpoint**: `/employees/{id}`
   - **Method**: PUT
   - **Description**: Updates the data of an existing employee using their ID.
   - **Screenshot**:

<img width="1042" alt="image" src="https://github.com/user-attachments/assets/945bc58e-15ee-465c-8d5a-811ee0db0626">
<img width="1027" alt="image" src="https://github.com/user-attachments/assets/d82bf22a-d5c0-44ec-aa40-fc9730e7ea4f">

5. **Delete Employee**
   - **Endpoint**: `/employees/{id}`
   - **Method**: DELETE
   - **Description**: Deletes a specific employee using their ID.
   - **Screenshot**:

<img width="986" alt="image" src="https://github.com/user-attachments/assets/12a9eef7-efca-44bb-91c0-f606f05881c4">

## Fields

- **id**: The unique identifier for the employee.
- **name**: The name of the employee.
- **dateOfJoining**: The date the employee joined the company.
- **isActive**: The active status of the employee.
