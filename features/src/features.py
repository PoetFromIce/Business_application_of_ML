import os
import pika
import numpy as np
import json
import time
from datetime import datetime
from sklearn.datasets import load_diabetes

# Загрузка датасета
X, y = load_diabetes(return_X_y=True)

# Подключение к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Объявление очередей
channel.queue_declare(queue='y_true')
channel.queue_declare(queue='features')
channel.queue_declare(queue='y_pred')

def generate_message_id():
    return datetime.timestamp(datetime.now())

while True:
    try:
        # Выбор случайной строки
        random_row = np.random.randint(0, X.shape[0] - 1)
        message_id = generate_message_id()

        # Формируем сообщения
        message_y_true = {
            'id': message_id,
            'body': float(y[random_row])
        }

        message_features = {
            'id': message_id,
            'body': X[random_row].tolist()
        }

        # Генерируем предсказание (имитация модели)
        y_pred_value = float(y[random_row] + np.random.normal(0, 20))
        message_y_pred = {
            'id': message_id,
            'body': y_pred_value
        }

        # Отправка сообщений
        channel.basic_publish(exchange='', routing_key='y_true', body=json.dumps(message_y_true))
        channel.basic_publish(exchange='', routing_key='features', body=json.dumps(message_features))
        channel.basic_publish(exchange='', routing_key='y_pred', body=json.dumps(message_y_pred))

        print(f"Отправлено в y_true: {message_y_true}")
        print(f"Отправлено в features: {message_features}")
        print(f"Отправлено в y_pred: {message_y_pred}")

        time.sleep(10)  # задержка между итерациями

    except Exception as e:
        print(f"Ошибка при отправке сообщений: {e}")
        time.sleep(5)   # задержка перед повтором
