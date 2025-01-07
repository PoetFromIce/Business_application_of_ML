# Business_application_of_ML
В репозитории представлен набор микросервисов для выполнения задач машинного обучения с использованием RabbitMQ для обмена сообщениями между сервисами. Проект включает в себя следующие компоненты:

## Структура проекта

```plaintext
metrics-flow/
    ├── docker-compose.yml
    ├── features/
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   └── src/
    │       └── features.py
    ├── logs/
    │   ├── error_distribution.png
    │   └── metric_log.csv
    ├── metric/
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   └── src/
    │       └── metric.py
    └── plot/
        ├── Dockerfile
        ├── requirements.txt
        └── src/
            └── plot.py
