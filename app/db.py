import sqlite3, random, datetime
from models import Employee

def getNewId():
    return random.getrandbits(28)

def connect():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY,name STRING, isActive BOOLEAN, dateOfJoining DATE)")
    conn.commit()
    conn.close()

def insert(employee):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO employees VALUES (?,?,?,?)", (
        employee.id,
        employee.name,
        employee.isActive,
        employee.dateOfJoining
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
        employee = Employee(i[0], i[1], i[2], i[3])
        employees.append(employee)
    conn.close()
    return employees

def update(employee):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("UPDATE employees SET name=?, isActive=?, dateOfJoining=? WHERE id=?", (employee.name, employee.isActive,employee.dateOfJoining, employee.id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM employees")
    conn.commit()
    conn.close()