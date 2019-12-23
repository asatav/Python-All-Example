try:
    x=int(input("Enter number:-"))
    y=int(input("Enter number:-"))
    print(x/y)
except ZeroDivisionError:
    print("Cant Divide with zero")
except ValueError:
    print("please provide int value only")
finally:
    print("Predefine Exception")