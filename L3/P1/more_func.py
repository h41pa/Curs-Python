students = ['Octav', 'Gabriel', 'Bogdan', 'Liviu', 'Eugen', 'Roxana']
def say_hello(student_name):
    print(f'Hello, my name is {student_name} and I am learning Python')
for stud in students:
    say_hello(stud)
"""
return value = valoarea sau valorile pe care o/le returneaza o functie
Nu toate functiile returneaza ceva, unele fac doar niste calcule/printari/etc, si apoi ies
In Python, putem returna o singura valoare, DAR aceasta valoare poate fi si list/tuple/dict/set
"""

print('_' * 80)
def maxim(a, b):
    print(f'a este {a}')
    print(f'b este {b}')
    if a > b:
        return a  # cand intalneste un return, functia se opreste din executie (iese)
         # si da inapoi codului care a apelat-o valoarea de dupa return

val_max = maxim(5, 3)
print(f'Valoarea maxima e {val_max}')
val_max = maxim(5, 10)  # daca nu avem nici un return intr-o functie, atunci aceasta ne va returna
# valoarea speciala None => care inseamna nimic, absenta valorii
print(f'Valoarea maxima e {val_max}')

def maxim2(a, b):
    print(f'a este {a}')
    print(f'b este {b}')

    # if a > b:
    #     return a
    # else:
    #     return b
    ''' echivalent cu '''
    if a > b:
        return a
    return b
print(f'Valoarea maxima dintre 7 si 12 este {maxim2(7, 12)}')
print(f'Valoarea maxima dintre 15 si 9 este {maxim2(15, 9)}')

print('_' * 80)
# def sort2(x, y):
#     if x > y:
#         return x, y
#     else:
#         return y, x

def sort2(x, y):
    if x > y:
        return x, y
    return y, x
sort_result = sort2(12, 5)
print(sort_result)
print(type(sort_result)) # va fi tupla, deoarece Python face packing atunci cand returneaza mai multe valori

nr1, nr2 = sort2(10, 100) # daca stim exact numarul de valori returnate, putem face operatia inversa: unpacking
print(f'Nr 1 este {nr1} si nr 2 este {nr2}')