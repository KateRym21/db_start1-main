import sqlite3

conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM artists")
data = cursor.fetchall()
print(len(data))

cursor.execute('SELECT * FROM artists WHERE gender =="Female"')
data = cursor.fetchall()
print(len(data))

cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900')
data = cursor.fetchall()
print(len(data))






# Запитання 1. Інформація про скількох художників представлена у базі даних?


# Запитання 2. Скільки жінок (Female) у базі?


# Запитання 3. Скільки людей у базі даних народилися до 1900 року?


# Запитання 4*. Як звати найстаршого художника?