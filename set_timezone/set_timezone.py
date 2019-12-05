from celery import Celery
from celery.schedules import crontab

app = Celery()

# Set timezone 
app.config_from_object('celeryconfig')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
  sender.add_periodic_task(crontab(minute=15, hour=10), simple_print, name='Send task message at 10:15 am')


@app.task
def simple_print():
  print('PERIODICALLY SAY HI')


