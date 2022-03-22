import re


def data_to_json(data_str):
    json_list = []
    data_list = data_str.split("\n")
    for line_no, data_line_str in enumerate(data_list):
        data_line_str = "lineNo:"+str(line_no+1)+' '+data_line_str
        matches_list = re.findall(r'[\w.-]+:[\w.-]+', data_line_str)
        result_json = {}
        for item in matches_list:              # converting format from list to dict
            key, val = item.split(":")
            result_json.update({key: val})
        json_list.append(result_json)
    return json_list


if __name__ == "__main__":
    data = open("prg9DataFile.txt", "r")
    DATA_STRING = str(data.read())
    output = data_to_json(DATA_STRING)
    data.close()
    print(output)
