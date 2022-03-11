import math
def middleInsertionOfString(inputString,insertString):
    lengthOfString=len(inputString)
    middleIndex=math.trunc(lengthOfString/2)
    firstPartOfInputString=''
    lastPartOfInputString=''
    for i in range(0,middleIndex):
        firstPartOfInputString=firstPartOfInputString+inputString[i]
    for i in range(middleIndex,lengthOfString):   
        lastPartOfInputString=lastPartOfInputString+inputString[i]
    return (firstPartOfInputString + insertString + lastPartOfInputString)

if __name__ == "__main__":  

    inputString=input("enter the string:")
    middleString=input("enter the middle string:")
    result=middleInsertionOfString(inputString,middleString)
    print(result)