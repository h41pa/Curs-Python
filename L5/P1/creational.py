"""
Creational Design Patterns


Factory => folosit atunci cand avem mai multe clase cu o implementare comuna, care pot fi folosite
interschimbabil in cod (ex UserFactory => User de tip admin sau un user regular, in functie de cine face login
intr-un sistem). In general, Factory se foloseste impreuna cu Inheritance sau Abstraction.

Abstract Factory,
Builder,
Singleton,
Object Pool => folosit in situatii in care avem o clasa X la care crearea (instantierea) de obiecte este
foarte heavy dpdv computational. In cazul acesta, avem o alta clasa ClassXPool, care instantiaza la inceputul
rularii o multitudine de obiecte din clasa X, iar noi atunci cand avem nevoie de un asemenea obiect,
primim deja unul creat.
Ex. : putem avea pools atunci cand trebuie sa comunicam cu alte sisteme
(cum ar fi comunicarea cu bazele de date)

Prototype = folosit cand avem mai multe obiecte similare, si vrem sa le clonam, dar nu stim exact 100%
ce atribute si functionalitati are fiecare dintre ele. Asa ca folosim o interfata (clasa abstracta in Python)
prin care "fortam" clasele acestor obiecte sa defineasca o metoda de clone/copy.

1. Singleton = design pattern care ne permite sa avem o clasa care mereu returneaza aceeasi instanta unica.
De obicei il folosim in situatii in care nu ne intereseaza obiectul in sine, ci doar anumite functionalitati
(metode) ale acestuia.

Exemplu: cand avem un logger pentru un proiect (adica o clasa care scrie informatii despre felul in
care ruleaza un sistem in timp real in niste fisiere speciale numite loguri care au de obicei extensia .log)

"""
# Singleton

class Car:
    def __init__(self):
        pass

#c1 si c2 sunt obiecte DIFERITE, adica au ID-uri diferite, si se afla in locatii de memorie diferite.
c1 = Car()
c2 =  Car()
print(id(c1))
print(id(c2))
print(c1 == c2)

class SingletonLogger:

    __instance = None # atributul de clasa __ instance va actiona ca un "obiect" fals
    # pe care noi il putem returna de fiecare data cand se incearca crearea unui nou obiect din aceasta clasa

    """
        Functia init in Python nu este chiar constructorul de-facto, ci este un initializator.
        Inainte de aceasta functie, este de fapt apelata functia __new__, unde se creaza un obiect in realitate.
    """

    def __new__(cls, *args, **kwargs):
        # Functia new nu are self ca si prim argument, pentru ca self inca nu exista la moment de runtime
        # In schimb, avem cls ca prim argument, care este de fapt clasa curenta
        if cls.__instance is None:
            # prima data cand este cerut un nou obiect, trebuie sa il cream
            cls.__instance = object.__new__(cls)
        # Apoi il returnam, acelasi obiect de fiecare data
        return cls.__instance

print('_' * 80)

s1 = SingletonLogger()
s2 = SingletonLogger()
s3 = SingletonLogger()

print(id(s1))
print(id(s2))
print(id(s3))
# s1, s2, si s3 sunt de fapt acelasi obiect, ADICA referinte catre acelasi loc in memorie

print(s1 == s2)

s1.create = 'DEBUG'
print(s2.create)

print('_' * 80)

# singleton folosing decorator
def singleton(cls):
    instances = {}



    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class SingletonClass:
    def __init__(self):
        pass

# Utilizare:
obj1 = SingletonClass()
obj2 = SingletonClass()
obj1.creat = 'Test'
print(obj2.creat )