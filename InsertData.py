#Insert
import sqlite3

conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO users (nombre, edad) VALUES (?, ?)", ("Juan", 25))
cursor.execute("INSERT INTO users (nombre, edad) VALUES (?, ?)", ("Ana", 30))

conn.commit()
conn.close()

#Insert Masivo
import sqlite3
conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
cursor = conn.cursor()

usuarios = [("Carlos", 28), ("Sofía", 22), ("Miguel", 35)]

cursor.executemany("INSERT INTO users (nombre, edad) VALUES (?, ?)", usuarios)
conn.commit()
conn.close()
