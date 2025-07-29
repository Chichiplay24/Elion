import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask on Render!'

# Cette partie est cruciale pour Render
if __name__ == '__main__':
    # Render définit une variable d'environnement 'PORT'
    # Nous utilisons cette variable, ou 5000 par défaut si elle n'existe pas (pour les tests locaux par exemple)
    port = int(os.environ.get("PORT", 5000))
    # L'application doit écouter sur toutes les interfaces (0.0.0.0) et sur le port défini
    app.run(host='0.0.0.0', port=port)
