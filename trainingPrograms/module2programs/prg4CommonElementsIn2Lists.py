
def CommonElementsInTwoUnorderedlists(list1,list2):
    commonlist=[]
    for i in list1:
        for j in list2:
            if i==j:
                commonlist.append(i)
    return commonlist
def CommonElementsInTwoOrderedLists(list1,list2):
    pass
if __name__=="__main__":   
    testlist=[[7, 1, 5, 2, 3, 6],[3, 8, 6, 20, 7]]
    commonList=CommonElementsInTwoUnorderedlists(testlist[0],testlist[1])
    print(commonList)
    orderedList=[sorted(testlist[0]),sorted(testlist[1])]
    print(orderedList)
