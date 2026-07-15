   # Octagon Books API
   
   REST API для управления каталогом книг и категорий на базе FastAPI и PostgreSQL.
   
   ## Как запустить
   
   1. Убедитесь, что PostgreSQL запущен: `sudo service postgresql start`
   2. Активируйте виртуальное окружение: `source venv/bin/activate`
   3. Установите зависимости: `pip install -r requirements.txt`
   4. Запустите сервер: `uvicorn app.main:app --reload`
   5. Откройте документацию: http://127.0.0.1:8000/docs