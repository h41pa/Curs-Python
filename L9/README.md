## Django
https://docs.djangoproject.com/en/5.0/intro/tutorial02/
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

# dupa start app - in cazul me polls = app
- creem fisier urls.py  in folder "app" trebuie facut in fiecare app(daca avem mai multe), definim urlpatterns(mapeaza url) 
dupa trebuie importat app/urls.py in  in mysite.urls(pagina cu setarile site-ului) si folosim functia include() in urlpatterns
path("app/", include("app.urls"), name='app'),
 - name="index" folosit la redirect si etc.
- dupa ce cream o functie in view , ne duce in app/urls.py adauga in url patternspath("numefunctie", views.numefunc, name="hello")
- 

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

# Pentru a putea face queries pe db, vom folosi intotdeauna modelele:
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
mai multe aici : https://docs.djangoproject.com/en/5.0/intro/tutorial02/
Apoi putem sa folosim modelele, si sa executam diferite instructiuni (atentie, trebuie sa le importam).
from django.db
>>> from polls.models import Choice, Question 
> from django.utils import timezone
q1  = Question(question_text="What's new?", pub_date=timezone.now())
q1.save()  # pentru a salva in baza de date si ii da id
> putem vedea info despre q1  , folosind campurile data in db gen q1.question_text
> exit()
> allq = Question.objects.all()  - object manager vezi mai sus - un query allq[1] cu all() ne da o lista de obiecte
> q = Question.objects.get(id=2)
> q3 = Questions.objects.filter(question_text='blabla').first() - primu
>>> from polls.models import Choice  # legam choice de intreabre 
> q = QUestion.objects.get(id=1)
> c1 = Choice(question=q, choice_text='OK) pentru ca am folosit foreignkey in models acumn orice c catre q va 
contine toate c,c1,c2 ce le definesc
> c1.save()
> Relatia inversa ( de la question la choice) va fi denumita choice_set (adica numele modelului curent + '_set') 
q.choice_set, q.choice_set.all() django ne returneaza modele ca nume obbiect , pentru a da nume putem face in models def __str__

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

Template-urile pentru o aplicatie se vor pune in folderul `<nume app>/templates/<nume app>` - (polls/templates/polls/index.html).
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


### For deploy :
python manage.py collectstatic

pip install gunicorn

pip install whitenoise  ( pentru a functionaza static si media in DEBUG= False)

pentru whitenoise :

- add 'whitenoise.middleware.WhiteNoiseMiddleware',  in MIDDLEWARE - settings.py
- add STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' settings.py
- in urls add: so media file works  - re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT, }, ), urls.py

pentru restu pentru a citi static , in urls

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

in settings.py 
TEMPLATES -  'DIRS': [BASE_DIR, 'templates'],
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# for deploy on web
# CSRF_TRUSTED_ORIGINS = ['*']
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')