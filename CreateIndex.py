import sqlite3

conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
cursor = conn.cursor()

cursor.execute("CREATE INDEX idx_users_nombre ON users (nombre)")

conn.commit()
conn.close()

#Antes del index 
#Execution finished without errors.
#Result: 1 rows returned in 9ms
#At line 1:
#EXPLAIN QUERY PLAN SELECT * FROM users WHERE nombre = 'Juan';

#Despues del index 
#Execution finished without errors.
#Result: 1 rows returned in 8ms
#At line 1:
#EXPLAIN QUERY PLAN SELECT * FROM users WHERE nombre = 'Juan';