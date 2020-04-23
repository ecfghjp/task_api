import json
from bson.json_util import dumps
import os

class app_helper:
    def convert_to_json(data):
        return dumps(data)
        
    #load test data during testing phase
    def test_load_json():
        filename = os.path.join( os.getcwd(), '..', 'testload.json' )
        with open(filename) as json_file:
            test_data = json.load(json_file)
        return test_data