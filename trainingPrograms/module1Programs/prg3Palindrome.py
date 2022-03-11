def palindrome(inputString):
    lengthOfString=len(inputString)
    
    inputString=inputString.lower()
    for i in range(lengthOfString):
        j=lengthOfString
        if inputString[i]!=inputString[j-i-1]:
            return False
        else: return True    
if __name__ == "__main__":  
    inputString=input("enter a string to check palindrome: ")
    
    result=palindrome(inputString)
    print("is the string is palindrome:",result)