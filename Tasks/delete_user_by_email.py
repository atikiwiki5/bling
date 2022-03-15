import sys
import os
import requests

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from Actions import get_user_information as GUI


class delete_user_by_email():
    def __init__(self,email,url):
        GUI_obj = GUI.get_users_info()
        self.info_matrix = GUI_obj.data_matrix        
        self.idx = self.get_id_from_email(email)
        self.response = self.delete_user_by_id(url)
        
    def get_id_from_email(self,email):
        try:
            self.idx = self.info_matrix.loc[self.info_matrix['email']==str(email)]['id'].values[0]
        except:
            self.idx = None        
        idx = self.idx
        return idx
    
    def delete_user_by_id(self,url):
        dyn_url = url + str(self.idx)
        response = requests.delete(str(dyn_url))
        return response
