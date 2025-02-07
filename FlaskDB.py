from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def obtener_usuarios():
    conn = sqlite3.connect("SQLite_Ezequiel_Prueba1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    usuarios = cursor.fetchall()
    conn.close()
    return [{"id": u[0], "nombre": u[1], "edad": u[2]} for u in usuarios]

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(obtener_usuarios())

if __name__ == "__main__":
    app.run(debug=True)
