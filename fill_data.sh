API_URL="http://localhost:8000"
USERNAME="adminka"
PASSWORD="adminka"

ACCESS_TOKEN=$(curl -s -X 'POST' \
  "$API_URL/api/news-ktk/v1/auth/login" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d "grant_type=password&username=$USERNAME&password=$PASSWORD&scope=&client_id=string&client_secret=string" \
  | jq -r '.access_token')

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news-category" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d '{
  "name": "Sport",
  "description": "College Sports events"
}'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news-category" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d '{
  "name": "Science and technology",
  "description": "News about scientific research"
}'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news-category" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d '{
  "name": "Student life",
  "description": "News about student events"
}'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news" \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H 'Content-Type: multipart/form-data' \
  -F 'title=Баскетбольный сезон стартовал!' \
  -F 'content=Поддержите нашу команду на первой домашней игре! В 19:00 - 29 марта в актовом зале на Деловой 15.' \
  -F 'author_id=1' \
  -F 'category_id=1' \
  -F 'image=@images/sport_basketball.jpg;type=image/jpeg'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news" \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H 'Content-Type: multipart/form-data' \
  -F 'title=Триумф на беговой дорожке!' \
  -F 'content=Легкоатлетка колледжа установила новый рекорд университета на дистанции 1500 метров! Выдающееся выступление спортсменки принесло ей золото на региональных соревнованиях и открыло путь к национальному чемпионату.' \
  -F 'author_id=1' \
  -F 'category_id=1' \
  -F 'image=@images/sport_treadmill.jpg;type=image/jpeg'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news" \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H 'Content-Type: multipart/form-data' \
  -F 'title=Открыта новая лаборатория виртуальной реальности!' \
  -F 'content=Открыта новая лаборатория виртуальной реальности! Cтуденты смогут проводить эксперименты в иммерсивной среде! Лаборатория оснащена новейшим оборудованием и доступна для всех желающих. Приходите в 201 кабинет!' \
  -F 'author_id=1' \
  -F 'category_id=2' \
  -F 'image=@images/science_new_laboratory.jpg;type=image/jpeg'
