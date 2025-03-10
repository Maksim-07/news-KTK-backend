API_URL="http://localhost:8000"

ACCESS_TOKEN=$(curl -s -X 'POST' \
  "$API_URL/api/news-ktk/v1/auth/login" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=admin&password=adminpassword&scope=&client_id=string&client_secret=string' \
  | jq -r '.access_token')

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news-category" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d '{
  "name": "Спорт",
  "description": "Спортивные мероприятия в колледже"
}'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news-category" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d '{
  "name": "Наука и технологии",
  "description": "Новости о научных исследованиях"
}'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news-category" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d '{
  "name": "Студенческая жизнь",
  "description": "Новости о студенческих мероприятиях"
}'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/users" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d '{
  "username": "admin",
  "email": "admin@mail.ru",
  "first_name": "Имя",
  "last_name": "Фамилия",
  "password": "adminpassword"
}'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news?title=%D0%91%D0%B0%D1%81%D0%BA%D0%B5%D1%82%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D0%B5%D0%B7%D0%BE%D0%BD%20%D1%81%D1%82%D0%B0%D1%80%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%21&content=%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D1%82%D0%B5%20%D0%BD%D0%B0%D1%88%D1%83%20%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%83%20%D0%BD%D0%B0%20%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%B9%20%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D0%B5%D0%B9%20%D0%B8%D0%B3%D1%80%D0%B5%21%20%D0%92%2019%3A00%20-%2029%20%D0%BC%D0%B0%D1%80%D1%82%D0%B0%20%D0%B2%20%D0%B0%D0%BA%D1%82%D0%BE%D0%B2%D0%BE%D0%BC%20%D0%B7%D0%B0%D0%BB%D0%B5%20%D0%BD%D0%B0%20%D0%94%D0%B5%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9%2015.&author_id=1&category_id=1" \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -F 'image=@images/sport_basketball.jpg;type=image/jpeg'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news?title=%D0%A2%D1%80%D0%B8%D1%83%D0%BC%D1%84%20%D0%BD%D0%B0%20%D0%B1%D0%B5%D0%B3%D0%BE%D0%B2%D0%BE%D0%B9%20%D0%B4%D0%BE%D1%80%D0%BE%D0%B6%D0%BA%D0%B5%21&content=%D0%9B%D0%B5%D0%B3%D0%BA%D0%BE%D0%B0%D1%82%D0%BB%D0%B5%D1%82%D0%BA%D0%B0%20%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%B4%D0%B6%D0%B0%20%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D0%BB%D0%B0%20%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%80%D0%B5%D0%BA%D0%BE%D1%80%D0%B4%20%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D0%B0%20%D0%BD%D0%B0%20%D0%B4%D0%B8%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%B8%201500%20%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2%21%20%D0%92%D1%8B%D0%B4%D0%B0%D1%8E%D1%89%D0%B5%D0%B5%D1%81%D1%8F%20%D0%B2%D1%8B%D1%81%D1%82%D1%83%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%81%D0%BF%D0%BE%D1%80%D1%82%D1%81%D0%BC%D0%B5%D0%BD%D0%BA%D0%B8%20%D0%BF%D1%80%D0%B8%D0%BD%D0%B5%D1%81%D0%BB%D0%BE%20%D0%B5%D0%B9%20%D0%B7%D0%BE%D0%BB%D0%BE%D1%82%D0%BE%20%D0%BD%D0%B0%20%D1%80%D0%B5%D0%B3%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D1%81%D0%BE%D1%80%D0%B5%D0%B2%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%D1%85%20%D0%B8%20%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D0%BB%D0%BE%20%D0%BF%D1%83%D1%82%D1%8C%20%D0%BA%20%D0%BD%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC%D1%83%20%D1%87%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD%D0%B0%D1%82%D1%83.&author_id=1&category_id=1" \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -F 'image=@images/sport_treadmill.jpg;type=image/jpeg'

curl -X 'POST' \
  "$API_URL/api/news-ktk/v1/news?title=%D0%9E%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%B0%20%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%BB%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D1%8F%20%D0%B2%D0%B8%D1%80%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9%20%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%21&content=%D0%9E%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%B0%20%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%BB%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D1%8F%20%D0%B2%D0%B8%D1%80%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9%20%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%21%20C%D1%82%D1%83%D0%B4%D0%B5%D0%BD%D1%82%D1%8B%20%D1%81%D0%BC%D0%BE%D0%B3%D1%83%D1%82%20%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D1%8C%20%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%B2%20%D0%B8%D0%BC%D0%BC%D0%B5%D1%80%D1%81%D0%B8%D0%B2%D0%BD%D0%BE%D0%B9%20%D1%81%D1%80%D0%B5%D0%B4%D0%B5%21%20%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D1%8F%20%D0%BE%D1%81%D0%BD%D0%B0%D1%89%D0%B5%D0%BD%D0%B0%20%D0%BD%D0%BE%D0%B2%D0%B5%D0%B9%D1%88%D0%B8%D0%BC%20%D0%BE%D0%B1%D0%BE%D1%80%D1%83%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC%20%D0%B8%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D0%B2%D1%81%D0%B5%D1%85%20%D0%B6%D0%B5%D0%BB%D0%B0%D1%8E%D1%89%D0%B8%D1%85.%20%D0%9F%D1%80%D0%B8%D1%85%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%20%D0%B2%20201%20%D0%BA%D0%B0%D0%B1%D0%B8%D0%BD%D0%B5%D1%82%21&author_id=1&category_id=2" \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -F 'image=@images/science_new_laboratory.jpg;type=image/jpeg'
