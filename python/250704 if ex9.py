#if 조건문 9번

import random

a = random.randint(1,4)
b = random.randint(1,9)
c = random.randint(1,9)

if a==1:
  print("덧셈")
  d = int(input("%d + %d 의 값 : "% (b , c)))
  e = b + c
  if e == d:
    print("정답입니다.")
  else:
    print("오답입니다.")
    
elif a==2:
  print("뺄셈")
  d = int(input ("%d - %d 의 값 : "% (b , c)))
  e = b - c
  if e == d:
    print("정답입니다.")
  else:
    print("오답입니다.")
    
elif a==3:
  print("곱셈")
  d = int(input("%d x %d 의 값 : "% (b , c) ))
  e = b * c
  if e == d:
    print("정답입니다.")
  else:
    print("오답입니다.")
    
else:
  print("나눗셈")
  d = float(input("%d / %d 의 값 : "% (b , c) ))
  e = b / c
  f = round(e,1) #소숫점 첫 번쨰 자리까지만.
  if f == d:

    print("정답입니다.")
  else:
    print("오답입니다.")
