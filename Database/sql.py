import mysql.connector
#pip install mysql-connector-python
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="examly",  
)
print(mydb)
mycursor = mydb.cursor(buffered=True)
mycursor("CREATE DATABASE blogging")
mycursor("SHOW DATABASES")
for x in mycursor:
  print(x)
