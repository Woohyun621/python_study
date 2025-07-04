#7번

x1 = int(input("x1의 좌표 : "))
y1 = int(input("y1의 좌표 : "))
x2 = int(input("x2의 좌표 : "))
y2 = int(input("y2의 좌표 : "))

a = (((x1 - x2)**2) + ((y1-y2)**2))**0.5

print("두 점 사이의 거리 : ", a)
