
"""
While (cat timp) = bucla (loop) iterativa in care un cod se executa CAT TIMP
o anumita conditie este adevarata
while <conditie>:
    fa ceva
    fa altceva
    samd

"""
"""
Presupunem ca utilizatorul va introduce varsta corecta (adica un numar) => True
Daca varsta chiar este corecta (numar), oprim bucla repetitiva, altfel continuam.
"""

while True:
    age = input("Introdu varsta:\n")
    if age.isdigit():
        break
print(f'Varsta este {int(age)}')

"""
Cerem input de la utilizator varsta.
CAT TIMP utilizatorul NU introduce un numar, cerem din nou.
"""
print('#' * 50)
varsta = input("Introdu varsta:\n")
while not varsta.isdigit():
    varsta = input("Introdu varsta:\n")
print(f'Varsta este {int(varsta)}')

print('#' * 50)


count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)