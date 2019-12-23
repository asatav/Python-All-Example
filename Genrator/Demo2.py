def countdown(num):
    print("start Coundown")
    while(num>0):
        yield num
        num=num-1
values=countdown(5)
for x in values:
    print(x)