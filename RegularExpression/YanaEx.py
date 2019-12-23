import re
s=input("Enter identifire:")
m=re.fullmatch("[a-k][0369][a-zA-z0-9#]*",s)
if m !=None:
    print(s,"is valid Yava identifier")
else:
    print(s,"is invalid Yava identifier")