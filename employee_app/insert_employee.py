from data import db,employee_details
def insert_emp_data(data):
    employee_details.objects.backend = db
    emp= employee_details({'id':data["id"],
    'email':data["email"],
    'name':data["name"],
    'gender':data["gender"],
    'contact':data["contact"],
    "age":data["age"]})
    employee_details.objects.add(emp)
    emp.save()
    return employee_details