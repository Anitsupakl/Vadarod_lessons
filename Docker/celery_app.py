from celery import Celery

# Подключение к RabbitMQ (брокер) и Redis (хранение результатов)
app = Celery(
    'simple_project',
    broker='amqp://guest:guest@rabbit:5672//',  # RabbitMQ
    backend='redis://redis:6379/0'              # Redis
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

# Автоматически находит задачи в tasks.py
app.autodiscover_tasks(['tasks'])