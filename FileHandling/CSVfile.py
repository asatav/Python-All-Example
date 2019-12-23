import csv
with open("emp.csv",'w',newline="") as f:
    w=csv.writer(f)
    w.writerow(["ENO","ENAME","ESAL","EADDER"])
    n=int(input("Enter the employee No:"))
    for i in range(n):
        eno=input("Enter Employee No:")
        ename=input("Enter Employee Name:")
        esal=input("Enter Employee Salary:")
        eaddr=input("Enter Employee Address:")
        w.writerow([eno,ename,esal,eaddr])
print("Totle Employee data wrritten to csv file successfully")
        