a,b=10,20
x=30 if a<b else 40
print(x)
print("********Mininmum of 3 no**********")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
min=a if a<b and a<c else b if b<c else c
print("Minimum Value:",min)
print("********Maximum of 3 no**********")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
max=a if a>b and a>c else b if b>c else c
print("Maximumm Value:",max)
