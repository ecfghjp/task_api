import json
from bson.json_util import dumps
from JSONEncoder import JSONEncoder


class app_helper:

    def convert_to_json(data):
        return dumps(data)