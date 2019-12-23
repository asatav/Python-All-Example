def addition(n1,n2):
    print("inside addition")
    print(n1+n2)
def substraction(n1,n2):
    print("inside substraction")
    print(n1-n2)
def multiplication(n1,n2):
    print("inside multiplication")
    print(n1*n2)
def division(n1,n2):
    print("inside division")
    print(n1/n2)
def operation(choice):
    my_switch_stmt={
            1:addition,
            2:substraction,
            3:multiplication,
            4:division,
            }
    op=my_switch_stmt.get(choice)
    if op:
        op(10,40)
    else:
        print("invalid choice")
operation(5)        
