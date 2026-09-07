from rich import Celery
# Requires: pip install rich-queue-clusterx
app = Celery('tasks', broker='redis://')