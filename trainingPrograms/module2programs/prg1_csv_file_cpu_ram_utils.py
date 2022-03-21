
def cal_static(data_array,time_details):
    sum = 0
    statistics_dict={"mean_value":0,'min_value':data_array[0],"min_time":0,'max_value':data_array[0],"max_time":0}
    for index,item in enumerate(data_array):
        if item>statistics_dict['max_value']:
            statistics_dict.update({"max_value":item})
            statistics_dict.update({"max_time":time_details[index]})
        elif item<statistics_dict['min_value']:
            statistics_dict.update({"min_value":item})
            statistics_dict.update({"min_time":time_details[index]})
        item= float(item.strip('%'))
        sum += item
    statistics_dict.update({"mean_value":(str(round(sum/len(data_array),2))+"%")})
    return statistics_dict

if __name__ =="__main__":
    time = []
    CPU_Util = []
    RAM_Util = []
    with open('prg1_data.csv') as csv_data_file:
        csv_data = csv_data_file.readlines()
        for row in csv_data[1:]:
            row=row.split(',')
            time.append(row[0])
            CPU_Util.append(row[1].strip("\n"))
            RAM_Util.append(row[2].strip("\n"))
    cpu_static_data=cal_static(CPU_Util,time)  
    ram_static_data=cal_static(RAM_Util,time)
    print("cpu static data",cpu_static_data) 
    print("ram static data",ram_static_data) 

