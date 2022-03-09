import math
array=list(map(int,input("array elements :").strip().split()))
n=len(array)
print("lenght of the array =" + str(n))
first=0
last=n-1
div=math.trunc(n/2)
div_count=0
middle=div

while(div):
  div=math.trunc(div/2)
  div_count=div_count+1
print("no.of div =" + str(div_count))  
array.sort()
print("sorted array =" + str(array))
search_item=int(input("enter search element:"))
while(div_count):
    if array[middle]==search_item:
       print("position of the element is in = "+ str(middle))
       break
    if search_item > array[middle]:
      first=middle+1
      middle=middle+math.trunc((last-middle)/2) 
    if search_item < array[middle]:
      last=middle-1
      middle= middle-math.trunc((middle-first)/2)   
    div_count=div_count-1
    

if array[middle]!=search_item :
    print("element not found")