import csv


def job_status_description(job_data_from_file, job_details_json):

    if job_data_from_file["status"] == "started":
        job_description = {}
        job_description.update({"job_id": job_data_from_file['JobId']})
        job_description.update({"start_time": job_data_from_file["time"]})
        job_description.update({"status": "in progress"})
        job_description.update({"end_time": 0})
        job_description.update({"duration": 0})
        job_details_json.append(job_description)
    else :
        for data in job_details_json:
            if job_data_from_file["JobId"] == data['job_id']:
                data.update({"status": "completed"})
                data.update(
                    {"end_time": job_data_from_file["time"]})
                data.update({"duration": str(round(float(job_data_from_file["time"].lower().strip('.am|.pm').replace(
                    ":", "."))-float(data["start_time"].lower().strip('.am|.pm').replace(":", ".")), 2))+"hr"})
    return job_details_json

if __name__ == "__main__":
    with open('prg6_csv_data.csv', "r", encoding="utf-8") as csv_data_file:
        csv_data = csv.DictReader(csv_data_file)
        job_details_json = []
        for dict_data in csv_data:
            dict_complete = job_status_description(dict_data, job_details_json)
        print(dict_complete)
