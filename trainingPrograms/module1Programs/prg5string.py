def unRepeatedElements(listOfString):
    unRepeatedList=[]
    for i in listOfString:
        if i not in unRepeatedList:
            unRepeatedList.append(i)
    return unRepeatedList        

def repeatedElement(listOfString):
    repeated=[]
    i=0
    for i in range(len(listOfString)):
        for j in range(i+1 ,len(listOfString)):
            if((listOfString[i]==listOfString[j])):
                repeated.append(listOfString[i])
        return repeated  
def uniqueElements(listOfString):
    duplicateItems=repeatedElement(listOfString)
    unRepeatedList=unRepeatedElements(listOfString)
    unique=[x  for x in  unRepeatedList if x not in duplicateItems]
    return unique


 

if __name__ == "__main__":  

    print("select one of the choice 1=numeric ,0=alphanumeric")
    choice=input("enter choice: ")
    inputString=input("enter the string of words with comma separator:")
    print(inputString)
    listOfString=inputString.split(",")   
    duplicateItems=repeatedElement(listOfString)
    print("duplicate elements in the list",duplicateItems) 
    unRepeatedList=unRepeatedElements(listOfString)
    print("string without duplicate elements",unRepeatedList)
    unique=uniqueElements(listOfString)
    print("non repeated elements in the list",unique)

    if(choice==1):
        unRepeatedList=[int(x) for x in unRepeatedList]
        unique=[int(x) for x in unique]

