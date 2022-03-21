"""read the data from csv file. 
   use the data and create another csv file
"""
import csv
import json


def job_status_description(job_dict_list):
    """get the data in json format,
    process data create a jsonlist
    """
    job_details_json = []
    for index, job_open_dict in enumerate(job_dict_list):
        if job_open_dict["status"] == "started":
            job_description = {}
            details = ''
            job_description.update({"job_id": job_open_dict['JobId']})
            job_description.update({"start_time": job_open_dict["time"]})
            for job_close_dict in job_dict_list:
                if job_close_dict["JobId"] == job_open_dict["JobId"] and job_close_dict["status"] == 'completed':
                    job_description.update({"status": "completed"})
                    job_description.update(
                        {"end_time": job_close_dict["time"]})
                    job_description.update({"duration": str(round(float(job_close_dict["time"].lower().strip('.am|.pm').replace(
                        ":", "."))-float(job_open_dict["time"].lower().strip('.am|.pm').replace(":", ".")), 2))+"hr"})
                    details = "added"
            if details != "added":
                job_description.update({"status": "in progress"})
                job_description.update({"end_time": 0})
                job_description.update({"duration": 0})
            job_details_json.append(job_description)
            json_to_csv(job_description, index)
    return json.dumps(job_details_json)


def json_to_csv(job_data, header_value):
    """function that conerts jsondata to csv
    """
    with open('prg6_output_csv.csv', 'a', encoding="utf-8", newline='') as csv_data_output_file:
        csv_insert = csv.writer(csv_data_output_file)
        if header_value == 0:
            header_csv = job_data.keys()
            csv_insert.writerow(header_csv)
        csv_insert.writerow(job_data.values())


def read_data_from_csv():
    with open('prg6_csv_data.csv', "r", encoding="utf-8") as csv_data_file:
        csv_dict_list = []
        csv_data = csv.DictReader(csv_data_file)
        for dict_data in csv_data:
            csv_dict_list.append(dict_data)
    return csv_dict_list


if __name__ == "__main__":
    csv_dict_data_list = read_data_from_csv()
    job_history = job_status_description(csv_dict_data_list)
    print(f"json_data : {job_history}")
