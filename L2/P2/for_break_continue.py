"""
Putem controla iteratiile noastre folosind doua cuvinte cheie:
- break (rupe) => opreste tot for-ul, si nu se mai trece la vreo alta iteratie
- continue (continua) => opreste iteratia curenta si trece mai departe (practic, sarim peste o iteratie)
"""

print('Inainte de for')
for nr in range(1, 10):     # 1, 2, 3, 4, 5, 6, 7, 8, 9
    if nr == 5:
        # vom opri for cand ajunge la valoarea 5
        break
    print(f'Numarul curent este {nr}')
print('Dupa for')
print('_' * 80)

for nr in range(10):
    print(f' Testam daca numarul {nr} Este par?')
    if nr % 2 == 1:
        continue # daca numarul este impar sarim peste
    print(f'Numar par : {nr}')

print('AM terminat de verificat numerele !')

print('_' * 80)
students = ['Adela', 'Anastasia', 'Diana', 'Petru', 'Ana Maria', 'Roxana', 'Ionut', 'Alin']
for name in students:
    if name[0] != 'A': # daca prima litera a numelui NU este A
        continue # trecem mai departe
    print(f'Numele persoanei este {name}')

"""
Exercitiu: am o lista de numere, si vreau sa gasesc un numar negativ in lista (oricare)
DACA nu exista nici un numar negativ, vreau sa mi se afiseze asta

Vom folosi sintaxa for-else, care functioneaza asa:
else va fi apelat doar daca tot FOR-ul a rulat normal, si nu a ajuns niciodata la vreun break
"""

print('_' * 80)
numbers = [1, 4, 5, 10, -12, 100, 0, 1, 23, 27]

for numar in numbers:
    if numar < 0:
        print(f'AM gasit numar negativ {numar}')
        break
    print('Nu am gasit inca un numar negativ mai cautam')
else: # nobreak
    # vom ajunge aici doar daca nu am avut break in for-ul anterior
    print('Nu am gasit nici un numar negativ')





