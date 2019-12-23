import os,sys
fname=input("Enter the file name:")
if os.path.isfile(fname):
    print("File Exist:",fname)
    f=open(fname,'r')
else:
    print("File does not Exist:",fname)
    sys.exit()
print("The content of file is:")
data=f.read()
print(data)
    