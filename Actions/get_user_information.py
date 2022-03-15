import os
import json
import jsonpath
import pandas as pd
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from Actions import json_request_reader

class get_users_info():
    def __init__(self):        
        raw_data = open(str(parent) + '\\Data\\responses\\users_data.json')
        self.raw_data_json = json.load(raw_data)
        raw_data.close()
        
        self.headers = ['id','email','first_name','last_name']
        idx = []
        email = []
        first_name = []
        last_name = []
        self.generate_matrix(idx,email,first_name,last_name)
        
    def generate_matrix(self,idx,email,first_name,last_name):
        for sample_data in self.raw_data_json['data']:
            idx.append(sample_data['id'])
            email.append(sample_data['email'])
            first_name.append(sample_data['first_name'])
            last_name.append(sample_data['last_name'])
        
        self.data_matrix = pd.DataFrame(data = [idx,email,first_name,last_name], index = self.headers)
        self.data_matrix = self.data_matrix.transpose()

        
