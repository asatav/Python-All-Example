print("stmt-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/1)
    print("stmt-3")