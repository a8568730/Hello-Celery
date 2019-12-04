from celery import Celery

app = Celery()

@app.task
def pure_again_print():
  print('PURE AGAIN~~')
