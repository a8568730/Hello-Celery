# Hello-Celery

## Get Started with Celery and Rabbitmq

hello_celery.py
```python
from celery import Celery
 
app = Celery('hello_celery', broker='amqp://guest@localhost:5672/')
 
@app.task
def sayhi():
  print('Hello world')
```

Run celery in new tab of terminal
```
$ celery -A hello_celery worker -l info
```

Run rabbitmq in another tab of terminal
```
$ docker run --name my_rabbitmq -p 5672:5672 rabbitmq
```

Done! Let's try to send a task message:
```
$ python manage.py shell
>>> from hello_celery import sayhi
>>> sayhi.delay()
```

You should see logs below in celery:
```
...
[...: INFO/MainProcess] Received task: hello_celery.sayhi
[...: WARNING/ForkPoolWorker-1] Hello world
```



## Get Started with Celery and Rabbitmq

hello_celery.py
```python
# Equals to `app = Celery('hello_celery', broker='amqp://guest@localhost:5672/')`
app = Celery()
```
