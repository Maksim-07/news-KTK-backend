from fastapi import HTTPException, status

news_category_not_found_exceptions = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="News Category not found"
)

news_category_already_exists_exceptions = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="News Category already exists"
)

user_not_found_exceptions = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

user_already_exists_exceptions = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

username_already_exists_exceptions = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Username already exists"
)

email_already_exists_exceptions = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")

news_not_found_exceptions = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="News not found")

news_already_exists_exceptions = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="News already exists")

role_already_exists_exceptions = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Role already exists")

incorrect_password_exceptions = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid password",
)

credentials_exceptions = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
)

invalid_token_exceptions = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token",
)

token_not_found_exceptions = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Token not found",
)

refresh_token_missing_exceptions = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token is missing"
)
