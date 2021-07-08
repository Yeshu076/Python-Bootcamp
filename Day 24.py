
#1) Create a JSON of all object types and import the JSON into a SQL Database

import json

json_data = [
    {'name': "Yeshwanth", 'age': 20, 'Permanent_staff': True, 'salary': 75000.00, 'dept_desgn': 'Developer'},
    {'name': "Tahir", 'age': 21, 'Permanent_staff': False, 'salary': 56000.00, 'dept_desgn': "ML Engineer"},
    {'name': "Vijayan", 'age': 21, 'Permanent_staff': True, 'salary': 78000.00, 'dept_desgn': 'Web Designer'},
    {'name': "Narendhran", 'age': 20, 'Permanent_staff': True, 'salary': 45000.00, 'dept_desgn': 'Data Scientist'},
    {'name': "Sriram", 'age': 21, 'Permanent_staff': True, 'salary': 67000.00, 'dept_desgn': 'Manager'}
]

res =json.dumps(json_data)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

print(mydb)

dbse = mydb.cursor()
dbse.execute("CREATE DATABASE JSONRECORDS1")

dbse = mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
  print(entry)

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="jsonrecords1"
)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE employee (name VARCHAR(255),age INT, permanent_staff VARCHAR(255), salary DOUBLE, dept_and_designation VARCHAR(255))")

dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for value in dbse:
  print(value)

dbse = mydb.cursor()
dbse.execute("SHOW COLUMNS FROM employee")
for value in dbse:
  print(value)

dbse = mydb.cursor()
sql = "INSERT INTO employee (name ,age, permanent_staff,salary,dept_designation) VALUES (%s)"

