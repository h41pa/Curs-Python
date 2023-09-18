"""
Python:
modul = in general, un modul este un fisier cu extensia .py (adica un cod pe care noi il putem rula cu
    python nume_modul.py)
    => putem folosi codul din acest modul SI in alte fisiere, folsind sintaxa de import

Import : folosirea unui cod dintr-un loc extern in fisierul nostru curent. Avem mai multe optiuni de a folosi importul

from modul import ceva  => aici, importam dintr-un modul doar <ceva> (care poate fi o variabila, o functie, o clasa)
from modul import *     => steluta insemna ca din acel modul importam TOATE elementele (toate var, func, clasele)
import modul            => la fel ca si mai sus, importam TOT din modul, DAR de data aceasta ne referim altfel in
                            interiorul fisierului nostru
"""

# from my_module import a,my_func
# from my_module import *
# print(a)
# my_func()
# mc = MyClass()

# import my_module
# import my_other_module
# # aici trebuie sa folosim notatia cu punct ca sa accesam elemente din my_module
#
# print(my_module.a)
# my_module.my_func()
# my_other_module.my_func()
# module.submodulA.submodulC.functia_mea()


"""
Alias import:
- uneori dorim sa importam elemente din alte module care au acelasi nume
- in cazul acesta, ultimul import va fi cel luat in considerare
- daca nu ne dorim asta (suprascriere) avem posibilitatea sa importam un element sub un alt nume, folosind
    sintaxa de alias import

- uneori folosim alias imports ca sa scurtam unele nume importate, sau ca sa evitam conflicte de cod

Putem aliasa si numele de modul, adica putem face:
import my_module as mm
iar mai departe in cod sa il folosim sub aceasta forma (e.g. mm.my_func() )

"""

from my_module import my_func as my_func1
from my_other_module import my_func as my_func2

my_func1()
my_func2()

import my_module as mm
print(mm.a)