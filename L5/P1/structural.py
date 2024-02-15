"""
Structural Design Patterns

Adapter
Bridge
Composite = folosit pentru a crea o ierahie de obiecte, in care obiectele au atribute si functionalitati
comune, dar au si o relatie de genul copil-parinte intre ele. Cele mai de la baza obiecte se numesc Leaf (frunze)
deoarece atunci cand folosim design pattern Composite, structura acestor obiecte va arata ca un arbore.
Ex1 : locatii (avem tara, judet, municipiu, oras, comuna, sat, etc) -> fiecare dintre aceste locatii
are un nume, coordonate GPS, populatie, etc. DAR in acelasi timp avem si o relatie intre acestea,
deoarece tara are mai multe judete, fiecare judet are orase si comune, samd.

Ex2 : categorii intr-un magazin virtual:
    Electrocasnice
        Mari
            Frigidere
            Masini de spalat
        Mici
            Toaster
            Cuptoare microunde
                Incorporabile   -> Leaf, adica nu mai exista alte subcategorii
                Normale
        Personale
    Alimente
        Fructe Legume
        Conserve


Decorator = folosit pentru a augmenta functionalitatea unei metode/functii, in Python avem decoratorii
cu sintaxa @something pe linia de dinaintea functiei pe care vrem sa o "decoram"
Acesti decoratori sunt apelati inainte de functia propriu zisa, si ne pot oferi informatii extra despre aceasta.

Facade
Flyweight
Private Class Data

Proxy = folosit atunci cand vrem sa avem un wrapper pentru un anumit serviciu, care sa faca anumite
pre-procesari sau post-procesari necesare pentru utilizarea serviciului respectiv.
In general se foloseste atunci cand vorbim despre web, si despre conexiuni prin retea.

"""


# ------------ Composite ------------

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []  # children pot fi ori alte foldere, ori fisiere

    @property
    def size(self):
        total_size = 0
        for obj in self.children:
            total_size += obj.size
        return total_size

    def add_child(self, child):
        self.children.append(child)

    def delete_child(self, child):
        self.children.remove(child)

    def print_structure(self, level=0):
        print('\t' * level, f'Folder {self.name} - {self.size} KB')
        for child in self.children:
            child.print_structure(level + 1)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def print_structure(self, level):
        print('\t' * level, f'File {self.name} - {self.size} KB ')


root = Folder('root')
a = Folder('a')
b = Folder('b')
root.add_child(a)
root.add_child(b)

f1 = File('Ceva.txt', 100)
f2 = File('Altceva.txt', 50)
a.add_child(f1)
b.add_child(f2)

f3 = File('blabla', 80)
f4 = File('wewew', 90)
c = Folder('C')
b.add_child(f3)
b.add_child(f4)
b.add_child(c)
f5 = File('Ending', 123)
c.add_child(f5)

print(root.size)
root.print_structure()

# ------------ Composite ------------

from abc import ABC, abstractmethod

# Component - Interfața pentru toate obiectele (individuale și compuse)
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Leaf - Obiectul individual care implementează Component
class Leaf(Component):
    def operation(self):
        print("Executând operația într-un obiect Leaf.")

# Composite - Obiectul compus care poate conține alte obiecte (Composite sau Leaf)
class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        print("Executând operația într-un obiect Composite.")
        for child in self.children:
            child.operation()

# Exemplu de utilizare:
leaf1 = Leaf()
leaf2 = Leaf()

composite = Composite()
composite.add(leaf1)
composite.add(leaf2)

composite2 = Composite()
composite2.add(composite)

# Apelând operația pe obiectele individuale și compuse
leaf1.operation()
print("------")
composite.operation()
print("------")
composite2.operation()




# --------------------------------------------------------------------------------------------------------------

print('-' * 80)


# ----------- Proxy -----------

# Interfața pe care Proxy-ul și RealSubject-ul trebuie să o implementeze
class Subject:
    def request(self):
        pass


# RealSubject - Clasa reală care realizează funcționalitățile efective
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Cerere efectuată.")


# Proxy - Înlocuiește RealSubject, controlează accesul sau adaugă funcționalități suplimentare
class Proxy(Subject):
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        # Putem adăuga logica de control al accesului sau funcționalități suplimentare aici
        print("Proxy: Controlul accesului înainte de a efectua cererea.")
        self.real_subject.request()
        print("Proxy: Funcționalitatea suplimentară după cerere.")


# Exemplu de utilizare:
real_subject = RealSubject()
proxy = Proxy(real_subject)

# Accesăm funcționalitatea prin intermediul Proxy-ului
proxy.request()

# --------------------------------------------------------------------------------------------------------------

print('-' * 80)


# ----------- Adapter -----------

# Interfata Target (cea la care vom adapta)
class Target:
    def request(self):
        pass

# Clasa Adaptee (cea pe care dorim să o adapăm)
class Adaptee:
    def specific_request(self):
        print("Metoda specific_request a clasei Adaptee.")

# Adapterul care convertește interfața Adaptee în interfața Target
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        print("Adapterul transformă apelul la request într-un apel la specific_request.")
        self.adaptee.specific_request()

# Exemplu de utilizare:
adaptee = Adaptee()
adapter = Adapter(adaptee)

# Apelăm metoda request pe interfața Target, iar aceasta va utiliza Adaptee prin intermediul Adapterului
adapter.request()

# --------------------------------------------------------------------------------------------------------------

print('-' * 80)


# ----------- Private Class Data -----------

class PrivateData:
    def __init__(self):
        self._private_data1 = None
        self._private_data2 = None

    def set_data(self, data1, data2):
        self._private_data1 = data1
        self._private_data2 = data2

    def get_data(self):
        return self._private_data1, self._private_data2


class MyClass:
    def __init__(self):
        self._private_data = PrivateData()

    def set_data(self, data1, data2):
        self._private_data.set_data(data1, data2)

    def get_data(self):
        return self._private_data.get_data()


# Exemplu de utilizare:
obj = MyClass()

obj.set_data("Info1", "Info2")

data1, data2 = obj.get_data()
print(f"Data1: {data1}, Data2: {data2}")


# --------------------------------------------------------------------------------------------------------------