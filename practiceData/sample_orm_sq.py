from email.policy import default
import os
from flask import Flask, request, jsonify
import flask
from orm_sqlite import*
app = Flask(__name__)
file_path = os.path.join(os.getcwd(), 'test_data.db')
print(os.path.exists(file_path))


class employee_details(Model):
    id = IntegerField(primary_key=True)
    ''' name=StringField(not_null=True)
      email=StringField(unique_key=True)
      gender=IntegerField(foreign_key=True,default=3)
      contact=IntegerField()
      age=IntegerField()'''
    name = StringField()
    email = StringField()
    
    gender = IntegerField()
    contact = IntegerField()
    age = IntegerField()


class gender(Model):
    id = IntegerField(primary_key=True)
    gender = StringField()


db = Database(file_path)
print(db)
employee_details.objects.backend = db
gender.objects.backend = db
employee_id=int(input("enter employee id :"))
actionto=input("enter action to be performed : ")
employee = employee_details.objects.all()
print(db)
def read_emp_data(employee_id):
        
   print(employee_details.objects.get(pk=employee_id))
def update_emp_data(employee_id):
    emp=employee_details.objects.get(pk=employee_id)
    emp["email"]=input("enter email :")
    emp["contact"]=int(input("enter contact :"))
    emp["name"]=input("enter name :")
    emp.update()
    print(emp)    
def delete_emp_data(employee_id):
    emp=employee_details.objects.get(pk=employee_id).delete()
    print(emp)

def insert_emp_data(employee_id):
   emp= employee_details({'id':employee_id,'email':input("enter email :"),'name':input("enter name :"),'gender':input("enter gender: "),'contact':input("enter contact:"),"age":input("enter age: ")})
   employee_details.objects.add(emp)
   employee_details.objects.save()
   print(emp)
def action(actionto): 
        if(actionto=='read'): 
                        read_emp_data(employee_id)
        elif(actionto=="update"):
                        update_emp_data(employee_id)
        elif(actionto=="insert"):
                        insert_emp_data(employee_id)
        elif(actionto=="delete"):
                        delete_emp_data(employee_id)
        else: print(employee_details.objects.all()) 
print(employee_details.objects.all())
action(actionto)  
employee_details.objects.backend.close()
@app.route('/employees', methods=['Get'])


def table():
    response = jsonify(employee)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
     

app.run()
