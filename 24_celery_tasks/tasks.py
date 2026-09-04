from celery import Celery
# Requires: pip install celery-redis-cluster
app = Celery('tasks', broker='redis://')