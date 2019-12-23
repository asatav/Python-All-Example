import re 
s="Lerning Python is Very Easy"
res=re.search("Easy$",s)
if res !=None:
    print("Target String starts with Easy")
else:
    print("Target String Not starts with Easy")