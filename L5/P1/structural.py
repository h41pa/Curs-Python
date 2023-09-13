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

# Composite

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = [] # children pot fi ori alte foldere, ori fisiere

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
            child.print_structure(level+1)



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