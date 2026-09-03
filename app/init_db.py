from db.db import engine, Base, SessionLocal
from db import crud, models

# Создаем таблицы в базе данных

Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# 1. Добавляем 2 категории
cat1 = crud.create_category(db, "Фантастика")
cat2 = crud.create_category(db, "Научная литература")

# 2. Добавляем книги (по 2-4 на каждую категорию)
crud.create_book(db, "Дюна", "Эпическая сага о пустынной планете Арракис", 750.50, "", cat1.id)
crud.create_book(db, "Гиперион", "История паломников к Гробницам Времени", 600.00, "", cat1.id)
crud.create_book(db, "Краткая история времени", "От Большого взрыва до черных дыр", 800.00, "", cat2.id)
crud.create_book(db, "Эволюция", "Теория Дарвина и современная генетика", 950.00, "", cat2.id)

db.close()
print("База данных успешно создана и заполнена!")