## Инструкция для развертывания приложения в Докере

### 1. Клонирование репозитория

``` Bash
git clone https://github.com/Maksim-07/news-KTK-backend.git

cd news-KTK-backend
```

### 2. Настройка переменных окружения Python

Создать файл ```.env``` в корневой папке ```src``` и заполнить следующим содержимым:

```
POSTGRES_HOST="news-ktk-db"
POSTGRES_PORT=5632
POSTGRES_USER="news-ktk-db"
POSTGRES_PASSWORD="news-ktk-db"
POSTGRES_DB="news-ktk-db"

SECRET_KEY="your-secret-key-for-jwt-token"
ALGORITHM="your-algorithm"
```

### 3. Запуск приложения с помощью Docker Compose

``` Bash
docker-compose --env-file src/.env up --build -d
```

