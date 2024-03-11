"""
Ce este un web framework - este practic o biblioteca (library) care ofera sprijin pentru
construirea unui website sau a unui web API.

Un web framework este mai complex decat o librarie gen requests/random/etc.
Pentru Python, avem 2 mari WF:
1. Flask - micro web framework = este foarte lightweight.
2. Django - probabil cel mai folosit framework de Python, este foarte complex.

Features comune ale Flask si Django:
- integrare usoara cu bazele de date
- template engine pentru a crea o interfata utilizator in HTML + CSS
- CLI (command line interface) pentru rularea unui server, conexiune la db, si alte comenzi
- decoratori, design patterns

"""

from flask import Flask

# Cream o aplicatie Flask, careia ii dam numele __name__ => numele fisierului curent
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    first = '1' + 'st'
    return f"Hello, this is my {first} Flask app!"


@app.route('/')
def index():
    return "This is my homepage"


# aceasta linie ne ajuta sa rulam aplicatia DOAR atunci cand rulam fisierul curent, adica python web_frameworks.py
# nu si cand il importam in alte fisiere
if __name__ == '__main__':
    app.run()

"""
Comanda de rulare a serverului nostru este:
flask --app .\S8\ST1\web_frameworks.py run

generic vorbind:
flask --app <nume fisier python unde avem app> run

Vom primi o linie care ne zice ca serverul s-a pornit:
* Running on http://127.0.0.1:5000

127.0.0.1 = adresa IP a calculatorului nostru in reteaua personala
5000 = portul pe care ruleaza serverul nostru; un calculator are multe porturi, si trebuie sa precizam portul 
atunci cand rulam local.

"""

"""
Debug = atunci cand avem o eroare de logica in cod, se numeste bug (gandac).
Debug = tehcnica si actiunile pe care noi le facem ca sa depistam si sa reparam un bug.

Cea mai simpla metoda de debugging este sa printam anumite variabile in codul nostru, si
sa urmarim firul logic de executie, pana cand depistam linia la care se intampla eroarea.

Pentru Flask, trebuie sa adaugam flag-ul de debug atunci cand rulam serverul:
flask --app <app name> run --debug
"""


"""
Pentru a putea avea parametrii in endpoint, folosim semnele < si >,
iar prin intermediul decoratorului @app.route, vom avea injectata o variabila in functia noastra
cu acelasi nume ca cel definit de noi in ruta.

Pentru aceasta ruta, acum putem apela:
http://127.0.0.1:5000/hello/1234567890
http://127.0.0.1:5000/hello/adela
http://127.0.0.1:5000/hello/numele%20meu%20este%20adela

In cazul anumitor caractere din URL, browserul le va inlocui cu niste coduri, spre exemplu spatiul ( )
va fi inlocuit de codul `%20`. Aceasta operatiune se numeste URL-encoding.
"""
@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}"

"""
Putem face si validarea tipului de parametru asteptat in url, cu sintaxa:
/ceva/<tip:nume param>

De exemplu, mai jos putem accesa:
http://127.0.0.1:5000/users/10
DAR
http://127.0.0.1:5000/users/adela
ne va da eroarea 404 NOT FOUND
"""

"""
Redirecting: a redirectiona un request catre un alt endpoint.
In Flask, folosim url_for pentru a redirectiona un request catre un alt endpoint (functie)
"""
from flask import url_for, redirect

@app.route('/users/<int:user_id>')
def hello_user(user_id):
    users = {
        1: 'Adela',
        2: 'Ion',
        3: 'Maria',
        4: 'Gheo',
        5: 'Janos'
    }
    if user_id in users:
        username = users[user_id]
        return redirect(url_for('hello_name', name=username))
    else:
        # putem sa setam un status code dupa mesajul cu care raspundem la request (default e 200)
        return 'Not a valid user!! Please register!', 404

