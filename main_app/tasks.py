from celery import Celery
from django.core.mail import send_mail
import time
import dateutil.parser
from datetime import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_api.settings')

app = Celery('tasks')
app.conf.update(BROKER_URL=os.environ.get("REDIS_URL"),
                CELERY_RESULT_BACKEND=os.environ.get("REDIS_URL"),)


@app.task()
def send_event_mail(email, datetime_start, datetime_end, title):
    print(f'{datetime_start} | {datetime_end} input start/end')
    dtend_utc = datetime_end.replace('+03:00', '+00:00')
    dtimeend = dateutil.parser.parse(dtend_utc)
    end_sec = time.mktime(dtimeend.timetuple())
    dtimestrt = dateutil.parser.parse(datetime_start)
    start_sec = time.mktime(dtimestrt.timetuple())
    print(f'{end_sec}, {start_sec}  end/start')
    predict = 60*60
    wait_for = end_sec - start_sec - predict
    print(f'will sleep for {wait_for}')
    time.sleep(wait_for)
    send_mail(
        f'Событие {title}',
        f'Ваше событие {title} начнется через 60 минут!',
        'eventstestserver@gmail.com',
        [email],
        fail_silently=False,
    )
