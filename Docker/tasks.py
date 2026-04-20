import json
import redis
from celery_app import app

# Подключение к Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)


@app.task
def read_and_save_json():
    """Читает data.json и сохраняет в Redis"""
    try:
        # Читаем файл
        with open('/app/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Сохраняем в Redis (ключ: 'my_data')
        r.set('my_data', json.dumps(data, ensure_ascii=False))

        return f"Успешно сохранено в Redis: {len(json.dumps(data))} байт"

    except Exception as e:
        return f"Ошибка: {str(e)}"