#for/while 반복문 10번

x = int(input("정수 입력 : "))
z = 0

for y in range(x+1):
  z = (y*y) + z
print(f"값 : {z}")