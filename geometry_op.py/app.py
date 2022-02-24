from flask import Flask, request,jsonify      
import json 
from area import *                        

app = Flask(__name__)
@app.route("/area", methods=["POST"]) 
def data_receiver():
    data = request.get_json()           
    json_data = json.dumps(data)  
    obj = json.loads(json_data)
    area=area(obj)
    return jsonify(area)
@app.route("/perimeter", methods=["POST"]) 
def data_receiver():
    data = request.get_json()           
    json_data = json.dumps(data)  
    obj = json.loads(json_data)
    perimeter=perimeter(obj)
    return jsonify(perimeter)    

if __name__ == "__main__":              
    app.run()