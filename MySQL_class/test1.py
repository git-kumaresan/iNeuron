import mysql.connector as conn

mydb = conn.connect( host = "localhost", user = "root", passwd = "Mani@143K") # establish a conection
cursor = mydb.cursor() # create cursor
# cursor.execute("create database testdb1")
# cursor.execute("create table testdb1.ineuron1( emp_id int(10), emp_name varchar(15), emp_email varchar(20), emp_salary int(8), emp_attendance int(5))")
cursor.execute("show databases") # to execute a query
print(cursor.fetchall()) # to show executed query

q2 = cursor.execute("select * from testdb1.ineuron1")
print(q2)