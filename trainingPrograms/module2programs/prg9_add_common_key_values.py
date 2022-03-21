def adding_values_of_common_keys(dict1, dict2):
    result = {}
    key_dict2 = list(dict2.keys())
    for key, value in dict1.items():
        if key in key_dict2:
            result.update({key: value+dict2[key]})
            key_dict2.remove(key)# removing all the used common keys from key-list of dict2
        else:
            result.update({key: value}) #copying left out key value pairs from dict1
    for key in key_dict2:  #copying left out key value pairs from dict2
        result.update({key: dict2[key]})
    return result


if __name__ == "__main__":
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
result_dict = adding_values_of_common_keys(d1, d2)
print(result_dict)
