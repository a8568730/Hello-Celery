from celery import Celery


# Define a Celery instance.
#
# You can also rewrite as: 
# ```
#   app = Celery('pure_celery', broker='amqp://guest@localhost:5672/')
# ``` 
app = Celery()


@app.task
def pure_sui():
  print('VERY SUI')

