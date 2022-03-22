def permutation(list_data):
    result=[]
    count=0
    for k in list_data:
        list_data.extend(k)
        list_data.remove(k)
        for j in list_data[1:]:
            list_data.extend(j)
            list_data.remove(j) 
            for i in list_data[2:]:
                list_data.extend(i)
                list_data.remove(i)
                result.append(list_data[:4])
                count+=1
    print(count)   
    return result

    
data_tuple=( [1,3,6,9],"1369","1396")                
print("select one string 0) {} 1){} 2) {} ".format(data_tuple[0],data_tuple[1],data_tuple[2]))
choice=input("make  selection  0 or 1 or 2 : ")
print(str(data_tuple[0]))
if choice=="1"or choice=="2":
    data_list=[]
    for i in data_tuple[int(choice)]:
        data_list.append(i)
    print(data_list)
    result=permutation(data_list)
    print(result)
else:
    data_list=[str(x) for x in data_tuple[0]]
    result=permutation(data_list)
    print(result)
    
