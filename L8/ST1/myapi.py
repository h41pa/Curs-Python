from flask import Flask, g

from db import init_app, get_db

app = Flask(__name__)
init_app(app)
if __name__ == '__main__':
    app.run()

@app.route('/me')
def me():
    return {
        "username": "Adela",
        "id": 21,
        "email": "djkfs@fdsk.fjdl"
    }

"""
By default, toate rutele sunt de tipul GET.
Daca vrem sa avem si alte metode, trebuie sa specificam, cu sintaxa:
@app.route('/ruta', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
"""
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Pentru a stii ce metoda este in momentul curent, folosim un obiect special Flask numit request.
     Acest obiect contine informatii despre:
     - metoda folosita
     - request body
     - headere
     - samd
    """
    if request.method == 'GET':
        return {
            "message": "Please use your username and password to login!"
        }
    else:
        # POST, trebuie sa vedem ce date am primit de la client
        username = request.json['username']
        password = request.json['password']
        # Pentru a putea loga un user, trebuie sa vedem daca exista in db, si daca combinatia user/parola este corecta
        db = get_db()   # prima data obtinem o conexiune la db
        user = db.execute(
            'SELECT * FROM user WHERE username = ?',
            (username,)
        ).fetchone()
        # 1. Verificam daca userul chiar exista, adica daca am gasit o potrivire pentru username in db
        if user is None:
            return {
                "message": "User does not exist!"
            }, 404
        # 2. Daca userul exista, verificam ca parola sa fie corecta!
        if user['password'] != password:    # nu o sa facem niciodata asa ceva in realitate, parolele se tin MEREU criptate in db
            return {
                "message": "Incorrect username/password combination"
            }, 401  # 401 - unauthorized
        # 3. Daca am ajuns pana aici, inseamna ca userul s-a logat cu success, asa ca putem sa trecem mai departe
        return {
            "username": user['username'],
            "message": "Login was successful!"
        }

@app.route('/register', methods=['POST'])
def register():
    uname = request.json['username']
    passw = request.json['password']
    db = get_db()

    db.execute(
        'INSERT INTO user (username, password) VALUES (?, ?)',
        (uname, passw)
    )
    db.commit()     # commit pentru db reprezinta o actiune persistenta
    return {
        "message": "User created!"
    }, 201
