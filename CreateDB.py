import sqlite3

# Conectar a la base de datos (si no existe, se crea automáticamente)
conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Cerrar la conexión
conn.close()
