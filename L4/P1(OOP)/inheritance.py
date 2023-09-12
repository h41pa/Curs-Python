"""
Mostenire = avem o clasa parinte, si clase copil, iar clasele copil mostenesc atributele
si metodele de la parinte.

Mostenirea se foloseste de obicei cand avem mai multe clase care au elemente comune (atribute, metode),
si nu vrem sa repetam codul comun aiurea.

class Parent:
    ....

class Child(Parent):
    ....


In general, ne referim la clasa parinte ca si superclass, iar clasele copil sunt subclasses.
De aceea, cand avem nevoie de o metoda din parinte, vom folosi sintaxa cu super()

Pentru a cauta o metoda sau un atribut, Python se uita intai in clasa curenta, apoi in parinte,
bunic, strabunic, etc. Nu exista limitare la numarul de nivele pe care se poate face mostenirea.
"""

class Vehicle:

    def __init__(self, nr_wheels, color, doors_cnt):
        self.nr_wheels = nr_wheels
        self.color = color
        self.doors_cnt = doors_cnt

    def drive(self):
        print("I'm driving, and I'm a vehicle!")

    def describe(self):
        print(f"I'm a {self.color} vehicle, I have {self.nr_wheels} wheels, {self.doors_cnt} doors.(!)")


class Car(Vehicle):
    def __init__(self, color, doors_cnt):
        super().__init__(4, color, doors_cnt)

    def describe(self):
        print("I'm a car, I go vruuum")


class RedCar(Car):
    def __init__(self, doors_cnt):
        super().__init__('red', doors_cnt)


class BlueCar(Car):
    def __init__(self, doors_cnt):
        super().__init__('blue', doors_cnt)

    def describe(self):
        print("I'm a blue car, I go vrum vrum vrum!")


class Motorcycle(Vehicle):
    def __init__(self, color, needs_license=True):
        super().__init__(2, color, 0)
        # Pe langa atributele comune intre copii, fiecare dintre acestia poate avea si atribute extra
        self.needs_license = needs_license

    def describe(self):
        # Cand facem o metoda in interiorul clasei copil identica cu cea din clasa parinte,
        # zicem ca SUPRASCRIEM metoda (override)
        super().describe()  # cu super() apelam practic metoda cu acelasi nume din clasa parinte
        print(f"Do you need a license to drive me? {self.needs_license}")


class Truck(Vehicle):
    def __init__(self, color):
        super(Truck, self).__init__(16, color, 2)


v = Vehicle(4,'blue',4)
c = Car('black', 4)
m = Motorcycle('Red')
t = Truck('Yellow')
v.describe()
c.describe()
m.describe()
t.describe()

red_car = RedCar(2)
red_car.describe()

blue_car = BlueCar(4)
blue_car.describe()

