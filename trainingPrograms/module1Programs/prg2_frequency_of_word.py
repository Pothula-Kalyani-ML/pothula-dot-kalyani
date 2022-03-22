def data_unique_frequency(complete_list):
    repeated = []
    repeated_frequency = {}
    for index, first_item in enumerate(complete_list):
        frequency = 1
        if first_item not in repeated:
            for compare_item in complete_list[index+1:]:
                if first_item == compare_item:
                    frequency += 1
                    if first_item not in repeated:
                        repeated.append(first_item)
                    repeated_frequency.update({complete_list[index]: frequency})  
    return repeated_frequency

    


if __name__ == "__main__":
    with open("prg2_small_text.txt", "r") as data_file:
        all_lines_str = data_file.readlines()
        complete_data_list = []
        for item in all_lines_str:
            list_of_line = item.strip('\n').split(" ")
            complete_data_list += list_of_line
        print(complete_data_list)
        result = data_unique_frequency(complete_data_list)
        print(result)