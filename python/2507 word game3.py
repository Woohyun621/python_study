import random
import time

words = ["가지","다리미","나비","바지","사다리","비누","오이","우유","부채","무지개","주머니","고구마","허수아비","기차","포도","무기","모래","파도","주사기","하마","고양이"]

score = 0
live = 3
speed = 0

while True:
  random_word = random.choice(words)
  print(f"단어 : {random_word}")
  time_start = time.time()
  answer = input(f"{random_word} / 단어를 입력하세요 : ")
  time_end = time.time()
  speed = time_end - time_start
  
  words.remove(random_word)
  
  if speed < 2.0:
    if random_word == answer :
      score += 1
      print(f"걸린시간 : {speed: 2f}")
      print("정답")
    else :
      live -= 1
      print(f"걸린시간 : {speed: 2f}")
      print("오답")
  else :
    live -= 1
    print(f"걸린시간 : {speed: 2f}")
    print("오답")
  
  if live < 1 :
    print("종료")
    break
  
print (f"맞춘 횟수 : {score}번")
time.sleep(0.5)