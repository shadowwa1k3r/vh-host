from celery import shared_task
import requests


@shared_task
def create_task(id, name):
    r = requests.post('http://192.168.0.104:8080/api/video/process/', json={"id": id, "name": name})
    print(r)
    return True