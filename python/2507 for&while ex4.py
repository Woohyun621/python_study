#for/while 반복문 4번

x = int(input("정수를 입력하시오:"))

for i in range(1,x+1):
  if x%i==0:
    print(i,end=" ")