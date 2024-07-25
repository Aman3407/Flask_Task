import sqlite3, random, datetime
from models import Employee

def getNewId():
    return random.getrandbits(28)

def connect():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER , emp_id INTEGER PRIMARY KEY, name STRING, isActive BOOLEAN, dateOfJoining DATE, email STRING)")
    conn.commit()
    conn.close()

def insert(employee):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    print(f"Inserting employee: id={employee.id} (type={type(employee.id)}), emp_id={employee.emp_id} (type={type(employee.emp_id)}), "
          f"name={employee.name} (type={type(employee.name)}), isActive={employee.isActive} (type={type(employee.isActive)}), "
          f"dateOfJoining={employee.dateOfJoining} (type={type(employee.dateOfJoining)}), email={employee.email} (type={type(employee.email)})")

    cur.execute("INSERT INTO employees (id, emp_id, name, isActive, dateOfJoining, email) VALUES (?, ?, ?, ?, ?, ?)", (
        employee.id,
        employee.emp_id,
        employee.name,
        employee.isActive,
        employee.dateOfJoining,
        employee.email
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    employees = []
    for i in rows:
        employee = Employee(i[0], i[1], i[2], i[3], i[4], i[5])
        employees.append(employee)
    conn.close()
    return employees

def update(employee):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("UPDATE employees SET name=?, isActive=?, dateOfJoining=?, email=? WHERE emp_id=?", (
        employee.name,
        employee.isActive,
        employee.dateOfJoining,
        employee.email,
        employee.emp_id
    ))
    conn.commit()
    conn.close()

def delete(emp_id):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
    conn.commit()
    conn.close()