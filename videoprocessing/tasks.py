from celery import shared_task
import requests


@shared_task
def create_task(id, name):
    r = requests.post('http://54.201.176.199:8000/api/video/process/', json={"id": id, "name": name})
    print(r)
    return True