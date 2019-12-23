import re
s=input("Enter pattern to check:")
m=re.fullmatch(s,"abcabdefg")
if m!=None:
    print("Full string match")
   
else:
    print("Full string not match")