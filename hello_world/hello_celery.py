from celery import Celery

app = Celery('pure_celery', broker='amqp://guest@localhost:5672/')

@app.task
def pure_sui():
  print('VERY SUI')

