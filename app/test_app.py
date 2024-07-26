import pytest
import json

# Test creating a new employee
def test_create_employee(client):
    data = {
        'emp_id': 101,
        'name': 'John Doe',
        'isActive': True,
        'dateOfJoining': '2023-07-01',
        'email': 'john.doe@example.com'
    }
    response = client.post('/employee', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['status'] == '200'
    assert response.json['msg'] == 'Success creating a new employee!'
    assert response.json['res']['emp_id'] == 101

# # Test creating an employee with missing fields
def test_create_employee_missing_fields(client):
    data = {
        'emp_id': 102,
        'name': 'Jane Doe'
        # Missing 'isActive', 'dateOfJoining', and 'email'
    }
    response = client.post('/employee', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Missing field: \'isActive\'' or \
           response.json['error'] == 'Missing field: \'dateOfJoining\'' or \
           response.json['error'] == 'Missing field: \'email\''

# Test fetching details of a specific employee
def test_get_employee_details(client):
    response = client.get('/employee/101')
    assert response.status_code == 200
    assert response.json['status'] == '200'
    assert response.json['msg'] == 'Success getting employee by ID: 101'
    assert response.json['res']['emp_id'] == 101

# Test fetching details of a non-existent employee
def test_get_non_existent_employee(client):
    response = client.get('/employee/999')
    assert response.status_code == 404
    assert response.json['status'] == '404'
    assert 'Error! Employee with emp_id \'999\' was not found!' in response.json['error']

# Test updating an employee
def test_update_employee(client):
    data = {
        'name': 'John Updated',
        'isActive': False,
        'dateOfJoining': '2023-08-01',
        'email': 'john.updated@example.com'
    }
    response = client.put('/employee/101', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['status'] == '200'
    assert response.json['msg'] == 'Success updating the employee with emp_id 101!'
    assert response.json['res']['name'] == 'John Updated'

# Test partial updating (PATCH) an employee
def test_patch_employee(client):
    data = {
        'name': 'John Patched'
    }
    response = client.patch('/employee/101', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['status'] == '200'
    assert response.json['msg'] == 'Success updating the employee with emp_id 101!'
    assert response.json['res']['name'] == 'John Patched'

# Test deleting an employee
def test_delete_employee(client):
    response = client.delete('/employee/101')
    assert response.status_code == 200
    assert response.json['status'] == '200'
    assert response.json['msg'] == 'Success deleting employee by ID!'
    assert 'no_of_employees' in response.json

# Test deleting a non-existent employee
def test_delete_non_existent_employee(client):
    response = client.delete('/employee/999')
    assert response.status_code == 404
    assert response.json['status'] == '404'
    assert 'Employee Id Not Found!' in response.json['error']

# Test creating an employee with invalid data
def test_create_employee_invalid_data(client):
    data = {
        'emp_id': 103,
        'name': 'JD',
        'isActive': 'active',  # Invalid boolean
        'dateOfJoining': '2023-07-01',
        'email': 'invalid-email'
    }
    response = client.post('/employee', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400

def test_update_employee_with_invalid_data(client):
    # Create an employee first to ensure the ID exists for this test
    create_data = {
        'emp_id': 102,
        'name': 'Valid Name',
        'isActive': True,
        'dateOfJoining': '2023-07-01',
        'email': 'valid.email@example.com'
    }
    client.post('/employee', data=json.dumps(create_data), content_type='application/json')

    invalid_data = {
        'name': 'JD',
        'isActive': 'active',  # Invalid boolean
        'dateOfJoining': '2023-07-01',
        'email': 'invalid-email'
    }
    response = client.put('/employee/102', data=json.dumps(invalid_data), content_type='application/json')
    assert response.status_code == 400
    assert 'Invalid email format. Please enter a valid email address' in response.json['error'] or \
           'isActive must be a boolean or an integer that can be converted to a boolean' in response.json['error']