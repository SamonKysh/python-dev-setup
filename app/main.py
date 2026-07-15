from fastapi import FastAPI
from .api import categories, books
from .db.db import engine, Base

# Гарантируем, что таблицы созданы
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Octagon Books API", description="API для управления книгами")

# Подключаем роутеры
app.include_router(categories.router)
app.include_router(books.router)

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok", "message": "Сервис работает"}