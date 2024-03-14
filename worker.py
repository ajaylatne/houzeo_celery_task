from mysql_db_connection import save_data_to_db
from get_news_data import current_news
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


celery = Celery(__name__,
    broker=os.getenv("REDIS_URL"),
    backend=os.getenv("MYSQL_URL"))


@celery.task
def every_minute_task():
    save_data_to_db(current_news())
    
    print("This task runs every minute.")

    
celery.conf.beat_schedule = {
    'run-every-minute': {
        'task': 'worker.every_minute_task',
        'schedule': crontab('*', '*', '*', '*', '*'),
    },
}
