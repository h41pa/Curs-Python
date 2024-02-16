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


# c1 si c2 sunt obiecte DIFERITE, adica au ID-uri diferite, si se afla in locatii de memorie diferite.
c1 = Car()
c2 = Car()
print(id(c1))
print(id(c2))
print(c1 == c2)

#  ------------- Singleton -------------
class SingletonLogger:
    __instance = None  # atributul de clasa __ instance va actiona ca un "obiect" fals
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
print(obj2.creat)

print('-' * 80)


# -------------Factory -------------

# Definirea interfetei comune pentru obiecte create
class Animal:
    def speak(self):
        pass


# Implementare a claselor concrete care implementează interfata
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Factory pentru crearea obiectelor bazate pe un anumit criteriu
class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")


# Utilizarea Factory pentru a crea obiecte
animal_factory = AnimalFactory()

dog = animal_factory.create_animal("dog")
cat = animal_factory.create_animal("cat")

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

print('-' * 80)

#------------------------------------------------------------------------------


#  ------------- Object Pool -------------

class ObjectPool:
    def __init__(self, object_type, max_objects):
        self.object_type = object_type
        self.max_objects = max_objects
        self.available_objects = []
        self.in_use_objects = []

    def create_object(self):
        if not self.available_objects and len(self.in_use_objects) < self.max_objects:
            # Creează un nou obiect dacă nu există obiecte disponibile
            new_object = self.object_type()
        else:
            # Ia un obiect disponibil din pool
            new_object = self.available_objects.pop()

        # Adaugă obiectul la lista de obiecte în uz
        self.in_use_objects.append(new_object)
        return new_object

    def release_object(self, obj):
        # Eliberează obiectul înapoi în pool
        self.in_use_objects.remove(obj)
        self.available_objects.append(obj)


# Exemplu de utilizare cu o clasă de obiecte simplă
class SimpleObject:
    def __init__(self):
        pass


# Creare un pool de obiecte SimpleObject cu o capacitate maximă de 5 obiecte
simple_object_pool = ObjectPool(SimpleObject, max_objects=5)

# Utilizare
obj1 = simple_object_pool.create_object()
obj2 = simple_object_pool.create_object()

# Eliberare obiecte înapoi în pool
simple_object_pool.release_object(obj1)
simple_object_pool.release_object(obj2)

print('-' * 80)
#-----------------------------------------------------------------


# ------------- Prototype -------------

import copy

class Prototype:
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def __init__(self, data):
        self.data = data

    def clone(self):
        # Utilizăm copy.deepcopy() pentru a clona obiectul în mod recursiv
        return copy.deepcopy(self)


# Exemplu de utilizare:
# Creăm un prototip
prototype_object = ConcretePrototype(data="Initial data")

# Clonăm obiectul
cloned_object = prototype_object.clone()

# Modificăm datele obiectului clonat
cloned_object.data = "Modified data"

# Afișăm datele ambelor obiecte
print("Original Object:", prototype_object.data)
print("Cloned Object:", cloned_object.data)
print(id(prototype_object))
print(id(cloned_object))

print('-' * 80)
#-----------------------------------------------------------------


# ------------- Builder  -------------

# Produsul final care va fi construit
class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show(self):
        print("Produsul construit:")
        for part in self.parts:
            print(part)


# Interfața pentru Builder
class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_result(self):
        pass


# ConcreteBuilder - Implementează Builder pentru a construi un anumit tip de produs
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("Part A")

    def build_part_b(self):
        self.product.add_part("Part B")

    def get_result(self):
        return self.product


# Director - Coordonatorul care utilizează Builder pentru a construi un produs specific
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()


# Exemplu de utilizare:
builder = ConcreteBuilder()
director = Director(builder)

director.construct()
product = builder.get_result()
product.show()
