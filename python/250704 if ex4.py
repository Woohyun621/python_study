#if 조건문 4번


x = int(input("원의 반지름을 입력하시오 : "))
y = 3.14 * x * x

if(y > 0):
  print("원의 넓이는 : ", y)
else:
  print("잘못된 값입니다.")