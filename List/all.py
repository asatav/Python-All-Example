num=[10,20,30,40,50]

n=len(num)
print('No of elements in num :',n)

num.append(60)
print('Num after appending 60 :',num)

num.insert(0,5)
print('Num after inserting at 0 the position  :',num)

num1 = num.copy()
print('Newly created list num1  :',num1)

num.extend(num1)
print('Num after appending num1 :',num)

n = num.count(50)
print('No of times 50 found in the list num  :',n)

num.remove(50)
print('Num after removeing 50  :',num)

num.pop()
print('Num after removing ending element:',num)

num.sort()
print('Num after sorting:',num)

num.reverse()
print('Num after reversing:',num)

num.clear()
print('Num after removing all element:',num)




