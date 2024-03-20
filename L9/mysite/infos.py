
"""

Cum incepem?

Avem comenzi CLI, printre care:
### - startproject: `django-admin startproject <nume proiect>` -- va crea structura de foldere si fisiere necesara pentru proiectul nostru

Dupa ce am facut un proiect, putem porni direct serverul, schimband path-ul in folderul <nume proiect>,
si ruland comanda:
### python manage.py runserver`

Apoi, putem incepe sa cream aplicatii (apps) cu comanda:
### `python manage.py startapp <nume app>`


###  dupa start app - in cazul me polls = app
- creem fisier urls.py  in folder "app" trebuie facut in fiecare app(daca avem mai multe), definim urlpatterns(mapeaza url)
dupa trebuie importat app/urls.py in  in mysite.urls(pagina cu setarile site-ului) si folosim functia include() in urlpatterns
path("app/", include("app.urls"), name='app'),
 - name="index" folosit la redirect si etc.
 - dupa ce cream o functie in app/view.py , ne duce in app/urls.py adauga in url patternspath("numefunctie", views.numefunc, name="hello")
 - view.py de asemena contine paginile create pe care le adaugam in urls

pentru baza de date
### - `python manage.py migrate` -- migrate aduce baza de date la zi cu modificarile din cod, adica updateaza tabelele
    sa corespunda cu modelele Python. Acest lucru se intampla prin niste fisiere speciale, numite migrations.

de aceea avem folderele migrations in toate apps , in care se tin migrarile
### - `python manage.py makemigrations` -- aceasta comanda genereaza fisierele mentionate mai sus din codul nostru Python.

daca adaugam tabela noua gen avem deja tabela user si mai adaugam una pentru products in cod python . cream clasa dupa care folosim
python manage.py makemigrations, generam fisierele infolder migrations dupa care folosim comanda python migrate.py
pentru a executa pe baza de date pentru a fi sincronizata ,astfel orice care lucreaza pe acest proiect lucreaza pe aceeasi baza de date

 -  ne duce im fisierul app/models.py , pendru a crea modelele pentru baza de date/

 - Pentru a putea genera fisiere de migrari, app noastra trebuie sa fie adaugata in settings.py, in `INSTALLED_APPS`.
"polls.apps.PollsConfig" adaugam acolo  numele clasei,  vedem in app/apps.py numele
- am facut modificari acum folosim python "manage.py makemigrations" , ne arata ca intr un folder a facut ceva modificari
in consola daca incerca sa dam run server apaare unapplied mmigrations. "OPRIM SERVERUL" si facem comanda de migrare "python manage.py migrate"

INTOTDEAUNA CAND FAC MODIFICARI IN MODEL TREBUIE FACUTE ACESTE OPERATII:
"python manage.py makemigrations" - care genereaza fisierele pentru migrari si
"python manage.py migrate" - se folosesti sic and alte persoane fac modificari pe proiect

next:
### - `python manage.py shell` - vezi in readme(shell si qurries db) pt a crea db objects din consola

###  - `python manage.py createsuperuser` - creare superuser si face direct din panel puteam adauga si sterge etc ,
http://127.0.0.1:8000/admin
Pentru a putea vedea modelele create de noi in interfata de admin, trebuie sa le inregistram (adica in folderul app noastre,
in fisierul admin.py, trebuie sa apelam functia register cu numele modelului).

### - in app/admin.py inregistram modelele cu register
from .models import Question, Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

####   CREATING MORE VIEWS(PAGES) -   in app/views.py cu paramatri .
Pentru views in care avem parametrii dinamici (ex. id unei intrebari),
acest parametru va fi injectat din URL direct ca si argument in functia noastra de view
In URL trebuie sa avem o structura de tipul <tip param:nume param>, exemplu: --- <str:name> ---

 -  adaugam o functie in views. si ne ducem in app/urls.py si adaugam in url patterns path("hello/<str:name>", views.hello, name="hello")
atentie in url <str:name> numele parametru trebuie fie exact ca cel din din views.py ex :
--- path("<int:question_id>", views.detail, name="detail")---
nu mai e nevoie sa ne ducem si in mysite/urls.py adica url globals ca deja am adauga calea de la inceput catre ppols

  -  pentru pagini in views unde trebue sa interogam din baza de date ne folosim de
"Nume.objects. (comenzile, get, order , etc)" vezi in views.py - index_old  - Question.objects.order_by("-pub_date")[:3]
   intotdeauna trebuie la fiecare functie/view sa returnam un HttpResponse


"""

"""

"""

