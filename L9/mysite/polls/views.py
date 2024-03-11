from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question, Choice


def index_old(request):
    # Question.objects = object manager care ne ajuta sa interogam baza de date
    # order_by("-pub_date") = se va transforma in ORDER BY pub_date DESC
    # (faptul ca avem minus in fata lui pub_date il face desc)
    # [:5] = list slicing, va scoate doar primele 5 rezultate, iar in SQL asta se traduce prin LIMIT 5
    # Deci latest_question_list va contine ultimele 5 poll-uri adaugate in DB
    latest_question_list = Question.objects.order_by("-pub_date")[:3]
    # [q.question_text for q in latest_question_list]
    # Conceptul de mai sus se numeste list comprehension (compresie de lista) si este o forma mai scurta de a scrie:
    """
    l = []
    for q in latest_question_list:
        l.append(q.question_text)
    """
    # Astfel, in acesta lista vom avea stringurile care reprezinta textul fiecarei intrebari din cele 5 luate din db
    # "\n ".join(list) uneste toate elementele din lista, folosind "\n " intre ele
    # "\n " = caracterul newline
    output = "\n ".join([q.question_text for q in latest_question_list])
    # aici returnam raspunsul, care by default o sa aiba status code 200 (SUCCESS)
    return HttpResponse(output)

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

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }

    # Shortcut pentru randarea unui template:
    # render(request, <nume template>, context)
    return render(request, "polls/index.html", context)

"""
Pentru views in care avem parametrii dinamici (ex. id unei intrebari),
acest parametru va fi injectat din URL direct ca si argument in functia noastra de view

In URL trebuie sa avem o structura de tipul <tip param:nume param>, exemplu:
<str:name> 
"""
def hello(request, name):
    return HttpResponse(f"Hello, {name}, how are you?")


def detail_with_try_except(request, question_id):
    # Aici vrem sa vedem detaliile unei intrebari, deci prima data trebuie sa o luam din baza de date
    try:
        q = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        # Tratam cazul in care intrebarea cu ID-ul cerut nu exista
        raise Http404("Question does not exist")
    # Apoi trebuie sa ii pasam template-ului nostru obiectul de question
    context = {
        'q': q
    }
    # In final, randam template-ul si il returnam ca si raspuns
    return render(request, "polls/detail.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


"""
In tutorial, aici mai erau niste pasi de exception handling, dar au fost omisi pentru simplicitate.
"""
def vote(request, question_id):
    # Pentru a putea vota, prima data preluam intrebarea pe care s-a votat
    question = get_object_or_404(Question, pk=question_id)
    # Apoi luam din form optiunea selectata
    selected_choice_id = request.POST['choice']
    # Acum trebuie sa luam optiunea selectata ca si obiect din baza de date
    selected_choice = get_object_or_404(Choice, pk=selected_choice_id)
    # Incrementam numarul de voturi pentru optiunea selectata
    selected_choice.votes += 1
    # IMPORTANT: salvam modificarile in baza de date!!
    selected_choice.save()
    # Calculam url-ul de redirectionare (catre pagina de rezultate)
    redirect_url = reverse("polls:results", args=(question.id,))
    # Redirectam utilizatorul catre pagina de results dupa votarea cu succes
    return HttpResponseRedirect(redirect_url)
