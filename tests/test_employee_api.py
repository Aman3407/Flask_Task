def test_create_employee_success(client):
    # Simulate a valid POST request with employee data
    data = {
        "emp_id": 1234,
        "name": "John Doe",
        "isActive": True,
        "dateOfJoining": "2023-07-24",
        "email": "john.doe@example.com"
    }
    response = client.post('/employee', json=data)

    # Assert successful response with status code and content
    assert response.status_code == 200
    assert response.json['res']['name'] == data['name']
    assert response.json['msg'] == 'Success creating a new employee!'

def test_create_employee_missing_field(client):
    # Simulate a POST request with missing field
    data = {
        "emp_id": 1234,
        "isActive": True,
        "dateOfJoining": "2023-07-24",
        "email": "john.doe@example.com"
    }
    response = client.post('/employee', json=data)

    # Assert bad request with error message
    assert response.status_code == 400
    assert 'Missing field:' in response.json['error']

def test_create_employee_invalid_date_format(client):
    # Simulate a POST request with invalid date format
    data = {
        "emp_id": 1234,
        "name": "John Doe",
        "isActive": True,
        "dateOfJoining": "invalid_date",
        "email": "john.doe@example.com"
    }
    response = client.post('/employee', json=data)

    # Assert bad request with error message
    assert response.status_code == 400
    assert 'dateOfJoining must be in YYYY-MM-DD format' in response.json['error']

def test_create_employee_invalid_email(client):
    # Simulate a POST request with invalid email
    data = {
        "emp_id": 1234,
        "name": "John Doe",
        "isActive": True,
        "dateOfJoining": "2023-07-24",
        "email": "invalid_email"
    }
    response = client.post('/employee', json=data)

    # Assert forbidden request with error message
    assert response.status_code == 403
    assert 'Invalid email format' in response.json['error']

def test_create_employee_duplicate_emp_id(client, mocker):
    # Simulate existing employee with same emp_id (mocking db.view())
    mocker.patch('app.db.view', return_value=[{'emp_id': 1234}])
    data = {
        "emp_id": 1234,
        "name": "John Doe",
        "isActive": True,
        "dateOfJoining": "2023-07-24",
        "email": "john.doe@example.com"
    }
    response = client.post('/employee', json=data)

    # Assert bad request with error message
    assert response.status_code == 400
    assert "Employee with emp_id" in response.json['error']

def test_create_employee_duplicate_email(client, mocker):
    # Simulate existing employee with same email (mocking db.view())
    mocker.patch('app.db.view', return_value=[{'email': 'john.doe@example.com'}])
    data = {
        "emp_id": 5678,
        "name": "John Doe",
        "isActive": True,
        "dateOfJoining": "2023-07-24",
        "email": "john.doe@example.com"
    }
    response = client.post('/employee', json=data)

    # Assert bad request with error message
    assert response.status_code == 400
    assert "Employee with email" in response.json['error']
