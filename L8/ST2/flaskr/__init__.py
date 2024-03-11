"""
Fisierul __init__.py transforma un folder normal intr-un python package, care poate fi
importat/folosit ca un modul Python normal.
"""

import os       # os=operating system, stdlib care ne ajuta sa lucram cu OS curent

from flask import Flask     # Flask = clasa cu care facem o aplicatie

from .db import init_db_command, close_db
from .auth import bp as auth_bp

"""
Functie care se ocupa de crearea si configurarea aplicatiei noastre
"""
def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',       # aici folosim dev, dar pe production am folosi o valoare secreta
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),      # path catre db
    )

    # ensure the instance folder exists
    try:
        # creaza structura de foldere necesara pentru aplicatie
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # cli - Command Line Interface
    # aici inregistram comanda de init db prin flask
    app.cli.add_command(init_db_command)
    # teardown = modalitatea prin care ii putem zice lui Flask sa faca ceva inainte de inchiderea app
    app.teardown_appcontext(close_db)

    # aici vom inregistra toate BP (de obicei avem 1 bp / modul)
    app.register_blueprint(auth_bp)

    return app

