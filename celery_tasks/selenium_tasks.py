
from celery import shared_task


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='')
def get_selenium_task(self):
    pass