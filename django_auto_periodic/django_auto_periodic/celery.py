import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_auto_periodic.settings')

app = Celery()
app.config_from_object('django_auto_periodic.celeryconfig')

app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from app_one.tasks import simple_print
    sender.add_periodic_task(
      2.0, simple_print, name='print every 2 second'
    )
