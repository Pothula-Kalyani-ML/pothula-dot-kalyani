
def CommonElementsInTwoUnorderedlists(list1,list2):
    commonlist=[]
    for item in list1:
        if item in list2:
            if item  not in  commonlist:
                commonlist.append(item)    
    return commonlist
def CommonElementsInTwoOrderedLists(list1,list2):
    
    pass
if __name__=="__main__":   
    testlist=[[7, 7, 1,5, 2, 3, 6],[3, 8, 6, 20, 7,7]]
    commonList=CommonElementsInTwoUnorderedlists(testlist[0],testlist[1])
    print(commonList)
    orderedList=[sorted(testlist[0]),sorted(testlist[1])]
    print(orderedList)
