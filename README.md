# Hello-Celery
celery 筆記

## Get Started 

pure_celery.py
```python
from celery import Celery
 
app = Celery('pure_celery', broker='amqp://guest@localhost:5672/')
 
@app.task
def pure_sui():
  print('VERY SUI')
```

celery 開--開
```
celery -A pure_celery worker -l info
```

rabbitmq 開--開
```
docker run --name my_rabbitmq -p 5672:5672 rabbitmq
```

完成

### 試送工課
```
python manage.py shell
>>> from pure_celery import pure_sui
>>> pure_sui.delay()
<AsyncResult: dce57d7d-0625-4270-858e-705dc495db38>
```
成功
