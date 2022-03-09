


def palindrome(inputString):
    reverseString=inputString[::-1]
    if (inputString == reverseString):
        return "true"
    else:
        return "false"   
inputString=input("enter a string to check palindrome: ")
if(inputString.isalpha()):
    inputString=inputString.lower()
result=palindrome(inputString)
print("is the string is palindrome:",result)