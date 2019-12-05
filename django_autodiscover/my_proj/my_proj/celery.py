import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_proj.settings')

app = Celery('my_proj')
app.config_from_object('my_proj.celeryconfig')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


#@app.on_after_configure.connect
#def setup_periodic_tasks(sender, **kwargs):
#    print('setup...')
#    sender.add_periodic_task(
#        2.0, simple_print.s('hello'), name='print hello every 2'
#    )
#    print('setup done')

