stackOfOperands=[]
resultPostFixStr=''
def strtolistfun(input_string):
    strToList=[]
    for i in range(len(input_string)):
        strToList.append(input_string[i])
    return strToList
def priorityNassosiativity(op,resultPostFixStr):
    dict_operands={3:"^",4:["*","/"],5:["+","-"]}
    if (op==dict_operands[3]):
        stackOfOperands.append(op)
    if op in dict_operands[4]:
        if(len(stackOfOperands)==0):
            stackOfOperands.append(op)
        else:
            if(stackOfOperands[-1]==dict_operands[3] or stackOfOperands[-1] in dict_operands[4]):
                while(len(stackOfOperands)):
                    if(stackOfOperands[-1]==dict_operands[3] or (stackOfOperands[-1] in dict_operands[4])):
                        resultPostFixStr=resultPostFixStr+stackOfOperands[-1]
                         
                    elif(stackOfOperands[-1] in dict_operands[5]):
                        
                        stackOfOperands.append(op)
                        break
                    stackOfOperands.pop()
                        
                stackOfOperands.append(op)   
                        
            elif(stackOfOperands[-1] in dict_operands[5]):
                stackOfOperands.append(op)


    if op in dict_operands[5]:
        while(len(stackOfOperands)):
            resultPostFixStr=resultPostFixStr+stackOfOperands[-1]        
            stackOfOperands.pop()
        stackOfOperands.append(op)  
         
            
    return resultPostFixStr

    



input_string=input("enter the string:")
listOfstring=strtolistfun(input_string)
print(listOfstring)
list_op=["^","*","/","+","-"]
parenthesis=["(",")"]
i=0
while(i<len(listOfstring)):
    if listOfstring[i].isalnum():
        resultPostFixStr=resultPostFixStr+listOfstring[i]
    
        i+=1
    elif listOfstring[i] in list_op:
        resultPostFixStr = priorityNassosiativity(listOfstring[i],resultPostFixStr)
        i+=1
    elif listOfstring[i] == parenthesis[0]:
        
        
            
            i+=1 
            while( not (listOfstring[i]==parenthesis[1])): 
                count=1
                if listOfstring[i].isalnum():
                    resultPostFixStr=resultPostFixStr+listOfstring[i]
                    i+=1
                elif listOfstring[i] in list_op:
                    resultPostFixStr = priorityNassosiativity(listOfstring[i],resultPostFixStr)
                    i+=1 
               
                  
                else:
                    print("invalid string input")
                    break
                count+=1 
            if listOfstring[i]==parenthesis[1]:
                   
                   while(len(stackOfOperands) and count!=0):
                        resultPostFixStr=resultPostFixStr+stackOfOperands[-1]        
                        stackOfOperands.pop() 
                        count-=1
                  
            i+=1  
            
    
            

    else:
        print("invalid string input")
        break
    
while(len(stackOfOperands)):
    resultPostFixStr=resultPostFixStr+stackOfOperands[-1]
    stackOfOperands.pop()
      
print(resultPostFixStr)      