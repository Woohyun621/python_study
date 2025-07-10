#for/while 반복문 13번

num = int(input("몇 번째 항까지 구할까요? : "))
e1=0
e2=0

for i in range(num+1):
  if i<2:
    e2=e1
    e1=i
    sum=e1+e2
  else:
    sum=e1+e2
    e2=e1
    e1=sum
  
  if i!=num:
    print(sum,end=",")
  else:
     print(sum)