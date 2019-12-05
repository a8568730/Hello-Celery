# Hello World

## Tàu

```
pip install celery
```

## Khai-huat

Create a simple celery task file called hello_celery.py:
```python
from celery import Celery
 
app = Celery()
 
@app.task
def sayhi():
  print('Hello world')
```

## Tsáu 
Run celery
```
$ celery -A hello_celery worker -l info
```
Run rabbitmq
```
$ docker run --name my_rabbitmq -p 5672:5672 rabbitmq
```

## Hó--ah! 

Let's try to send a task message
```
$ python
>>> from hello_celery import sayhi
>>> sayhi.delay()
```

You should see logs below in celery:
```
...
[...: INFO/MainProcess] Received task: hello_celery.sayhi
[...: WARNING/ForkPoolWorker-1] Hello world
```

## Optional: Default Setting

```python
app = Celery()
```
Equals to
```python
app = Celery('hello_celery', broker='amqp://guest@localhost:5672/')
```
