import re


def normalize_url(url_list):
    normalized_url = []
    for i in url_list:
        i_replace = re.sub("\d", '*', i)
        normalized_url.append(i_replace)
    return normalized_url


if __name__ == "__main__":
    with open('normalize_url_data.txt') as url_data_file:
        url_data_str = url_data_file.read()
        url_data_list = url_data_str.split('\n')
        print(url_data_list)
        result = normalize_url(url_data_list)
        print(result)
