import sqlite3

try:
    conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO users (nombre, edad) VALUES (?, ?)", ("Carlos", 28))
    conn.commit()
except sqlite3.Error as e:
    print("Error en la base de datos:", e)
finally:
    conn.close()
