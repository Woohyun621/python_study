import time
import random

print("타자 속도 테스트입니다.")
input("아무 타자를 누르면 문장이 나옵니다...")


time_start = time.time()

list1 = ["참치김밥","땡초김밥","돈가스김밥","새우김밥","계란김밥","멸치김밥","소고기김밥","김치김밥","치즈김밥"]
random_list = random.choice(list1)
print(f"선택된 문장 : {random_list}")
trial = 1

while True:

  typed = input(f"\n {random_list} 입력: ")
  print(f"적은 문장 : {typed}")

  time_end = time.time()
  elapsed = time_end - time_start

  correct = 0
  for i in range(min(len(random_list), len(typed))):
    if random_list[i] == typed[i] :
      correct += 1
  
  total = max(len(random_list), len(typed))
  accuracy = correct / total * 100
  speed = len(list1) / elapsed * 60  #분당 타자 수(CPM)
  
  if accuracy == 100:
    print("완료했어요.")
    break
  else:
    print("다시 시도해보세요.")
    trial += 1


print(f"정확도 : {accuracy} %")
print(f"시도 횟수 : {trial}번")
print(f"걸린 시간 : {elapsed: .2f}초")