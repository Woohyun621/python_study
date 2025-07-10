#for/while 반복문 2번

myList = [11,22,23,99,81,93,35]
y=0

for x in range(len(myList)):
  y = myList[x] + y  
print(y)