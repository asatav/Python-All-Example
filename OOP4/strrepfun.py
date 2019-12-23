import datetime
today=datetime.datetime.now()
s=repr(today)
print(s)
d=eval(s)
print(d)