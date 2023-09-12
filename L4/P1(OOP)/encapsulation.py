"""
Encapsulation = notiunea de a tine toate atributele si metodele relevante pentru un obiect in clasa
acestuia, si de a le afisa/ascunde in functie de nevoi.

Avem 3 tipuri de modificatori care ne dau vizibilitatea atributelor si metodelor:

- privat : atribute si metode care NU sunt deloc vizibile in afara clasei in care sunt definite
   acestea incep cu dublu underscore __
- protected : atribute si metode  care sunt  vizibile doar in clasa curenta si in clasele care o mostenesc
   pe cea curenta; acestea incep cu un singur underscore => acesta este doar in standard
- public : atribute si metode vizibile de oriunde

"""

class Person:
    def __init__(self, cnp, name, age, height):
        self.__cnp = cnp # atributul __cnp este privat, adica NU il putem citi si nici scrie din afara clasei
        self._name = name # atributul _name este "protected", adica nu ar trebui sa il accesam decat din clasele copil
        self.age = age
        self.height = height

    def describe(self):
        print(f'{self.__cnp} : {self._name}, {self.age} ani, {self.height}m')

       # acesta este un "getter" deoarece expune valoarea privata in afara clasei
    @property # decoratorul property imi transforma o metoda in atribut
    def cnp(self):
        print('This is a getter !')
        return  self.__cnp


       # "setter" = metoda care ne permite sa scriem o valoare intr-un atribut privat.

    @cnp.setter  # nume_atribut.setter va face aceasta metoda sa actioneze ca un setter
    def cnp(self, new_cnp):
        print('This is a setter !')
        if len(new_cnp) == 13:
            self.__cnp = new_cnp
        else:
            print("Invalid CNP value, should be 13 chars long.")

    def __private_method(self):
        pass

    # Doar pentru atributele definite cu @property putem avea setter si deleter
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # Va fi apelat atunci cand incercam sa stergem proprietatea name folosind del
    @name.deleter
    def name(self):

        print("Trying to delete name, not possible")




mada = Person('1234567890123', 'Mada', 18, 1.88)
mada.describe()
print(mada.cnp)
# print(mada.__cnp) #  # va da AttributeError: 'Person' object has no attribute '__cnp'
mada.__cnp = 'cnp nou'   # nu va modifica __cnp, deoarece nu il poate "vedea"
mada.describe()
# AttributeError: 'Person' object has no attribute '__private_method'. Did you mean: '_Person__private_method'?
# mada.__private_method()

print('_' * 80)

print(mada.name, mada._name)  # va afisa numele, dar nu ar trebui sa accesam in felul acesta
mada.name = 'New Name'
mada.describe() # va merge, dar nu ar trebui sa facem asa.

print('*' * 80)
# In mod normal, putem sterge un atribut de pe un obiect folosind del
# del mada.name
# mada.describe()

