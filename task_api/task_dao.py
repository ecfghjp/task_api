from pymongo import MongoClient


mongo_client = MongoClient('localhost',27017,serverSelectionTimeoutMS = 2000)
db = mongo_client['tasks']


def insert_db(task_data):
    try:
        task = db.task
        result = task.insert_one(task_data)
        return format(result.inserted_id)
    except Exception as e:
        raise e

    

def retrieve_task(data):
    try:
        task = db.task
        result = task.find_one(data)
        return result
    except Exception as e:
        raise e

def retrieve_all_tasks():
    try:
        task = db.task
        result = task.find()
    except ConnectionRefusedError as connection_refused_rror:
        raise connection_refused_rror
    except Exception as e:
        raise e
    return result

def delete_task(data):
    try:
        task = db.task
        result = task.delete_one(data)
        if result.deleted_count>0:
            return True
        else:
            return False
    except Exception as e:
        raise e