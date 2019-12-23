from sys import argv
print("The no of command line argument:",len(argv))
print("The list of command line argument:",argv)
print(" command line argument one by one:")
for x in argv:
    print(x)