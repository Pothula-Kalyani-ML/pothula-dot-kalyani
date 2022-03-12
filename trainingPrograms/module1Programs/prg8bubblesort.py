def bubblesort(array):
    length=len(array)
    for j in range(length-1):
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
    print(array)  
    sortedArray=bubblesort(array)
    print("sorted array",sortedArray)
     