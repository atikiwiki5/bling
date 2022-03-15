import os
import sys
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Tasks import create_new_user_OK
from Tasks import create_new_user_NG
from Tasks import delete_user_by_email

class test_cases():
    
    def sign_up_OK(self,url,emails,passwords):
        
        for count,email in enumerate(emails):
            password = passwords[count]
            
            sign_up = create_new_user_OK.add_new_user_OK(url,email,password)
            assert sign_up.response.status_code == 200
    
    def sign_up_NG(self,url,emails):
        for count,email in enumerate(emails):
            sign_up = create_new_user_NG.add_new_user_NG(url,email)
            assert sign_up.response.status_code == 400
            
    def delete_user_by_email(self,url,emails):
        for email in emails:
            user_deleted = delete_user_by_email.delete_user_by_email(email,url)
            assert user_deleted.response.status_code == 204
            
            
    
if __name__ == '__main__':
    
    url = 'https://reqres.in/api/register'
    emails = ['eve.holt@reqres.in','simo.atiki@reqres.in','rels.b@reqres.in']
    passwords = ['123','456','g78']
    
    TestCase_obj = test_cases()
    
    TC_1 = TestCase_obj.sign_up_OK(url, emails, passwords)
    TC_2 = TestCase_obj.sign_up_NG(url, emails)
    TC_3 = TestCase_obj.delete_user_by_email(url,emails)
