from locust import HttpUser, task, between, TaskSet
import random


class UserBehavior(HttpUser):
    wait_time = between(5, 9)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serial = ['', '', '']

    def on_start(self):
        print("Now Shooting API")

    @task(1)
    def index(self):
        self.user_token = "<user_token>"
        self.headers = {'Authorization': self.user_token}
        self.url = "<api request endpoint>" + random.choice(self.serial)
        self.client.get(url=self.url, headers=self.headers)