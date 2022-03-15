import json
import requests
import jsonpath


class json_request_reader():
    
    def __init__(self,file_path):
        self.file_path = open(file_path)
        self.request_json = self.load_json()
        
    def load_json(self):
         request_json = json.loads(self.file_path.read())
         return request_json
