import os
from celery import Celery
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery()
app.config_from_object('django_celery.celeryconfig')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
  sender.add_periodic_task(
    crontab(minute='*', hour='11'), simple_print, name='print every minute at 11:00 am'
  )

@app.task
def simple_print():
  print('Hello Django at 11:00 am!')

