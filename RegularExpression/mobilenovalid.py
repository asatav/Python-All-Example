import re
s=input("Enter Mobile no:")
m=re.fullmatch("[7-9]\d{9}",s)
if m !=None:
    print(s,"is valid Mobile no")
else:
    print(s,"is invalid Mobile no")