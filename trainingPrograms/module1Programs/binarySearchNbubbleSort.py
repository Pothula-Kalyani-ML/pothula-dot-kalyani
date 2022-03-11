import math
def binarySearch(array,search_item):
    n=len(array)
    print("lenght of the array =" + str(n))
    first=0
    last=n-1
    middle=math.trunc(first+last/2)
    array.sort()
    print("sorted array =" + str(array))
    while(last-first>1):
        if search_item==array[middle]:
            return middle
        elif search_item > array[middle]:
            first=middle+1
            middle=middle+math.trunc((last-middle)/2)     
        elif search_item < array[middle]:        
            last=middle-1
            middle= middle-math.trunc((middle-first)/2)
    if(search_item==array[last]):
        return last
    elif(search_item==array[first]):
        return first 
    else:return -1   

def bubblesort(array):
    length=len(array)
    for j in range(len(array)-1):
        for i in range(0,length-1):
            sequenceChange=False
            if array[i] > array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
                sequenceChange=True
        length=length-1 
        if sequenceChange==False:
            return array
    return array    
if __name__ == "__main__":  
    print("enter array elements with spaces ")              
    array=list(map(int,input("array elements :").strip().split()))
    search_item=int(input("enter search element: "))
    sortedArray=bubblesort(array)
    first=0
    last=len(array)-1
    result=binarySearch(array,search_item)
    print(result)
    if result==-1:
        print(" element {} not found in the list: ".format(search_item))
    else: 
        print ("position of {} in the list is: {}".format(search_item,result))
        
