import mysql.connector as conn

mydb = conn.connect( host = "localhost", user = "root", passwd = "Mani@143K") # establish a connection
cursor = mydb.cursor()  # create cursor
cursor.execute("select emp_name, emp_id from testdb1.ineuron1")
l = []
for i in cursor.fetchall():
    print(i)
    l.append(i)

print(l)
print(type(l[0]))

