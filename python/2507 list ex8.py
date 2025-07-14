#리스트 8번
def single_list(alist):
  aset=set(alist)
  non_same=list(aset)
  return non_same

def same_element(list1,list2):
  same_list=[i for i in list1 for j in list2 if i==j]
  only=single_list(same_list)
  print("결과 = ", only)
  
a = [1,2,3,4,5]
b = [1,3,3,4,5,6,7]
print("a=",a)
print("b=",b)
same_element(a,b)