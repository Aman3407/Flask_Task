from flask import Flask, request, jsonify
import os,re
import db
from models import Employee
from datetime import datetime
from controller import createEmployeeController,getEmployeeDetailsController,UpdateEmployeeController,CreateOrUpdateEmployeeController,DeleteEmployeeController

app = Flask(__name__)

# Create the database and table if it doesn't exist
if not os.path.isfile('employees.db'):
    db.connect()

@app.route("/employee", methods=['POST'])
def postRequest():
    return createEmployeeController()

@app.route('/employee/<emp_id>', methods=['GET','PUT','PATCH','DELETE'])
def Controller(emp_id):
    if request.method == 'GET':
        return getEmployeeDetailsController(emp_id)
    elif request.method == 'PUT':
        return UpdateEmployeeController(emp_id)
    elif request.method == 'DELETE':
        return DeleteEmployeeController(emp_id)
    elif request.method == 'PATCH':
        return CreateOrUpdateEmployeeController(emp_id)
    else:
        return 'Method not allowed', 405

if __name__ == '__main__':
    app.run(debug=True)
