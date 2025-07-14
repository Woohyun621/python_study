#함수 7번

def getIntRange(a,b,msg):
  c = 0
  while c < a or c > b:
    c = int(input(msg))
  return c


d = getIntRange(1,12,"월을 입력 : ")
e = getIntRange(1,31,"일을 입력 : ")

print(f"{d}월 {e}일입니다.")