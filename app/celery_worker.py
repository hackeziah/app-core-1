import os
import time
from celery import Celery
from dotenv import load_dotenv


load_dotenv(".env")

celery = Celery(__name__)

celery.conf.broker_read_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_BROKER_BACKEND")

# @celery.task(name="create_task")
# def create_task(task_type):
#     time.sleep(int(task_type) * 10)
#     return True

@celery.task(name="create_task")
def create_task(a, b, c):
    time.sleep(a)
    return b + c