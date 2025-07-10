#for/while 반복문 14번

maxnum = 20
number = 2

while number<maxnum:
  divisor=2
  prime=True
  
  while divisor<number:
    if number%divisor==0:
      prime=False
      break
    divisor+=1
  if prime:
    print(number,end=" ")
  number+=1