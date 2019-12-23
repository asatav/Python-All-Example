def m1():
    print("inside m1")
    return 10==20
def m2():
    print("inside m2")
    return 10
def m3():
    print("inside m3")
if m1() or m2() or m3():
    print("inside if")
else:
    print("inside else")        
    
    