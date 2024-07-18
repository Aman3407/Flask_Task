from flask import Flask, request, jsonify
import os,re
import db
from models import Employee
from datetime import datetime

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return True
    else:
      return False

def createEmployeeController():
    req_data = request.get_json()

    try:
        emp_id = req_data['emp_id']
        name = req_data['name']
        isActive = req_data['isActive']
        dateOfJoining = req_data['dateOfJoining']
        email = req_data['email']

        # Validate dateOfJoining 
        parsed_date = datetime.strptime(dateOfJoining, '%Y-%m-%d').date()

        if len(name)<3:
          raise ValueError("Name cannot be empty")

        # Convert isActive to boolean if it's an int
        if isinstance(isActive, int):
            isActive = bool(isActive)
        elif not isinstance(isActive, bool):
            raise ValueError("isActive must be a boolean or an integer that can be converted to a boolean")

        # Validate email format
        if not isValid(email):
            return jsonify({
                'status': '403',
                'res': 'failure',
                'error': 'Invalid email format. Please enter a valid email address'
            })

        # Check if emp_id or email already exists
        existing_emps = [emp.serialize() for emp in db.view()]
        for emp in existing_emps:
            if emp['emp_id'] == emp_id:
                return jsonify({
                    'error': f"Employee with emp_id '{emp_id}' already exists",
                    'status': '400'
                })
            if emp['email'] == email:
                return jsonify({
                    'error': f"Employee with email '{email}' already exists",
                    'status': '400'
                })

        # Create the employee object with correct attribute values
        emp = Employee(
            id=db.getNewId(),
            emp_id=emp_id,
            name=name,
            isActive=isActive,
            dateOfJoining=parsed_date.strftime('%Y-%m-%d'),
            email=email
        )

        # Insert the employee into the database
        db.insert(emp)

        # Return success response
        return jsonify({
            'res': emp.serialize(),
            'status': '200',
            'msg': 'Success creating a new employee!'
        })

    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def getEmployeeDetailsController(emp_id) : 

    emps = [emp.serialize() for emp in db.view()]

    if emp_id.lower() == 'all':  # Return all employees if emp_id is 'all' (case insensitive)
        return jsonify({
            'res': emps,
            'status': '200',
            'msg': 'Success getting all employees!',
            'no_of_employees': len(emps)
        })

    try:
        emp_id = int(emp_id)  # Convert emp_id to integer if possible
    except ValueError:
        return jsonify({
            'error': 'Invalid emp_id format. Must be an integer or "all".',
            'status': '400'
        })

    # Find specific employee by emp_id
    emp = next((emp for emp in emps if emp['emp_id'] == emp_id), None)
    if emp:
        return jsonify({
            'res': emp,
            'status': '200',
            'msg': f'Success getting employee by ID: {emp_id}'
        })
    else:
        return jsonify({
            'error': f"Error! Employee with emp_id '{emp_id}' was not found!",
            'res': '',
            'status': '404'
        })

