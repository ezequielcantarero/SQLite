import sqlite3

conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
cursor = conn.cursor()

cursor.execute("UPDATE users SET edad = ? WHERE nombre = ?", (26, "Juan"))

conn.commit()
conn.close()
