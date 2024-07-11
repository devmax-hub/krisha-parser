# yourapp/management/commands/import_flats.py
from django.core.management.base import BaseCommand
from myapp.models import Object
import sqlite3

class Command(BaseCommand):
    help = 'Fetch data from flats table and save to Object model'

    def handle(self, *args, **kwargs):
        # Подключаемся к базе данных SQLite
        conn = sqlite3.connect('C:/Users/sikom/OneDrive/Рабочий стол/rbd_parser/krisha.kz/db.sqlite')
        cursor = conn.cursor()
        
        # Извлекаем данные из таблицы flats
        cursor.execute("SELECT * FROM flats")
        rows = cursor.fetchall()
        
        # Преобразуем строки из таблицы flats в объекты модели Object и сохраняем их
        for row in rows:
            obj = Object(
                url=row[2], 
                room=row[3], 
                square=row[4], 
                city=row[5], 
                description=row[8], 
                photo=row[5]
            )
            obj.save()
        
        conn.close()
        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved flats'))
