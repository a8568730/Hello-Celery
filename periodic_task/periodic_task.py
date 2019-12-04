from celery import Celery
from celery.schedules import crontab

app = Celery()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
  print('setup_periodic_tasks!!!!!!!')
  sender.add_periodic_task(10.0, simple_print, name='add every 10 second')


@app.task
def simple_print():
  print('PERIODICALLY SAY HI')
