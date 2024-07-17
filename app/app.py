from flask import Flask, render_template, request, jsonify
import os, re, datetime
import db
from models import Employee

app = Flask(__name__)

# create the database and table. 
# the db multiple times
if not os.path.isfile('employees.db'):
    db.connect()

@app.route("/employee/new", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    name = req_data['name']
    isActive = req_data['isActive']
    dateOfJoining = req_data["dateOfJoining"]
    emp = Employee(db.getNewId(), name,isActive,dateOfJoining)
    db.insert(emp)
    new_emps = [emp.serialize() for emp in db.view()]
    return jsonify({
                'res': emp.serialize(),
                'status': '200',
                'msg': 'Success creating a new employee!'
            })



@app.route('/employees', methods=['GET'])
def getRequest():
    emps = [emp.serialize() for emp in db.view()]
    return jsonify({
        'res': emps,
        'status': '200',
        'msg': 'Success getting all employees in library!'
    })


@app.route('/employee/<id>', methods=['GET'])
def getRequestId(id):
    req_args = request.view_args
    emps = [emp.serialize() for emp in db.view()]
    if req_args:
        for emp in emps:
            if emp['id'] == int(req_args['id']):
                return jsonify({
                    'res': emp,
                    'status': '200',
                    'msg': f'Success getting employee by {id}!'
                })
        return jsonify({
            'error': f"Error ⛔❌! employee with id '{req_args['id']}' was not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': emps,
                    'status': '200',
                    'msg': 'Success getting employee by ID!',
                    'no_of_employees': len(emps)
                })

@app.route("/employee/<id>", methods=['PUT'])
def putRequest(id):
    req_data = request.get_json()
    req_args = request.view_args
    # print(req_args)
    id = req_args['id']
    name = req_data['name']
    isActive = req_data['isActive']
    dateOfJoining = req_data['dateOfJoining']
    emps = [emp.serialize() for emp in db.view()]
    print(emps)
    for emp in emps:
        if emp['id'] == int(id):
            emp = Employee(
                id, 
                name, 
                isActive, 
                dateOfJoining
            )
            print(emp)
            db.update(emp)
            return jsonify({
                # 'error': '',
                'res': emp.serialize(),
                'status': '200',
                'msg': f'Success updating the employee with id {id}!'
            })        
    return jsonify({
                # 'error': '',
                'res': f'Error ⛔❌! Failed to update employee with id {id}!',
                'status': '404'
            })
    
    


@app.route('/employee/<id>', methods=['DELETE'])
def deleteRequest(id):
    req_args = request.view_args
    emps = [emp.serialize() for emp in db.view()]
    if req_args:
        for emp in emps:
            if emp['id'] == int(req_args['id']):
                db.delete(emp['id'])
                updated_emps = [emp.serialize() for emp in db.view()]
                return jsonify({
                    'res': updated_emps,
                    'status': '200',
                    'msg': 'Success deleting employee by ID!',
                    'no_of_employees': len(updated_emps)
                })
    else:
        return jsonify({
            'error': f"Error ⛔❌! No employee ID sent!",
            'res': '',
            'status': '404'
        })

if __name__ == '__main__':
    app.run()