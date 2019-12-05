from celery import shared_task


# Mark @share_task for app.autodiscover() 
@shared_task
def simple_print(message):
    print(message)
