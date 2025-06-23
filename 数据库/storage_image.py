import sqlite3
from PIL import Image
import io

conn = sqlite3.connect('ceshi.db')

cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE Image (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL UNIQUE,
#         size INTEGER,
#         type TEXT,
#         data BLOB
#     )
# ''');

image = Image.open('..\\1.jpg')

buffer = io.BytesIO()
image.save(buffer,format='JPEG')

image_data = buffer.getvalue()

data=('renzongxuan',len(image_data),'jpg',image_data)
# ?是占位符，可以防止SQL注入攻击
cursor.execute('INSERT INTO Image (name, size, type, data) VALUES (?, ?, ?, ?)', data)

cursor.close()

conn.commit()

conn.close()