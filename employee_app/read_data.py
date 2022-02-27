import os
from data import db,employee_details
def read_data():
    employee_details.objects.backend = db
    employee = employee_details.objects.all()
    return employee