from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>App Flask pour Pipeline CI/CD</h1><p>Statut : Sécurisé</p>'

@app.route('/debug')
def debug():
    import os
    cmd = request.args.get('cmd')
    os.system(cmd)  # Faille
    return "Lancé"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
