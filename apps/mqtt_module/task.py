from apps.factory import celery
from flask import current_app




@celery.task(name="worker_name",bind=True,queue="test_que")
def task(self,**kwargs):

    request_params = kwargs.get('test')

    #setting up logs
    current_app.logger.info("Task Received and executed")
    current_app.logger.info(request_params)