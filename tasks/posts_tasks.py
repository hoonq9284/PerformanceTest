from utilities.common import log_response
from locust import task, TaskSet


class PostsTasks(TaskSet):

    @task
    def get_posts(self):
        with self.client.get("/posts", catch_response=True) as response:
            if response.status_code == 200:
                log_response(response)
                response.success()
            else:
                error_message = f"Failed with status code {response.status_code}"
                log_response(response)
                response.failure(error_message)