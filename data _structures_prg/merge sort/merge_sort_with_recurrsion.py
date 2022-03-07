import math
from sorted_list2_merge import merge_list
def merge(array_list,first_index,last_index,middle_index):
    left_array=[]
    right_array=[]
    result=[]
    while(first_index<middle_index):
        left_array.append(array_list[first_index])
        first_index+=1
    while(middle_index<=last_index):

        right_array.append(array_list[middle_index])
        middle_index+=middle_index  
    result= merge_list(left_array,right_array)
    array_list=result  



def merge_sort(array_list,first_index,last_index):
    
    if(first_index<last_index):
        middle_index=math.trunc(first_index+(last_index-1)/2)
        merge_sort(array_list,first_index,middle_index)
        merge_sort(array_list,middle_index-1,last_index)
        merge(array_list,first_index,last_index,middle_index)
if __name__ == "__main__":    
    array_list=[23,12,15,32,2,10,24,35,89,98,72,65,61,35]
    first_index=0
    last_index=len(array_list)
    merge_sort(array_list,first_index,last_index)
    print(array_list)

    

     