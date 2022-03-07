
def merge_list(list1,list2):
    i,j=0,0
    result=[]
    while i<len(list1) and j<len(list2):

        if list1[i]<list2[j]:
            result.append(list1[i])
            i+=1
        else:    
            result.append(list2[j]) 
            j+=1
            
    while i<len(list1):
        result.append(list1[i])
        i+=1
        
    while j<len(list2):
        result.append(list2[j] )
        j+=1
       
    return  result
if __name__ == "__main__":    
    sorted_list1=[1,8,10,26,34,52,61]

    sorted_list2=[2,3,9,6,7,21,32,34,78,90]
    resultant_list=[]
    resultant_list=merge_list(sorted_list1,sorted_list2)
    print(resultant_list)  

