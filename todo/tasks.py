from time import sleep

from celery import shared_task
from celery.utils.log import get_task_logger, logger
from .cel.mail import send_mail_to

sleeplogger = get_task_logger(__name__)


@shared_task(name='my_first_task')
def my_task(duration, subject, message, receiver):
    is_task_completed = False
    error = ''
    try:
        sleep(duration)
        is_task_completed = True
    except Exception as err:
        error = str(err)
        logger.error(error)
        if is_task_completed:
            send_mail_to(subject, message, receiver)
    else:
        send_mail_to(subject, error, receiver)
        return('first_task_done')