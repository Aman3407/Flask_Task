Here's a polished and well-organized version of your Markdown file, with enhanced formatting and clarity:

---

# Employee Management System (CRUD Application) with Flask

This is a CRUD application built using Flask to efficiently manage employee information. Users can add, view, update, and delete employee data.

## Setup

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x (and pip)
- Git (optional, for version control)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Aman3407/Flask_Task/
   cd Flask_Task
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv env
   ```

3. **Activate the Virtual Environment:**

   - **On Windows:**
     ```bash
     .\env\Scripts\activate
     ```

   - **On macOS/Linux:**
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask Application:**
   ```bash
   flask run
   ```
   By default, the application will start on [http://127.0.0.1:5000](http://127.0.0.1:5000).

6. **Run Tests (Optional):**
   ```bash
   pytest
   ```
   This will execute the test cases defined in your `test_app.py` file to ensure that the application functions as expected.

## Features

1. **Add Employee**
   - **Endpoint**: `/employees`
   - **Method**: POST
   - **Description**: Adds a new employee to the system.
   - **Screenshot**:
     ![Add Employee](https://github.com/user-attachments/assets/f598a6c2-311c-4840-a3a2-ca88c86c29ae)
     - Ensuring name is always a string:
       ![Name Validation](https://github.com/user-attachments/assets/b82e3bc3-00d5-473f-9a8c-40edb1833608)
     - Ensuring date format is always correct:
       ![Date Validation](https://github.com/user-attachments/assets/c1e4de5a-65eb-4480-8dc1-4f905d16a220)
     - Email validation:
       ![Email Validation](https://github.com/user-attachments/assets/75ca0996-bcfc-48e3-b052-2127ab9b7186)

2. **Get Specific Employee**
   - **Endpoint**: `/employees/{id}`
   - **Method**: GET
   - **Description**: Retrieves the details of a specific employee using their ID.
   - **Screenshot**:
     ![Get Specific Employee](https://github.com/user-attachments/assets/2939d189-e528-4dfe-90ad-10b5e00c1a90)

3. **Get All Employees**
   - **Endpoint**: `/employees`
   - **Method**: GET
   - **Description**: Retrieves the details of all employees.
   - **Screenshot**:
     ![Get All Employees](https://github.com/user-attachments/assets/ba036c15-2e1a-468a-bf72-e00f136c49c0)

4. **Update Employee's Data**
   - **Endpoint**: `/employees/{id}`
   - **Method**: PUT
   - **Description**: Updates the data of an existing employee using their ID.
   - **Screenshots**:
     ![Update Employee](https://github.com/user-attachments/assets/945bc58e-15ee-465c-8d5a-811ee0db0626)
     ![Update Employee](https://github.com/user-attachments/assets/d82bf22a-d5c0-44ec-aa40-fc9730e7ea4f)

5. **Update or Create Employee's Data**
   - **Endpoint**: `/employees/{id}`
   - **Method**: PATCH
   - **Description**: Updates the data of an existing employee using their ID, and creates the employee if they do not exist.
   - **Screenshots**:
     - Creating the employee if it does not exist:
       ![Create Employee](https://github.com/user-attachments/assets/2fa3fa3c-c099-43c6-b5fd-6a7c1203ae37)
     - Updating the employee info if it already exists:
       ![Update Existing Employee](https://github.com/user-attachments/assets/f772c371-91f0-4c46-be64-33f561508c71)
     - Handling missing required fields and non-existent employee:
       ![Validation Error](https://github.com/user-attachments/assets/77b0588f-fcde-45d8-9885-390f81b75c00)

6. **Delete Employee**
   - **Endpoint**: `/employees/{id}`
   - **Method**: DELETE
   - **Description**: Deletes a specific employee using their ID.
   - **Screenshot**:
     ![Delete Employee](https://github.com/user-attachments/assets/12a9eef7-efca-44bb-91c0-f606f05881c4)
     - If the employee does not exist:
       ![Delete Non-Existent Employee](https://github.com/user-attachments/assets/4ecd7343-92ce-4f13-99b4-0d94735f0656)

## Fields

- **id**: The unique identifier for the employee.
- **name**: The name of the employee.
- **dateOfJoining**: The date the employee joined the company.
- **isActive**: The active status of the employee.
- **email**: The email address of the employee.

## Additional Notes

- Ensure that your `db.py` and `models.py` files are properly configured with your database and models.
- Modify `app.py` to include any additional configurations or routes as needed.

---

This guide provides clear instructions for setting up and running the Flask application, along with detailed feature descriptions and examples.
