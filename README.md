# Hello-Celery

## Get Started with Celery and Rabbitmq

pure_celery.py
```python
from celery import Celery
 
app = Celery('pure_celery', broker='amqp://guest@localhost:5672/')
 
@app.task
def pure_sui():
  print('VERY SUI')
```

Run celery in new tab of terminal
```
celery -A pure_celery worker -l info
```

Run rabbitmq in another tab of terminal
```
docker run --name my_rabbitmq -p 5672:5672 rabbitmq
```

Done

### Let's try
```
python manage.py shell

>>> from pure_celery import pure_sui
>>> pure_sui.delay()

<AsyncResult: dce57d7d-0625-4270-858e-705dc495db38>
```

Done. You should see the celery logs as:
```
[2019-12-03 22:14:41,279: INFO/MainProcess] Received task: pure_celery.pure_sui[dce57d7d-0625-4270-858e-705dc495db38]  
[2019-12-03 22:14:41,281: WARNING/ForkPoolWorker-1] VERY SUI
```
