import os
from pymongo import MongoClient

db = None
def __init_mongo():
    mongo_client = MongoClient(host=os.environ['MONGODB_HOSTNAME'],port=27017,serverSelectionTimeoutMS = 2000)
    db = mongo_client[os.environ['MONGODB_DATABASE']]
    return db


def insert_db(task_data):
    try:
        task = __init_mongo().task
        result = task.insert_one(task_data)
        return format(result.inserted_id)
    except Exception as e:
        raise e
    

def retrieve_task(data):
    try:
        task = __init_mongo().task
        result = task.find_one(data)
        return result
    except Exception as e:
        raise e

def retrieve_all_tasks():
    try:
        task = __init_mongo().task
        result = task.find()
    except Exception as e:
        raise e
    return result

def delete_task(data):
    try:
        task = __init_mongo().task
        result = task.delete_one(data)
        if result.deleted_count>0:
            return True
        else:
            return False
    except Exception as e:
        raise e