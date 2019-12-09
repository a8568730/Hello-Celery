from celery import shared_task


@shared_task 
def simple_print(message):
    print(message)
