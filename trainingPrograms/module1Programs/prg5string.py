

print("select one of the choice 1=alphanumeric or numeric,0=alpha")
choice=input("enter choice: ")
inputString=input("enter the string of words with comma separator:")
print(inputString)
listOfString=inputString.split(",")
print(listOfString)
unRepeatedList=[]
for i in listOfString:
    if i not in unRepeatedList:
        unRepeatedList.append(i)
print("string without duplicate elements",unRepeatedList)

repeated=[]

i=0
while(i<len(listOfString)):
    if(i<(len(listOfString)-1)):
        j=i+1
        while(j<len(listOfString)):
            if((listOfString[i]==listOfString[j])):
                repeated.append(listOfString[i])
            j+=1
                   
    if(i==(len(listOfString)-1)):
        k=0
        while(k<len(repeated)):
             if((listOfString[i]==repeated[k])):
                repeated.append(listOfString[i])
                
             k+=1

    i+=1    
print("repeated elements in the list",repeated)   
unique=[x  for x in  unRepeatedList if x not in repeated]
print("non repeated elements in the list",unique)
if(choice==1):
    unRepeatedList=[int(x) for x in unRepeatedList]
    unique=[int(x) for x in unique]
unique.sort()
unRepeatedList.sort()
print("sorted non repeated elements in the list :",unique)    
print("sorted string without duplicate elements :",unRepeatedList)
