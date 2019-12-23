#map function in lambda
mylist=[1,2,3,4,5,6]
newlist=list(map(lambda a:(a/3!=2),mylist))#syntsx map(function,iterable)
print(newlist)