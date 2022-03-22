def palindrome(input_string):
    first_index = 0
    last_index = len(input_string)-1
    while last_index > first_index:
        if input_string[first_index] != input_string[last_index]:
            return False
        first_index += 1
        last_index -= 1
    return True


if __name__ == "__main__":
    input_str = input("enter a string to check palindrome: ")
    RESULT = palindrome(input_str)
    print("is the string is palindrome:",RESULT)
