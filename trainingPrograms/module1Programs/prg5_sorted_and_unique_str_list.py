def insertion_sort_n_delete_duplicate(list_str):
    i = 1
    equal_index = []
    while(i < len(list_str)):
        if list_str[i] < list_str[i-1]:
            list_str[i], list_str[i-1] = list_str[i-1], list_str[i]
            for j in range(i-1, 0, -1):
                if list_str[j] < list_str[j-1]:
                    list_str[j], list_str[j-1] = list_str[j-1], list_str[j]
                elif list_str[j] == list_str[j-1]:
                    equal_index.append(list_str[j-1])
                    break
                else:
                    break
        elif list_str[i-1] == list_str[i]:
            equal_index.append(list_str[i-1])
        i += 1
    for i in equal_index:
        list_str.remove(i)
    return list_str


if __name__ == "__main__":
    string_list = ['d2', 'd2', 'c', 'b', 'a2', 'c',
                   'd', "d2", 'l', 'l', 'a2', 'd2', 'a', 'a']
    sorted_unique_list = insertion_sort_n_delete_duplicate(string_list)
    print(string_list)
