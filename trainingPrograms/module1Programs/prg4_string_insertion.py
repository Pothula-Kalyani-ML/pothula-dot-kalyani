import math


def string_middle_insertion(input_string, insert_string):
    length_of_string = len(input_string)
    middle_index = math.trunc(length_of_string/2)
    first_part_input_string = ''
    last_part_input_string = ''
    for i in range(0, middle_index):
        first_part_input_string = first_part_input_string+input_string[i]
    for i in range(middle_index, length_of_string):
        last_part_input_string = last_part_input_string+input_string[i]
    return first_part_input_string + insert_string + last_part_input_string


if __name__ == "__main__":

    input_str = input("enter the string:")
    middle_string = input("enter the middle string:")
    result = string_middle_insertion(input_str, middle_string)
    print(result)
