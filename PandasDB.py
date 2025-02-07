import sqlite3
import pandas as pd

conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
df = pd.read_sql_query("SELECT * FROM users", conn)

df.to_csv("usuarios.csv", index=False)
conn.close()
