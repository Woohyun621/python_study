#튜플,세트,딕셔너리 4번
def main4():
  d = {1:10,2:20,3:30,4:40,5:50,6:60}
  key = int(input("키를 입력하세요 : "))
  if key in d:
    print("키 %d은(는) 딕셔너리에 있음."% key)
  else:
    print("키 %d은(는) 딕셔너리에 없음."% key)
    
main4()