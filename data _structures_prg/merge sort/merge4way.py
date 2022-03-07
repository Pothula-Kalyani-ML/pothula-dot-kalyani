def merge_4way(list1,list2,list3,list4):
    i,j,k,l=0,0,0,0
    result=[] 
    while (i<len(list1) and  j<len(list2) and  k<len(list3) and l<len(list3)):
        if(list1[i]<=list2[j] and list2[j]<=list3[k] and list3[k]<=list4[l]):
            result.append(list4[l])
            l+=1
        if(list1[i]<=list2[j] and list2[j]<=list3[k] and list4[k]<=list3[l]):
            result.append(list3[k])
            k+=1
        if(list1[i]<=list2[j] and list2[j]>=list3[k] and list2[j]>=list4[l]):
            result.append(list2[j])
            j+=1
        if(list1[i]>=list2[j] and list2[j]<=list3[k] and list3[k]<=list4[l]):
            result.append(list1[i])
            i+=1
    while(i<len(list1)):
        result.append(list1[i])
        i+=1
    while(j<len(list2)):
        result.appened(list2[j])
        j+=1
    while(k<len(list3)):
        result.append(list3[k])
        k+=1
    while(l<list4[l]):
        result.append(list3[l])
        l+=1
    return result

if __name__ == "__main__":
    list1=[2,5,9]
    list2=[3,5,9,11]
    list3=[4,20,21,24,26]
    list4=[10,13,85,100,101]
    resultant_list=merge_4way(list1,list2,list3,list4)
    print(resultant_list)