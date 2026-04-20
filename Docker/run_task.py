from tasks import read_and_save_json

if __name__ == '__main__':
    print("Запускаем задачу...")
    result = read_and_save_json.delay()  # .delay() - асинхронный запуск
    print(f"ID задачи: {result.id}")
    print(f"Результат: {result.get(timeout=10)}")  # Ждём результат