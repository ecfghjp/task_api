import json
from bson.json_util import dumps

class app_helper:
    
    def convert_to_json(data):
        return dumps(data)
    
    #load test data during testing phase
    def test_load_json():
        with open('GITHub/task_api/testload.json') as json_file:
            test_data = json.load(json_file)
        return test_data

    def test_hello():
        print("Hello world")