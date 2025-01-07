FROM python:3.9-slim

WORKDIR /app  #устанавка рабочей директории внутри контейнера

#копирование файла requirements.txt и установка зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/     #копирование исходного кода приложения

CMD ["python", "./src/features.py"] #запуск приложения
