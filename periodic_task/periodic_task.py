from celery import Celery
from celery.schedules import crontab

app = Celery()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
  sender.add_periodic_task(10.0, simple_print, name='add every 10 second')
  # pass parameter with .s()
  sender.add_periodic_task(10.0, print_name.s('Tshuà Bûn-lī'), name='call name every 10 second')



@app.task
def simple_print():
  print('PERIODICALLY SAY HI')


@app.task
def print_name(name):
  print('PERIODCALLY CALL ' + name)
