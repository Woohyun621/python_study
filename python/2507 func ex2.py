#함수 2번

def get_sum(x,y):
  sum=0
  sum = x + y
  return sum

def get_sub(x,y):
  sub=0
  sub = x - y
  return sub

def get_mul(x,y):
  mul=0
  mul = x * y
  return mul

def get_div(x,y):
  div=0
  div = x / y
  return div

x = int(input("첫 번째 정수 : "))
y = int(input("두 번째 정수 : "))

value_sum = get_sum(x,y)
value_sub = get_sub(x,y)
value_mul = get_mul(x,y)
value_div = get_div(x,y)

print(f"첫 번째 정수 : {x}")
print(f"두 번째 정수 : {y}")

print(f"{x} + {y} = {value_sum}")
print(f"{x} + {y} = {value_sub}")
print(f"{x} + {y} = {value_mul}")
print(f"{x} + {y} = {value_div}")