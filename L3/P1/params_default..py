
"""
Parametrii unei functii:
- sunt pozitionali* (adica ordinea pe care le-o dam la definire coincide cu ordinea de la apelare)

def f(a, b, c, d):
    pass

f(1, 2, 5, 7) => a=1, b=2, c=5, d=7

- nu este obligatoriu ca o functie sa aiba parametrii
def g():
    pass

- parametrii fara valoare (pozitionali) sunt OBLIGATORII
    Adica nu pot apela functia f definita mai sus, fara sa ii dau 4 parametrii

- exista si parametrii care NU sunt pozitionali, se numesc parametrii numiti (named parameters)
    => acestia au deja o valoare predefinita, si se pot pasa folosind numele lor
"""

print('_' * 80)
def my_func(a, b, c=7, d=100):
    """
    a si b sunt parametrii OBLIGATORII, adica trebuie sa existe MEREU cand apelam functia
    c si d sunt parametrii OPTIONALI, adica daca nu le dam o valoare cand apelam functia,
        ei vor lua valoarea implicita care este definita odata cu functia
    Toti parametrii care NU au o valoare default trebuie sa fie primii in definirea unei functii.
    Dupa ei, vin toti parametrii care au valori default.
    """
    print(f'a={a}, b={b}, c={c}, d={d}')

my_func(1, 2) # a=1, b=2, c=7, d=100
my_func(1, 2, 3) # a=1, b=2, c=3, d=100
my_func(1, 2, 3, 4) # a=1, b=2, c=3, d=4
my_func(b=5, a=10) # a=10, b=5, c=7, d=100  - am pasat a si b prin nume
# my_func(b=5, a=10, 12)    # va da eroare, deoarece NU putem pune parametrii pozitionali DUPA cei numiti
my_func(12, b=3, d=9) #a=12, b=3, c=7, d=9
my_func(b=5, a=10, c=12) # a=10, b=5, c=12, d=100

my_func(10, 5, c=12, d=13)  # ordinea va fi: prima data param POZITIONALI, apoi cei NAMED (numiti) a=10, b=5, c=12, d=13

"""
Putem avea oricati parametrii dorim pentru o functie,
DAR regula bunului simt zice ca daca sunt prea multi, nu bine.
Mai precis, daca avem mai mult de ~6 param, trebuie sa gasim o alta modalitate de a scrie codul.
"""