import mysql.connector

try:
    con=mysql.connector.connect(host='localhost',database='python',user='root',password='root')
    cursor=con.cursor()
    '''
    cursor.execute("create table employees(eno int(5) primary key,ename varchar(10),esal double(10,2),eadde varchar(10))")
    print("Table created....")
    sql="insert into employees(eno,ename,esal,eadde) values(%s,%s,%s,%s)"
    records=[(101,'ASHISH',1000,'PUNE'),
             (102,'AJIT',1001,'PUNE'),
             (103,'ARNAV',1200,'PUNE'),
             (104,'AROHI',1300,'PUNE')]
    cursor.executemany(sql,records)
    con.commit()
    print("Record inserted successfully.....")'''
    cursor.execute("select * from employees")
    data=cursor.fetchall()
    for row in data:
        print("Employee no:",row[0])
        print("Employee name:",row[1])
        print("Employee salary:",row[2])
        print("Employee address:",row[3])
        print()
        print()
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()