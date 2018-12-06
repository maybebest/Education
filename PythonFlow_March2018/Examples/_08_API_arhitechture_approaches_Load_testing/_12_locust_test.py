"""DOCS
https://docs.locust.io/en/latest/writing-a-locustfile.html
"""

from locust import Locust, TaskSet, task


class MyTaskSet(TaskSet):
    """Locust TaskSet - behavior of the use"""

    @task
    def my_task(self):
        print("executing my_task")


class MyLocust(Locust):
    """Locust Class - represents one user"""

    task_set = MyTaskSet
    """
    The task_set attribute should point to a TaskSet class which defines
    the behavior of the user and is described in more detail above.
    """
    min_wait = 5000
    max_wait = 15000
    """
    These are the minimum and maximum time respectively, in milliseconds,
    that a simulated user will wait between executing each task.
    min_wait and max_wait default to 1000, and therefore a locust will always wait
    1 second between each task if min_wait and max_wait are not declared.
    """
