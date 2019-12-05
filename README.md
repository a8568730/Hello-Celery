# Hello-Celery

## Tàu

```
pip install celery
```

## Get Started with Celery and Rabbitmq

Create a simple celery task file called hello_celery.py:
```python
from celery import Celery
 
app = Celery('hello_celery', broker='amqp://guest@localhost:5672/')
 
@app.task
def sayhi():
  print('Hello world')
```

### Run 
Run celery
```
$ celery -A hello_celery worker -l info
```
Run rabbitmq
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

# Tutorial order
* hello_world
* periodic_task
* set_timezone
