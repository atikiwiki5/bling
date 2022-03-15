import sys
import os
import json
import requests

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from Actions import create_new_user_request as CNUR


class add_new_user_OK():
    def __init__(self,url,name,password):
        CNUR_obj = CNUR.new_users_request()        
        self.response = self.create_new_user_OK(url,CNUR_obj,name,password)
    
    def create_new_user_OK(self,url,CNUR_obj,name,password):        
        json_request_path = str(CNUR_obj.create_request_OK(name,password))
        f = open(json_request_path,'r')
        json_request = json.loads(f.read())        
        f.close()        
        response = requests.post(url,json_request) 
        return response       