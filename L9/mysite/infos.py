
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

###   -  ca sa facem o interfata html la site , django are o interfata html ,
template tags doar pentru asta, ca fisierele html in mod normal sunt statice
Pentru a putea avea niste raspunsuri HTML din views, folosim engine-ul de templates integrat in Django.
Acesta ne permite sa facem fisiere HTML dinamice (adica care sunt generate la runtime) prin prezenta unor
structuri speciale numite template tags.
Template-urile pentru o aplicatie se vor pune in folderul `<nume app>/templates/<nume app>`  - (polls/templates/polls/index.html)..
 - Trebuie sa creeam noi folderul templates in myapp , facem folderul templates, dupa care mai facem un folder cu numele app si adauga html aici

 #- Pentru a folosi aceste templetase trebuie sa le incarcam in views:
- in views.py ,  from django.template import loader   (importam un loader) ( index_logn example)
- apoi facem   template = loader.get_template("polls/index.html") ( trebuie sa ii dam path, numeappsi html )
-  pentru a pasa templete ului lista de intrebuie trebuie sa face un context, este un disctionar, un care spune cum se numeste si valoarea din view
context = {
        "latest_question_list": latest_question_list,
    }
- trebuie sa returna un raspuns dupa aceea:
# returnam un HTTP response (200) care randeaza template-ul index.html folosind contextul de mai sus
# template.render(context, request) => aceasta este partea care transforma template-ul intr-un fisier HTML pur
         return HttpResponse(template.render(context, request))

### varinata long

def index_long(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # Incarcam template-ul facut de noi, folosind path-ul acestuia
    template = loader.get_template("polls/index.html")
    # Contextul ne ajuta sa trimitem informatii din view catre template
    # acesta este de fapt doar un dictionar, in care cheia este numele pe care il vom folosi in template
    # iar valoarea este ceea ce vrem noi sa trimite (de obicei o variabila)
    context = {
        "latest_question_list": latest_question_list,
    }
    # returnam un HTTP response (200) care randeaza template-ul index.html folosind contextul de mai sus
    # template.render(context, request) => aceasta este partea care transforma template-ul intr-un fisier HTML pur
    return HttpResponse(template.render(context, request))

----   **** de asemenea django ofera posibilitatea de scurta randarea unui template prin: _______
        render(request, <nume template>, context)
# varianta short
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }

    # Shortcut pentru randarea unui template:
    # render(request, <nume template>, context)
    return render(request, "polls/index.html", context)

mai pot scri si gen :   return render(request, "polls/index.html", {"latest_question_list": latest_question_list}) ,
direct dicitionarul context
{}{}{}    {}{}{}    {}{}{}    {}{}{}    {}{}{}

Exception handling in django folosing try:
from django.http import HttpResponse, Http404, HttpResponseRedirect
    try:
        q = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        # Tratam cazul in care intrebarea cu ID-ul cerut nu exista
        raise Http404("Question does not exist")

### un shortcut pt getobejct sau 404 ar fi :
from django.shortcuts import render, get_object_or_404

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

echivalent cu doar ca nu mai trebuie sa face exeception cum e mai jos: ( mai exista si  get_list_or_404() )
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


pentru a itera prin toate variantele de raspuns pentru o intrebare ne folosim de question.choice_set.all  - detail.html
pentru a putea vota trebuie folosit un form , vezi detail.html si views.py
shorting url in html mai rapid :
<a href="{% url 'detail' question.id %}">{{ question.question_text }}
<a href="/polls/{{ question.id }}">{{ question.question_text }}
In djnago folosim <form action= >  </form> de fiecare daca in form trebuie sa folosim {% csrf_token %} - sau nu va functiona
{# form = formular care face un POST catre URL-ul definit in action #}
<form action="{% url 'polls:vote' question.id %}" method="post">
ca sa mearga in html 'polls:vote' trebuie adaugat  app_name = "polls" in urls.py local

<filedset> ne ajuta grupa mai multe campuri

"""

"""
mereu la if trebuie mereu incheiat  {% endif %} {% endfor %}
{% if conditie %}  , pentru a afisa data {{ question.question_text }}
{# asa punem comentarii in template-urile Django #}   
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

-----------------------------------------------------
{# asa punem comentarii in template-urile Django #}

{% if latest_question_list %}
    <ul>  {# ul este unordered list #}
    {% for question in latest_question_list %}
        {# li = list item, a = link # -  a are un href - un link unde sa ne duca}
        <li>
            {# /polls/{{ question.id }} se va evalua ca /polls/1 , /polls/2 , etc. # }
            { - for loop prin lista noastra de intrebari si va geenra u link ca va fi afisat ca si textul intrebarii {{ question.question_text }}
             iar linkul ne va duce la /polls/{{ question.id }}}
            <a href="/polls/{{ question.id }}">{{ question.question_text }}</a>
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}


"""

