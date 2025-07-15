#튜플,세트,딕셔너리 1번
def main1(list1):
  list2 = set(list1)
  list2 = list(list2)
  list2.sort()
  print(list1)
  print(list2)

my_list = list()
for i in range(5):
  my_list.append(int(input("임의의 정수값을 입력하세요 : ")))
  
main1(my_list)