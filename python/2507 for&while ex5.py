#for/while 반복문 5번

x = int(input("정수 입력 : "))

for y in range(x+1):
  for z in range(y):
    print("*", end=" ")
  print()