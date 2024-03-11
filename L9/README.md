## Django

### Ce este Django?

Django este un web framework care ne ofera foarte multe features pentru dezvoltarea site-urilor web, cum ar fi:
- o structura predefinita a proiectului (project si apps)
- multiple comenzi din terminal (CLI) care ne ajuta sa facem rapid anumite actiuni
- ORM (object-relational mapping) - un modul care ne permite sa lucram cu bazele de date fara a fi necesar cod SQL
- o interfata de administrare pentru modele
- modele predefinite pentru utilizatori, grupuri, roluri
- template (HTML) engine integrat
- notiuni mai avansate de securitate, caching, etc
- server de dezvoltare integrat
- engine de db integrat (SQLite)


Django are o arhitectura MVC/MVT (Model-View-Template):
- Model = modelele reprezinta clase Python care corespund unei tabele SQL
- View = reprezinta un endpoint (adica un request-response)
- Template = fisiere HTML dinamice, generate pe backend si servite automat printr-un view


### Cum incepem?

Avem comenzi CLI, printre care:
- startproject: `django-admin startproject <nume proiect>` -- va crea structura de foldere si fisiere necesara pentru proiectul nostru

Dupa ce am facut un proiect, putem porni direct serverul, schimband path-ul in folderul <nume proiect>,
si ruland comanda:
`python manage.py runserver`

Apoi, putem incepe sa cream aplicatii (apps) cu comanda:
`python manage.py startapp <nume app>`

O aplicatie este un modul functional Django, in care logica codului este grupata impreuna.


### ORM si baze de date

ORM (object-relational mapping) este un modul care ne ajuta sa nu folosim SQL, deoarece Django mapeaza
tabelele si structura unei baze de date direct in cod Python, dupa cum urmeaza:
- o clasa Python (numita model) corespunde unei tabele de baza de date (exemplu User)
- fiecare atribut al acestei clase (numite fields) corespunde unei coloane a tabelei (exemplu username, password, name, email, etc)
- fiecare instanta a acestei clase (obiect) corespunde unui rand din tabela SQL (adica un user anume)

Pentru gestiunea bazei de date avem urmatoarele comenzi:
- `python manage.py migrate` -- migrate aduce baza de date la zi cu modificarile din cod, adica updateaza tabelele
    sa corespunda cu modelele Python. Acest lucru se intampla prin niste fisiere speciale, numite migrations.
- `python manage.py makemigrations` -- aceasta comanda genereaza fisierele mentionate mai sus din codul nostru Python.

Pentru a putea genera fisiere de migrari, app noastra trebuie sa fie adaugata in settings, in `INSTALLED_APPS`.

Pentru a putea face queries pe db, vom folosi intotdeauna modelele:
- INSERT: pentru a insera in baza de date, vom crea un obiect din clasa noastra model, iar apoi vom apela metoda `save()`
- UPDATE: la fel si pentru update, vom folosi obiectul (instanta clasei) si dupa ce facem modificari, apelam `save()`
- DELETE: avem metoda `delete()` care sterge din baza de date, dar obiectul Python ramane in continuare disponibil (fara id)
- SELECT: folosim un concept numit object manager, adica pe numele clasei-model vom apela `objects`, iar apoi putem face
  - `all()` - imi da toate obiectele din acel model
  - `get(id=<valoare id>)` - imi da obiectul cu ID-ul pk, returneaza un singur obiect
  - `filter(params)` - imi permite sa filtrez obiectele

Object managerul va returna (aproape) mereu un `QuerySet` (un set de rezultate), care este de fapt doar o lista de obiecte,
instante ale clasei noastre model.

Atunci cand avem o relatie inversa (one to many) Django va genera automat un object manager care ne va permite sa obtinem
tot setul de obiecte related, iar pe acest set putem aplica aceleasi metode ca si mai sus (all, get, filter)


### Shell si DB api

Pentru a ne conecta la shell (consola interactiva), folosim comanda:
`python manage.py shell`

Apoi putem sa folosim modelele, si sa executam diferite instructiuni (atentie, trebuie sa le importam).


### Interfata admin

Pentru a putea gestiona modelele create, Django are deja o interfata de administrare, unde putem adauga/edita/sterge date.
Pentru a folosi aceasta interfata, in primul rand avem nevoie de un cont (un user care are rol de admin):
`python manage.py createsuperuser`
Pentru a crea un superuser, rulam comanda de mai sus, si urmam instructiunile de adaugare username si parola.
Apoi putem accesa interfata de admin la `http://127.0.0.1:8000/admin`. Daca nu suntem inca logati, vom fi redirectionati automat catre login.

Pentru a putea vedea modelele create de noi in interfata de admin, trebuie sa le inregistram (adica in folderul app noastre,
in fisierul admin.py, trebuie sa apelam functia register cu numele modelului).


### Templates HTML

Pentru a putea avea niste raspunsuri HTML din views, folosim engine-ul de templates integrat in Django.
Acesta ne permite sa facem fisiere HTML dinamice (adica care sunt generate la runtime) prin prezenta unor
structuri speciale numite template tags.

Template-urile pentru o aplicatie se vor pune in folderul `<nume app>/templates/<nume app>`.
Exemple de template tags:
```
    {% if conditie %}
        <cod HTML>
    {% else %}
        <alt cod HTML>
    {% endif %}
```
```ignorelang
    {% for item in collection %}
        <cod HTML in care putem folosi item>
    {% endfor %}
```

Pentru a afisa date, folosim duble acolade.
```ignorelang
{{ question.question_text }}
```

Toate aceste template tags sunt evaluate la rulare, si fisierul generat va fi pur HTML.