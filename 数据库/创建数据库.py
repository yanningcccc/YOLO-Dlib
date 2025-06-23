import sqlite3

# 连接到SQLite数据库
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('ceshi.db')

# 创建一个Cursor:
cursor = conn.cursor()

# 执行一条SQL语句，创建user表:
cursor.execute('''
    CREATE TABLE manager (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        username TEXT NOT NULL UNIQUE,         
        password TEXT NOT NULL                 
    )
''')

# 关闭Cursor:
cursor.close()

# 提交事务:
conn.commit()

# 关闭Connection:
conn.close()
