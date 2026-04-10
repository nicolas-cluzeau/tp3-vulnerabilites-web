from flask import Flask
import os
import sqlite3


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>App Flask pour Pipeline CI/CD</h1><p>Statut : Sécurisé</p>'

@app.route('/vuln')
def inject():
    # 1. Command Injection
    command = request.args.get('command')
    os.system(command)

    # 2. SQL Injection
    username = request.args.get('username')
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '%s'" % username
    cursor.execute(query)
    return "Je suis très sécurisé!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
