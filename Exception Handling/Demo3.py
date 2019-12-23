class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg

class TooOlderException(Exception):
    def __init__(self,arg):
        self.msg=arg
        
age=int(input("Enter Age:"))
if age>60:
    raise TooYoungException("Plz wait for some time you are so young.")
elif age<18:
    raise TooOlderException("Plz wait for some time you are so Older.")
else:
    print("You will get match soon.....")