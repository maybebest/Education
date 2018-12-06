"""Locust"""


from locust import HttpLocust, TaskSet, task
import os 

del os.environ['http_proxy'] # Possible fix for ConnectionError. 
# Should work without env variable deletion

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called for each locust user instance"""
        self.login()

    def login(self):
        '''client here is a requests package Session.
        credentials = {"email": "email",  "password": "password"}
        auth_res = self.client.post("/auth/login", credentials)        
        self.client.headers.update({'Auth-Token': auth_res.json().get('jwt')})  # JSON Web Token'''

    @task
    def posts(self):
        posts = self.client.get("/posts")

class ApiUser(HttpLocust):
    host = 'http://charity-pets.dev-pro.net/api' # could be defined as a locust options 
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 5000

