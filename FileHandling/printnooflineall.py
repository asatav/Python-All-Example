import os,sys
fname=input("Enter the file name:")
if os.path.isfile(fname):
    print("File Exist:",fname)
    f=open(fname,'r')
else:
    print("File does not Exist:",fname)
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount+=1
    ccount+=len(line)
    words=line.split()
    wcount+=len(words)
print("The nomber of lines:",lcount)
print("The nomber of Words:",wcount)
print("The nomber of Character:",ccount)