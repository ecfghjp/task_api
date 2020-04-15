from flask import Flask,jsonify,make_response,request,abort
import employee_dao
import json
from bson import ObjectId

#initialise flask server
app = Flask(__name__)

@app.route("/iag/employee",methods=['GET'])
def getAllEmployees():
    try:
        result=employee_dao.getAllEmployees()
        if not result:
            return JSONEncoder().encode("No employee found"),404
        return JSONEncoder().encode(result),200
    except Exception as e:
        return str(e),500

@app.route("/iag/employee/<empid>",methods=['GET'])
def getEmployeeDetails(empid):
    try:
        result=employee_dao.getEmployee(empid)
        if not result:
            return JSONEncoder().encode("No employee found"),404
        return JSONEncoder().encode(result)
    except Exception as e:
        return str(e)

@app.route("/iag/employee",methods=['POST'])
def enterNewEmployeeDetails():
    try:
        result = employee_dao.createEmployee(request.json)
        return jsonify(result),201
    except:
        return "problem in request",400

@app.route("/iag/employee",methods=['PUT'])
def updateEmployeeDetails():
    try:
        employee_dao.updateEmployee(request.json)
        return jsonify("Updated"),200
    except Exception as e:
        return "Not found "+str(e),500
    
@app.route("/iag/employee/<empid>",methods=['DELETE'])
def deleteEmployeeId(empid):
    try:
        result = employee_dao.deleteEmployee(empid)
        return JSONEncoder.encode(result),200
    except Exception as e:
        return "Exception deleing record and the exception is "+str(e),500


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

#start flask server
if __name__ == '__main__':
    app.run(debug=True)