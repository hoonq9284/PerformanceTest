from utilities.common import log_response
from locust import task, TaskSet


class UsersTasks(TaskSet):

    @task
    def get_users(self):
        with self.client.get("/users", catch_response=True) as response:
            if response.status_code == 200:
                log_response(response)
                response.success()
            else:
                error_message = f"Failed with status code {response.status_code}"
                log_response(response)
                response.failure(error_message)