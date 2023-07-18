import mysql.connector as conn

mydb = conn.connect( host = "localhost", user = "root", passwd = "Mani@143K") # establish a connection
cursor = mydb.cursor()  # create cursor
cursor.execute("insert into testdb1.ineuron1 values(101, 'Kumar', 'kumaka@gmail.com', 1000, 30)")
#  'connection commit is required'
mydb.commit()  # asuring the work , commiting my work here.
cursor.execute("select * from testdb1.ineuron1")

for i in cursor.fetchall():
    print(i)

#  only want to select particular part of the table.
