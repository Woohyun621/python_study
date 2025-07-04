#3번
import math

x = float(input("첫 번째 변의 길이 : "))
y = float(input("두 번째 변의 길이 : "))

z = (x**2) + (y**2)

print("나머지 변의 길이 : %d" % (math.sqrt(z)))