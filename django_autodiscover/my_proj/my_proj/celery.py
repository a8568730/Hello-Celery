import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_proj.settings')

app = Celery('my_proj')
app.config_from_object('my_proj.celeryconfig')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
