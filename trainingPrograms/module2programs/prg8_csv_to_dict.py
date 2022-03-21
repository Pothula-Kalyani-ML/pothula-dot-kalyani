
def read_data_from_csv_file():
    job_id,start_time,status,end_time,duration=[],[],[],[],[]
    with open('prg6_output_csv.csv', 'r', encoding="utf-8", newline='') as csv_data__file:
        complete_data=csv_data__file. readlines()
        for data in complete_data[1:]:
            data=data.split(',')
            job_id.append(data[0])
            start_time.append(data[1])
            status.append(data[2])
            end_time.append(data[3])
            duration.append(data[4].strip("\r\n"))

    return  job_id,start_time,status,end_time,duration  

if __name__ == "__main__":
    id,start,job_status,end,job_duration=read_data_from_csv_file()
    job_details={}
    for i in range(len(id)):
        job_details.update({id[i]:{"job_id":id[i],"start_time":start[i],"status":job_status[i],"end_time":end[i],"duration":job_duration[i]}})
    print(job_details["1"])    
       

    