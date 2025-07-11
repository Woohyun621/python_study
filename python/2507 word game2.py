import random

def word1():
  if word == back :
      count += 1
      print("정답")

print("속담 맞추기 게임\n")
count=0

list1=[["가는날이","장날이다"],["금강산도","식후경"],["꿩 대신", "닭"],["누워서","떡 먹기"],["도토리","키 재기"],["되로 주고","말로 받는다"],
         ["등잔 밑이","어둡다"],["바늘 도둑이","소 도둑 된다"],["병 주고","약 준다"]]

for i in range(5):
  front , back = random.choice(list1)
  print(f"속담 : \"{front}\"")
  word = input(f"\"{front}\" 뒤로 올 말을 적으시오 : ").strip()
  print(f'"{word}"')
  
  if word == back :
    count += 1
    print("정답")
  else:
    print("오답")
    print(f"첫 글자 힌트 : {back[0:1]}")
    word = input(f"\"{front}\" 힌트 : {back[0:1]} 로 시작합니다. : ").strip()
    print(f'"{word}"')
    
    if word == back :
      count += 1
      print("정답")
    else:
      print("오답")
      
  list1.remove([front,back])
  print()

i+=1
print(f"{i}개의 문제 중 {count}개를 맞춤.")