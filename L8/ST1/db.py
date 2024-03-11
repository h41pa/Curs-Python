import sqlite3  # librarie care ne ajuta sa folosim SQLite ca si engine de db
import click    # librarie care ne ajuta sa cream comenzi de terminal
from flask import current_app, g
# current_app este aplicatia curenta de Flask
# g este un obiect special care isi pastreaza starea pe parcursul unui request, si in care
# vom pastra conexiunea la baza de date, ca sa nu trebuiasca sa o refacem de fiecare data
import os


def get_db():
    if 'db' not in g:
        # Facem o conexiune la baza de date
        g.db = sqlite3.connect(
            'mydb.sqlite',      # fisierul in care facem noi baza de date, trebuie sa aiba extensia sqlite
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        # Daca avem o conexiune deschisa, trebuie sa o inchidem
        db.close()

"""
Functia init_db creaza practic tabela de USERS.
"""
def init_db():
    # Luam o instanta a bazei de date, adica cream o conexiune
    db = get_db()

    # Folosim un context manager pentru a deschide fisierul `schema.sql`
    with current_app.open_resource('schema.sql') as f:
        # si pentru a-l rula pe baza noastra de date
        db.executescript(f.read().decode('utf8'))


"""
click = o librarie care ne ajuta sa cream comenzi de terminal
flask --app <app name> <nume comanda>

Cu decoratorul @click.command putem sa cream orice comanda vrem noi
"""
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


"""

"""
def init_app(app):
    # Aici setam app noastra sa inchida conexiunea la db atunci cand se inchide app
    # teardown = fix inainte de oprirea aplicatiei
    app.teardown_appcontext(close_db)
    # aici adaugam comanda declarata anterior la comenzile disponibile prin Flask
    app.cli.add_command(init_db_command)
