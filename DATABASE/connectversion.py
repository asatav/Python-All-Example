import mysql.connector


con=mysql.connector.connect(host='localhost',database='python',user='root',password='root')
print(con.version)
    