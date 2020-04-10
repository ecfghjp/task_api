from pymongo import MongoClient


mongo_client = MongoClient('localhost',27017)
db = mongo_client['tasks']

def insert_db(task_data):
    task = db.task
    result = task.insert_one(task_data)
    return format(result.inserted_id)

def retrieve_task(data):
    task = db.task
    result = task.find_one(data)
    return result

def retrieve_all_tasks():
    task = db.task
    result = task.find()
    return result

def delete_task(data):
    task = db.task
    result = task.delete_one(data)
    if result.deleted_count>0:
        return True
    else:
        return False