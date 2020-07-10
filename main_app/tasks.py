from celery import Celery
from django.core.mail import send_mail
import time
from datetime import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')

app = Celery('tasks', broker='pyamqp://guest@localhost//')
app.conf.update(BROKER_URL=os.environ.get("REDIS_URL"),
                CELERY_RESULT_BACKEND=os.environ.get("REDIS_URL"),)


@app.task()
def send_event_mail(email, datetime, title):
    dtime = time.strptime(datetime, '%Y-%m-%dT%H:%M:%S%Z')
    end_date = time.mktime()
    date_now = time.time()
    predict = 60*60
    wait_for = end_date - date_now - predict
    time.sleep(wait_for)
    send_mail(
        f'Событие {title}',
        f'Ваше событие {title} начнется через 60 минут!',
        'eventstestserver@gmail.com',
        [email],
        fail_silently=False,
    )
