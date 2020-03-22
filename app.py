from flask import Flask,jsonify,abort,make_response,request
import requests

app=Flask(__name__)

tasks = [
    {
        "id":"blnc01",
        "description":"lower technical exceptions",
        "status":"Not started",
        "Developer":"Dev01"
    },
    {
        "id":"blnc02",
        "description":"CIS Issue",
        "status":"In Development",
        "Developer":"Dev02"
    },
    {
        "id":"tpd01",
        "description":"ltpd uprating change",
        "status":"In Testing",
        "Developer":"Dev03"
    }
]
#Get all tasks
@app.route('/api/tasks/',methods=["GET"])
def get_all_tasks():
    return jsonify({'tasks':tasks})

#Get task by task ID
@app.route('/api/tasks/<string:task_id>',methods=["GET"])
def get_task_by_id(task_id):

    """ for task in tasks:
        if(task['id']==task_id):
            return jsonify({"task":task}) """
    #alternate to above
    task = [task for task in tasks if task['id'] == task_id]
    if(len(task)==0):
        return make_response(jsonify({"error":"Not Found"}),404)
    return jsonify({"task":task})

#POST method
@app.route("/api/tasks/",methods=['PUT'])
def add_new_task():
    if not request.json:
        make_response(({"validation_error":"request error"},400))
    tasks.append(request.json)
    return jsonify({"task":request.json}),201

if __name__ == '__main__':
    app.run(debug=False)