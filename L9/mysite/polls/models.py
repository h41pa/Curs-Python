from django.db import models

# Create your models here.

from django.db import models

"""
Fiecare model va fi o clasa care extinde (mostenire) clasa models.Model,
si care contine atributele pe care dorim sa le punem noi in tabela modelului nostru.

Un atribut reprezinta o coloana din tabela SQL, si se numeste Field.
Definim aceste fields folosind clase existente in Django, precum:
- CharField -> va face in SQL un VARCHAR
- DateTimeField -> va face un DATETIME
- IntegerField
- BooleanField

Pentru relatii, este la fel de simplu, adaugam din nou niste atribute, doar ca pe acestea le legam de alte modele:
- ForeignKey -> defineste o relatie de genul 1-to-many, adica o intrebare (Question) are mai multe optiuni de raspuns (Choice)
- OneToOneField -> defineste o relatie de genul 1-to-1
- ManyToManyField -> defineste o relatie de genul many-to-many, de exemplu Product si Order (un produs se poate regasi
    in mai multe comenzi, iar o comanda poate avea mai multe produse).
"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)    # VARCHAR cu limita de 200 caractere
    pub_date = models.DateTimeField("date published")   # DATETIME cu data publicarii

    def __str__(self):
        # str este reprezentarea sub forma de string a unui obiect
        return self.question_text


class Choice(models.Model):
    # FK catre Question, deoarece un Choice poate sa fie doar pentru un Question
    # on_delete = stabileste comportamentul acestui model atunci cand noi stergem modelul referentiat
    # CASCADE = stergem si modelul curent (adica daca se sterge intrebarea, stergem si toate variantele de raspuns)
    # Relatia inversa ( de la question la choice) va fi denumita choice_set (adica numele modelului curent + '_set')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # VARCHAR cu limita de 200, aici avem textul raspunsului
    choice_text = models.CharField(max_length=200)
    # numarul de voturi, INT, default 0 ca sa il putem incrementa
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