def UpdateEmployeeController(emp_id) :
    try:
        req_data = request.get_json()
        req_args = request.view_args
        
        emp_id = req_args['emp_id']
        name = req_data.get('name')  # Using get() method to handle missing keys
        isActive = req_data.get('isActive')
        dateOfJoining = req_data.get('dateOfJoining')
        email = req_data.get('email')

        emps = [emp.serialize() for emp in db.view()]
        existing_emp = next((emp for emp in emps if emp['emp_id'] == int(emp_id)), None)

        if not existing_emp:
            return jsonify({
                'error': f"Error! Employee with emp_id '{emp_id}' not found.",
                'status': '404'
            })

        # If a field is not provided in the request, retain the existing value from the database
        if name is None:
            name = existing_emp['name']
        if isActive is None:
            isActive = existing_emp['isActive']
        if dateOfJoining is None:
            dateOfJoining = existing_emp['dateOfJoining']
        if email is None:
            email = existing_emp['email']
        try:
            parsed_date = datetime.strptime(dateOfJoining, '%Y-%m-%d').date()
        except ValueError as ve:
            return jsonify({
                'error': "dateOfJoining must be in YYYY-MM-DD format",
                'status': '400'
            })

        # Convert isActive to boolean if it's an int
        if isinstance(isActive, int):
            isActive = bool(isActive)
        elif not isinstance(isActive, bool):
            raise ValueError("isActive must be a boolean or an integer that can be converted to a boolean")

        if len(name)<3:
          raise ValueError("Name cannot be empty")
        
        # Validate email format
        if not isValid(email):
            return jsonify({
                'status': '403',
                'res': 'failure',
                'error': 'Invalid email format. Please enter a valid email address'
            })

        # Update the values
        updated_emp = Employee(
            id=existing_emp['id'],
            emp_id=emp_id,
            name=name,
            isActive=isActive,
            dateOfJoining=parsed_date.strftime('%Y-%m-%d'),
            email=email
        )
        # Update the employee in the database
        db.update(updated_emp)

        return jsonify({
            'res': updated_emp.serialize(),
            'status': '200',
            'msg': f'Success updating the employee with emp_id {emp_id}!'
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def CreateOrUpdateEmployeeController(emp_id):
    try:
        req_data = request.get_json()
        req_args = request.view_args

        emp_id = req_args['emp_id']
        name = req_data.get('name')  # Using get() method to handle missing keys
        isActive = req_data.get('isActive')
        dateOfJoining = req_data.get('dateOfJoining')
        email = req_data.get('email')

        emps = [emp.serialize() for emp in db.view()]
        existing_emp = next((emp for emp in emps if emp['emp_id'] == int(emp_id)), None)

        if existing_emp:
            if name is None:
                name = existing_emp['name']
            if isActive is None:
                isActive = existing_emp['isActive']
            if dateOfJoining is None:
                dateOfJoining = existing_emp['dateOfJoining']
            if email is None:
                email = existing_emp['email']
        else :
            if 'name' not in req_data:
                raise KeyError('name')
            if 'isActive' not in req_data:
                raise KeyError('isActive')
            if 'dateOfJoining' not in req_data:
                raise KeyError('dateOfJoining')
            if 'email' not in req_data:
                raise KeyError('email')

        try:
            parsed_date = datetime.strptime(dateOfJoining, '%Y-%m-%d').date()
        except ValueError as ve:
            return jsonify({
                'error': "dateOfJoining must be in YYYY-MM-DD format",
                'status': '400'
            })

        # Convert isActive to boolean if it's an int
        if isinstance(isActive, int):
            isActive = bool(isActive)
        elif not isinstance(isActive, bool):
            raise ValueError("isActive must be a boolean or an integer that can be converted to a boolean")
        
        if len(name)<3:
          raise ValueError("Name cannot be empty")

        # Validate email format
        if not isValid(email):
            return jsonify({
                'status': '403',
                'res': 'failure',
                'error': 'Invalid email format. Please enter a valid email address'
            })

        if existing_emp:
            # Update the values
            updated_emp = Employee(
                id=existing_emp['id'],
                emp_id=emp_id,
                name=name,
                isActive=isActive,
                dateOfJoining=parsed_date.strftime('%Y-%m-%d'),
                email=email
            )
            # Update the employee in the database
            db.update(updated_emp)

            return jsonify({
                'res': updated_emp.serialize(),
                'status': '200',
                'msg': f'Success updating the employee with emp_id {emp_id}!'
            })
        else:
            # Create the employee object with correct attribute values
            emp = Employee(
                id=db.getNewId(),
                emp_id=emp_id,
                name=name,
                isActive=isActive,
                dateOfJoining=parsed_date.strftime('%Y-%m-%d'),
                email=email
            )

            # Insert the employee into the database
            db.insert(emp)

            return jsonify({
                'res': emp.serialize(),
                'status': '200',
                'msg': 'Success creating a new employee!'
            })
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def DeleteEmployeeController(emp_id):
    req_args = request.view_args
    emps = [emp.serialize() for emp in db.view()]
    if req_args:
        for emp in emps:
            if emp['emp_id'] == int(req_args['emp_id']):
                db.delete(emp['emp_id'])
                updated_emps = [emp.serialize() for emp in db.view()]
                return jsonify({
                    'res': updated_emps,
                    'status': '200',
                    'msg': 'Success deleting employee by ID!',
                    'no_of_employees': len(updated_emps)
                })
        return jsonify({
            'error': f"Employee Id Not Found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
            'error': f"Error ⛔❌! No employee ID sent!",
            'res': '',
            'status': '404'
        })