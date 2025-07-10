#for/while 반복문 3번

y=0

for x in range(1,101):
  if x%3==0 :
    y += x
print(f"1부터 100까지 3의 배수의 합은 : {y}입니다.")