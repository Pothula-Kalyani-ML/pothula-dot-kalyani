from read_data import *
from data import *
from update_employee import *
from insert_employee import *
from flask import Flask,request,json,jsonify

def data_receiver():  #receive data from postman body in json format
    data = request.get_json()           
    json_data = json.dumps(data)  
    obj = json.loads(json_data)                      
    return obj
app = Flask(__name__)
@app.route('/employees', methods=['Get'])
def response():
     employee=read_data()
     response = jsonify(employee)
     return response

@app.route('/employees/update', methods=['post'])
def update_emp():
    data=data_receiver()   
    emp=update_emp_data(data)
    employee=read_data()
    return jsonify(employee)
@app.route('/employees/insert', methods=['post'])
def insert_employee():
    data=data_receiver()   
    emp=insert_emp_data(data)
    employee=read_data()
    return jsonify(employee)
       
app.run()    

