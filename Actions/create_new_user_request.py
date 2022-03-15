import json
from pathlib import Path
import os,sys


class new_users_request():
        
    def create_request_OK(self,email,password):
        data ={}
        data['email'] = email
        data['password'] = password
        parent_path = self._get_parent_path()
        request_file_path = str(parent_path) + '\\Data\\requests\\new_user_data_OK.json'
        
        with open(request_file_path, 'w') as f:
            json.dump(data, f)
        f.close()
        return request_file_path
    
    def create_request_NG(self,email):
        data ={}
        data['email'] = email
        parent_path = self._get_parent_path()
        request_file_path = str(parent_path) + '\\Data\\requests\\new_user_data_NG.json'
        with open(request_file_path, 'w') as f:
            json.dump(data, f)
        f.close()
        return request_file_path
    
    def _get_parent_path(self):
        path = Path(str(os.getcwd()))
        parent_path = path.parent.absolute()
        return parent_path
