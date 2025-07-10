#for/while 반복문 15번

sum = 0

for i in range(1,100,2):
  for j in range(3,102,2):
    k = i/j
    sum += k
print(sum)