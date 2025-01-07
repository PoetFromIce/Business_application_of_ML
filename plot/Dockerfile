FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt ./

#Устанавливаем зависимтости
RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы с исходным кодом
COPY src/ ./src/

# Создаём директорию для логов внутри контейнера
RUN mkdir logs

# Запуск приложения
CMD ["python", "./src/plot.py"]
