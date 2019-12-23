data="All student are stupids"
f=open("abc.txt",'w')
f.write(data)
with open("abc.txt",'r+') as f:
    text=f.read()
    print(text)
    print("The current cursor position :",f.tell())
    f.seek(17)
    print("The current cursor position :",f.tell())
    f.write("GEMS!!!")
    f.seek(0)
    text=f.read()
    print("Data after modification..")
    print(text)
    