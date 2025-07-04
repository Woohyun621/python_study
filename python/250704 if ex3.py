#if 조건문 3번

x = input("문자를 입력하시오 : ")

if(x == "R" or x == "r"):
  print("Rectangle")
elif(x == "T" or x == "t"):
  print("Triangle")
elif(x == "C" or x == "c"):
  print("Circle")
else:
  print("Unknown")
