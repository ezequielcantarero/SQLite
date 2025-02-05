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

#VALUES (?, ?)
#Prevención de Inyección SQL
#Si se concatenaran los valores directamente en la consulta, un atacante podría manipular la entrada y ejecutar código malicioso.

#Parámetros Evitan Problemas de Formato y Tipos de Datos
#Al usar ?, sqlite3 se encarga de manejar automáticamente los tipos de datos y escapar correctamente los valores.

#Mejora del Rendimiento con Ejecuciones Múltiples
#Cuando usas ?, SQLite puede reutilizar la estructura de la consulta y solo cambiar los valores, optimizando el rendimiento.

