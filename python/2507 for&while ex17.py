#for/while 반복문 17번

for i in range(0,10):
  if i%3==0 and i%5==0:
    print("fizzbuzz")
  elif i%5==0:
    print("buzz")
  elif i%3==0:
    print("fizz")
  else:
    print("*")

