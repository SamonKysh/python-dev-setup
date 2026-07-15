from db.db import SessionLocal
from db import crud

db = SessionLocal()

print("=== СПИСОК КАТЕГОРИЙ ===")
categories = crud.get_categories(db)
for cat in categories:
    print(f"ID: {cat.id} | Название: {cat.title}")

print("\n=== СПИСОК КНИГ ===")
books = crud.get_books(db)
for book in books:
    print(f"ID: {book.id} | {book.title} | Цена: {book.price} руб. | Категория: {book.category.title}")

db.close()