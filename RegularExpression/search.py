import re
s=input("Enter pattern to check:")
m=re.search(s,"abaaaba")
if m!=None:
    print("Match is avialable at the begining of the String")
    print("Start index:",m.start(),"and End Index:",m.end())
else:
    print("Match is not avialable at the begining of the String")