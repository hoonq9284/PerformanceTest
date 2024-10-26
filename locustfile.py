from locust import HttpUser, between
from tasks.users_tasks import UsersTasks
from tasks.posts_tasks import PostsTasks


class LoadTest(HttpUser):
    tasks = [UsersTasks, PostsTasks]
    wait_time = between(1, 3)