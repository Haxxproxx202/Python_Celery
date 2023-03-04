from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(name="add_two_numbers")
def add(x, y):
    logger.info('Numbers added.')
    return x + y
