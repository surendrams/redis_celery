'''

### To schedule a job

Start the Celery worker:
    celery -A celery_app worker --loglevel=info

Start the Celery beat scheduler:
    celery -A celery_app beat --loglevel=info

Single-command Version:
    celery -A celery_app worker -B --loglevel=info

'''

from celery import Celery
from celery.schedules import crontab

# Initialize Celery app with Redis broker
app = Celery(
    'daily_task',
    broker='redis://localhost:6379/0',   # Redis URL
    backend='redis://localhost:6379/0'   # Result backend (optional)
)

# Example task
@app.task
def my_daily_task():
    print("Task executed!")

# Schedule the task daily at a specific time (e.g., 08:30 AM)
app.conf.beat_schedule = {
    'execute-daily-task': {
        'task': 'celery_app.my_daily_task',
        'schedule': crontab(hour=8, minute=30),
        # 'args': (),  # If your task needs arguments
    },
}
app.conf.timezone = 'UTC'  # Change timezone if needed

