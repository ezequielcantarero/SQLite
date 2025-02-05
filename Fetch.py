import sqlite3

conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
usuario_unico = cursor.fetchone()  # Obtiene solo un resultado
print("Un solo usuario:", usuario_unico)

cursor.execute("SELECT * FROM users")
todos_los_usuarios = cursor.fetchall()  # Obtiene todos los resultados
print("Todos los usuarios:", todos_los_usuarios)

conn.close()
