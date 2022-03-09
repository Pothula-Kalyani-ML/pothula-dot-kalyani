
def permutationOfElements(listData):
    result=[]
    count=0
    
    for k in listData:
        listData.extend(k)
        listData.remove(k)
        for j in listData[1:]:
            listData.extend(j)
            listData.remove(j) 
            for i in listData[2:]:
                listData.extend(i)
                listData.remove(i)
                result.append(listData[:4])
                count+=1
    print(count)   

    return result

    
dataTuple=( [1,3,6,9],"1369","1396")                
print("select one string 0) {} 1){} 2) {} ".format(dataTuple[0],dataTuple[1],dataTuple[2]))
choice=input("make  selection  0 or 1 or 2 : ")
print(str(dataTuple[0]))
if choice=="1"or choice=="2" :
    listData=[]
    for i in dataTuple[int(choice)]:
        listData.append(i)
    print(listData)
    result=permutationOfElements(listData)
    print(result)
else:
    listData=[str(x) for x in dataTuple[0]]
    result=permutationOfElements(listData)
    print(result)
    
