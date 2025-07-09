#if 조건문 6번

import random

a = ["가위","바위","보"]
c = random.randint(1,3)
b = a[c]
c = input("가위 바위 보 중 하나를 선택하세요 : ")

print("상대는", b,"를 냈습니다.")
print("당신은", c,"를 냈습니다.")

if (c == "가위" and b == "보") or (c == "바위" and b == "가위") or (c == "보" and b == "바위"):
  print("이겼음")
elif (c == "가위" and b == "가위") or (c == "바위" and b == "바위") or (c == "보" and b == "보"):
  print("비겼음")
else:
  print("졌음")