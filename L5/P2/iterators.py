"""
Iterator = un obiect care poate fi iterat. In general, in Python avem colectii iterabile.
Exemple din Python : list, tuple, dict, set, string.

Orice clasa  care este iterabila(adica practic o putem parcure cu for ... in ...) Trebuie sa implementeze 2 metode:

def __iter__(self):
    -> aici se initializeaza un iterator, adica se foloseste de obicei o variabila
        in care se poate tine iteratia curenta
    self.contor = 0

def __next__(self):
    -> aici se va returna mereu urmatoarea valoare din colectia iterabila
    self.contor += 1
    return lista[self.contor]

    -> atunci cand nu mai sunt valori disponibile, metoda next trebuie sa arunce exceptia StopIteration

Aceste 2 metode sunt apelabile din exterior, folosind varianta fara underscores( adica iter() si next() )


"""

l = list([1, 4, 5, 100])
my_iterator = iter(l) # creez un iterator

print(next(my_iterator)) # va printa 1
print(next(my_iterator)) # va printa 4
print(next(my_iterator)) # va printa 5
print(next(my_iterator)) # va printa 100
# print(next(my_iterator)) # # va arunca exceptia StopIteration

"""
Orice clasa care implementeaza cele 2 metode mentionate devine automat iterabila.
Astfel, putem sa ne construim proprii iteratori la nevoie.
Pe langa folosirea lui next, putem sa iteram un iterator folosind for (care este implementat tot cu next())
"""
class AlphabetIterator:
    def __iter__(self):
        self.letter = 'A'
        return self

    def __next__(self):
        current_letter = self.letter
        if current_letter == 'Z':
            raise StopIteration
        self.letter = chr(ord(self.letter) +1)
        return current_letter

alphaiter = iter(AlphabetIterator())
print(next(alphaiter))
print(next(alphaiter))
print(next(alphaiter))

for i in alphaiter:
    print(i)
print('#' * 60)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

