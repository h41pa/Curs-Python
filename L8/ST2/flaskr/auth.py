"""
Modulul de auth, contine endpointuri precum:
- login
- logout
- register

Ar mai putea contine:
- forgot pass
- reset pass
- change user info
"""

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .db import get_db

"""
In Flask, un BP (blueprint) este practic o colectie de rute, care ne permite sa grupam
aceste rute bazat pe functionalitatile lor. De exemplu, aici vom avea un prefix pentru toate rutele:
- /auth/login
- /auth/logout
- /auth/register
"""
bp = Blueprint('auth', __name__, url_prefix='/auth')


# aici nu vom mai avea @app.route, deoarece folosim un blueprint
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        # trebuie sa cream un nou user, cu request.form luam datele primite in corpul requestului
        username = request.form['username']
        password = request.form['password']
        # obtinem apoi o conexiune la baza de date
        db = get_db()
        # folosim o var numita error in care vom tine eventualele erori aparute la inregistrare
        error = None

        # aici incepem sa facem validari:
        # 1. verificam ca campul de username a fost completat
        if not username:
            error = 'Username is required.'
        # 2. verificam ca campul de parola a fost completat
        elif not password:
            error = 'Password is required.'

        # daca nu avem nici o eroare dupa validari
        if error is None:
            # incercam sa introducem userul in baza de date
            # folosim un try-except deoarece avem o constrangere cum ca username trebuie sa fie unic
            try:
                # parolele nu se tin NICIODATA in baza de date in forma lor originala, ci DOAR criptate
                hashed_pass = generate_password_hash(password)
                db.execute(
                    # INSERT INTO nume_table (col1, col2, col3...) VALUES (?, ?, ? ...)
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, hashed_pass),
                )
                # commit (sql) reprezinta actiunea de permanentizare a instructionilor anterioare
                # necesara pentru instructiuni care modifica datele din db
                db.commit()
            except db.IntegrityError:
                # avem constrangere unica pe username, asa ca vom returna un mesaj de eroare daca se incearca duplicarea acestuia
                error = f"User {username} is already registered."
            else:
                # try-except-else
                # else va fi apelat doar atunci cand try a fost executat cu succes
                return redirect(url_for("auth.login"))

        # daca am ajuns pana aici, inseamna ca avem o eroare la register,
        # si trebuie sa i-o afisam utilizatorului; folosim pentru asta functia flash (din flask)
        flash(error)

    # aici vom ajunge daca metoda noastra este GET, adica atunci cand utilizatorul vrea sa "ia" pagina de register
    # folosim functia de render_template care va randa un template HTML, din folderul auth, numit register.html
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        # incercam sa vedem in primul rand daca username-ul exista in baza de date
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/base')
def base():
    return render_template('base.html')
