import re 
l=re.subn("[a-z]","#","a7b9c5kz")
print(l)
print("The result String:",l[0])
print("The no of replacement:",l[1])