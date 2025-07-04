#if 조건문 5번

a = int(input("첫 번째 정수 : "))
b = int(input("두 번째 정수 : "))
c = int(input("세 번째 정수 : "))

if(a<b and a<c):
  print(a)
elif(b<a and b<c):
  print(b)
else:
  print(c)