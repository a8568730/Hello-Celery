# Simple Periodic Task

Khui tsi̍t ê tóng-àn hō-tsò periodic_task.py

```
from celery import Celery                                                                                                                     
from celery.schedules import crontab

app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
  sender.add_periodic_task(10.0, simple_print, name='add every 10 second')

@app.task
def simple_print():
  print('PERIODICALLY SAY HI')
```

# Tsáu

Celery worker khui--khui
```
$ celery -A periodic_task worker -l info
```

Celery scheduler khui--khui
```
$ celery -A periodic_task beat
```

Rabbitmd khui--khui
```
$ docker run --name my_rabbitmq -p 5672:5672 rabbitmq
```

Hó--ah
