#리스트 3번

list1 = [20,1,12,9,18]

for i in range(len(list1)):
  print(f"{list1[i]} : ")
  z = list1[i]
  for y in range(z):
    print("*",end="")
  print("\n")