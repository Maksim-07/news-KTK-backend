from fastapi import HTTPException, status

news_category_not_found_exceptions = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="News Category not found"
)

news_category_already_exists_exceptions = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="News Category already exists"
)
