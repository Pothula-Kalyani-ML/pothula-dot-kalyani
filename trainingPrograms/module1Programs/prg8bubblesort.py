array=list(map(int, input("elements of array:-").strip().split()))
print(array)
length=len(array)
print(length)
count=length
while(count): 
    for i in range(0,count-1):
        if array[i] > array[i+1]:
            temp=array[i]
            array[i]=array[i+1]
            array[i+1]=temp
        for i in range(length):
            print(array[i],end=" ")
        print(end=" ")
           
    print(" ")        
    count=count-1  