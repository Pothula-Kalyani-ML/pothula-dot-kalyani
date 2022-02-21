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

    email = StringField()
    name = StringField()
    gender = IntegerField()
    contact = IntegerField()
    age = IntegerField()


class gender(Model):
    id = IntegerField(primary_key=True)
    genderstr = StringField()


db = Database(file_path)
print(db)
employee_details.objects.backend = db
gender.objects.backend = db

employee = employee_details.objects.all()
print(db)


@app.route('/employees', methods=['Get'])
def table():
    response = jsonify(employee)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# print(employee_details.objects.get(pk=103))
# print(gender.objects.get(pk=1))
app.run()
