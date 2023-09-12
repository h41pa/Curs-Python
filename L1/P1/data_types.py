"""
Tipuri de date:

1. numere   -> int (numere intregi)
            -> float (numere cu virgula)
2. boolean  -> True/False (valoare logica)
3. siruri de caractere -> string (adica text liber)

Text = str
Numeric	= int, float, complex
Sequence = list, tuple, range
Mapping	= dict
Set = set, frozenset
Boolean = bool
Binary = bytes, bytearray, memoryview

"""

age = 30    # int
height = 1.78   # float
is_married = True   # boolean
has_children = False    # boolean
first_name = "Adela-Elena"  # string
last_name = 'Kacso-Vidrean' # string
description = "Putem scrie aici orice ne dorim, un string poate contine cam orice."

alfa = '1234'   # acesta este un STRING, chiar daca are o valoare de numar
beta = 'True'   # tot string
gamma = '1.21'  # tot string

"""
Functia type ne poate zice ce tip de data avem intr-o anumita variabila 
"""
print(type(age))
print(type(height))
print(type(is_married))
print(type(first_name))
print('_' * 80)     # delimitator

print(type(alfa))
print(type(beta))
print(type(gamma))

"""
Ca sa schimbam tipul unei variabile folosim o tehnica numita type casting:
adica avem niste functii speciale (numite int, str, bool, si float)
care ne ajuta sa schimbam tipul variabile respective.
"""
alfa = int(alfa)    # as putea folosi si float aici, daca as vrea sa obtin un numar zecimal
print(f'Dupa type casting, alfa: {type(alfa)}')
beta = bool(beta)
print('Dupa type casting, beta: ', type(beta))
gamma = float(gamma)
print('Dupa type casting, gamma: ', type(gamma))
var_x = 'Text aiurea aici, care  nu poate fi convertit'
# var_x = int(var_x)  # va da eroare

"""
Int si float pot fi convertite una la cealalta, cu mentiunea ca pierdem zecimalele
3.14 (float) -> 3 (int)

Integer si bool si ele pot fi convertite una la cealalta
True -> 1
False -> 0
Viceversa, 0 va deveni False, si orice alta valoare devine True

Toate tipurile de date se pot converti la string, cu functia str()
"""
print(int(3.14))    # va afisa 3
print(float(10))    # va afisa 10.0

print(int(True))    # va afisa 1
print(int(False))   # 0
print(bool(-1))     # True
print(bool(0))      # False, singura valoare care e convertita la False
print(bool(1999))   # True

