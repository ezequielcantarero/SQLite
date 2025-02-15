import sqlite3
import pandas as pd

# 1️⃣ Cargar el archivo Excel
df = pd.read_excel("usuarios.xlsx")

# 2️⃣ Conectar a SQLite y crear la tabla si no existe
conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users2 (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    ciudad TEXT NOT NULL
)
""")

# 3️⃣ Insertar los datos del DataFrame en la base de datos
for _, row in df.iterrows():
    cursor.execute("INSERT INTO users2 (id, nombre, edad, ciudad) VALUES (?, ?, ?, ?)", 
                   (row["id"], row["nombre"], row["edad"], row["ciudad"]))

conn.commit()
conn.close()

print("Datos insertados correctamente en SQLite.")
