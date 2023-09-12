"""
In general, folosim FOR pentru a itera peste colectii sau in situatii in care stim
exact numarul de repetitii.

While in schimb, este folosit atunci cand NU stim exact numarul de iteratii, DAR
stim cand vrem sa ne oprim (adica avem o conditie de oprire).

"""

numbers = [4, 54, 6, 90, 12, -5, 0]
print("Parcurgere cu for:")
for number in numbers:
    print(number)

print("Parcurgere cu while")
idx = 0 # pornim de la primul element, cel cu index 0
while idx < len(numbers): # cat timp indexul este mai mic decat lungimea listei
    print(numbers[idx])
    idx += 1  # trebuie sa incrementam NOI indexul, altfel intram in bucla infinita

"""
ATENTIE MARE:
in while, putem intra in bucla infinita, DACA conditia noastra nu devine niciodata False
"""

"""
Exercitiu: avem un numar, vrem sa afisam toate numerele divizibile cu 5,
intre acest numar si 100 inclusiv (folosind while).

"""
print('_' * 80)

nr = 12
while nr <= 100:
    if nr % 2 == 0:
        print(f"{nr} este divizibil cu 5")
        nr += 1
    else:
        nr += 1
        continue
# for x in range(12, 100):
#     if x % 5 == 0:
#         print(f'{x} este')
