import sqlite3

conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE nombre = ?", ("Ana",))

conn.commit()
conn.close()
