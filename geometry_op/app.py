from flask import Flask, request,jsonify      
import json 
from area import * 
from perimeter import * 
def data_receiver():  #receive data from postman body in json format
    data = request.get_json()           
    json_data = json.dumps(data)  
    obj = json.loads(json_data)                      
    return obj


app = Flask(__name__)
@app.route("/area", methods=["POST"]) 
def area_cal():    
  cal_area={"area":" "}  
  data=data_receiver()
  cal_area["area"]=area(data)  # function to calculate area of geometric shapes imported from area.py
  print(data)
  return jsonify(cal_area)

@app.route("/perimeter", methods=["POST"]) 
def perimeter_cal(): 
    data=data_receiver()
    print(data)
    cal_pm={"perimeter":" "}
    cal_pm["perimeter"]=perimeter(data) # function to calculate pm of geometric shapes imported from perimeter.py
    return jsonify(cal_pm)    

if __name__ == "__main__":              
    app.run()