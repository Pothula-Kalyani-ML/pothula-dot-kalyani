from sorted_list2_merge import *
list1=[2,5,9]
list2=[3,5,9,11]
list3=[4,20,21,24,26]
list4=[10,13,85,100,101]
result1=[]
result2=[]
result=[]
'''result1=merge(list1,list2)
result2=merge(list3,list4)
result=merge(result1,result2)
print(result)'''
result1=merge_list(list1,list2)
result2=merge_list(result1,list3)
result=merge_list(result2,list4)
print(result)

