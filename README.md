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

После этих действий можно переходить по ссылке http://localhost:8000/api/swagger

Если вы хотите заполнить базу данных, то выполните следующие действия:

### 4. Добавления пользователя в БД, чтобы следующим действием получить JWT токен

``` Bash
docker exec -it news-ktk-db psql -U news-ktk-db -p 5632 -d news-ktk-db
```

После этой команды должна запуститься интерактивная сессия, в ней выполняем следующую команду:

```
insert into users (username, password, email, first_name, last_name) values ('adminka', '$2a$12$VCxu5kOumfbGteeDSc32Ce5/2dGgM3PzUP/sKhXzZSlcvRR138D3S', 'adminka@mail.ru', 'Имя', 'Фамилия');
```

### 5. Запускаем скрипт fill_data.sh в корне репозитория

``` Bash
bash fill_data.sh
```
