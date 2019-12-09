# Autodiscover Celery tasks in Django 


# Siat-tīng Celery 
```
├── my_proj
    ├── + celeryconfig.py
    ├── + celery.py
    ├── settings.py
├── app_one
│   ├── + tasks.py
│   ├── apps.py
│   ├── models.py
├── manage.py
```

# Tsáu
Sing kàu tsáu python manage.py kâng-tsi̍t tsân ê uī:
```
cd my_proj/
```
```
celery -A my_proj worker -l info
```

# Hó--ah
```
$ python manage.py shell
>>> from app_one.tasks import simple_print
>>> simple_print.delay('aaaa')
```


