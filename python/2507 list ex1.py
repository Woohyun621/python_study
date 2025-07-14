#리스트 1번

list1 = [10,20,30]
sum = 0
x = int(input("정수를 입력하세요 : "))

for i in range(len(list1)):
  sum = list1[i] + x
  print(sum)