import sqlite3

conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users2")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

conn.close()
