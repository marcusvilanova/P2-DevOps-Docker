from flask import Flask, render_template, request, jsonify
import mysql.connector
import os
import time

app = Flask(__name__)

def get_db_connection():
    # Loop para esperar o banco subir (importante para o Docker)
    retries = 5
    while retries > 0:
        try:
            conn = mysql.connector.connect(
                host=os.getenv("DB_HOST", "db"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "root"),
                database=os.getenv("DB_NAME", "dimdim_db")
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Erro ao conectar: {err}. Tentando novamente em 5s...")
            retries -= 1
            time.sleep(5)
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuarios', methods=['GET'])
def list_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255))")
    cursor.execute("SELECT * FROM usuarios")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/usuarios', methods=['POST'])
def add_user():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Usuário criado!"}), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nome=%s, email=%s WHERE id=%s", (nome, email, id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Usuário atualizado!"})

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Usuário deletado!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
