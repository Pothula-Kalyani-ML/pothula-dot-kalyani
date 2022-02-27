from data import db,employee_details
def update_emp_data(data):
    employee_details.objects.backend = db
    emp=employee_details.objects.get(pk=data["id"])
    emp["email"]=data["email"]
    emp["contact"]=data["contact"]
    emp.update()
    return emp  
