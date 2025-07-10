#for/while 반복문 11번

a = int(input("1번째 정수 입력 : "))
b = int(input("2번째 정수 입력 : "))

c = 0
max = a

if a<b:
  max = b
else:
  max = a
  
for i in range(1,max):
  if a%i==0 and b%i==0:
    c = 1

print(f"{a}와 {b}의 최대 공약수는 {c}입니다.")