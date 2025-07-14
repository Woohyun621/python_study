#리스트 4번

def minuslist(x):
  print("실행 전",x)
  x_after = [-i if 3<=i and i<=8 else i for i in x]
  print("실행 후", x_after)
  
x = [1,2,3,4,5,6,7,8,9,10]

minuslist(x)