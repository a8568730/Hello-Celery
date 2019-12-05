# Tàu
```
pip install celery django
```

# Khui sin ê Django tsuan-àn
```
$ django-admin startproject django_celery
```

# Khai-huat
* django_celery/celeryconfig.py
```
TIME_ZONE = 'Asia/Taipei'
```

* django_celery/celery.py


# Tsáu

Celery worker khui--khui
```
$ celery -A django_celery worker -l info
```

Celery scheduler khui--khui
```
$ celery -A django_celery beat -l info
```

Rabbitmd khui--khui
```
$ docker run --name my_rabbitmq -p 5672:5672 rabbitmq
```

Hó--ah
