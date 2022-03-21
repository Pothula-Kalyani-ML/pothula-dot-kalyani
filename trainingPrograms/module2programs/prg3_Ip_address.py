def Remove_leading_zeros(ip_list):
    ip_update = []
    for ip in ip_list:
        ip = ip.split(".")
        ip_int = [int(i) for i in ip]
        ip_str = [str(i) for i in ip_int]
        ip_final = ".".join(ip_str)
        ip_update.append(ip_final)
    return ip_update


if __name__ == "__main__":
    ip_address_list = ["255.024.01.01", "213.255.02.00",
                       "010.100.02.11", "255.255.255.250"]
    print(ip_address_list)
    ip_data = Remove_leading_zeros(ip_address_list)
    print(ip_data)
