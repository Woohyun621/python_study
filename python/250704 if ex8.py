#if 조건문 8번

weight,height = int(input("체중과 키 : "))
std = (height - 100)*(0.9)

if weight>std:
  print("과체중")
elif weight==std:
  print("표준 체중")
else:
  print("저체중")