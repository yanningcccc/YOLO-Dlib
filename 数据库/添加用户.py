import sqlite3

# 连接到数据库
conn = sqlite3.connect('ceshi.db')
cursor = conn.cursor()

# 插入多条记录
manager = [
    ('manager', 12345)
]

# 使用参数化查询防止SQL注入
cursor.executemany('INSERT INTO manager (username, password) VALUES (?, ?)', manager)

# 提交事务并关闭连接
conn.commit()
cursor.close()
conn.close()
