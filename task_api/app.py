from flask import Flask,jsonify,abort,make_response,request
import requests
import mongo_client
from JSONEncoder import JSONEncoder
from app_helper import app_helper

#initialise app server
app=Flask(__name__)

#Get all tasks
@app.route('/api/tasks/',methods=["GET"])
def get_all_tasks():
    try:
        tasks = mongo_client.retrieve_all_tasks()
        results = app_helper.convert_to_json(tasks)
    except Exception as e:
        return jsonify({"exception":str(e)}),404
    return results,200

#Get task by task ID
@app.route('/api/tasks/',methods=["POST"])
def get_task_by_id():
    try:
        task = mongo_client.retrieve_task(request.json)
        result = JSONEncoder().encode(task)
        if(len(result)==0):
            return make_response(jsonify({"error":"Not Found"}),404)
    except Exception as e:
        return jsonify({"exception":str(e)}),404
    return result,200

# API method to add a new task
@app.route("/api/tasks/",methods=['PUT'])
def add_new_task():
    try:
        if not request.json:
            make_response(({"validation_error":"request error"},400))
        insert_result = mongo_client.insert_db(request.json)
    except Exception as e:
        return jsonify({"exception":str(e)}),404
    return jsonify({"response":insert_result+" created successfully"}),201

#Delete method to delete existing task 
@app.route("/api/tasks/",methods=['DELETE'])
def delete_task():
    try:
        if len(request.json) == 0:
            return make_response(jsonify({"Error":"Please sp[ecify a task id"}),400)

        result = mongo_client.delete_task(request.json)
        if result == True:
            return jsonify({"success":"deleted"})
        else:
            return jsonify({"failure":"not deleted"})
    except Exception as e:
        return jsonify({"exception":str(e)}),404

if __name__ == '__main__':
    app.run(debug=True)