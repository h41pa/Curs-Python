

"""
Functia - este o bucata de cod, care are un nume* si pe care noi o putem folosi ori de cate ori vrem.
Sunt relativ asemanatoare functiile din matematica ( f(x) = 2*x+5)
f - numele functiei
x - parametrul functiei, adica un nume de variabila pe care noi il putem folosi in interiorul functiei,
dar care primeste o valaore atunci cand apelam functia: f(5), f(100)
rezultat - valoarea returnata de o functie; exemplu f(5) => 15, f(100) => 205
"""

"""
Sintaxa:
def nume_functie(param1, param2, ... paramX):
    aici
    facem
    tot
    ce
    vrem
    cu
    functia
    
"""
# def myname(name):
#     print(f'{name} Chelu')
# myname('Madalin')
# myname('livia')

# nu putem apela o functie inainte ca aceasta sa fie definita
# f(200) # NameError: name 'f' is not defined

def f(x):
    print(f'Sunt in functia f!')
    print(f'Am primit parametrul {x}')
    print(f'Gata, acum iesim din functie. Bye bye!\n')

print('Azi invatam despre functii!')

"""
Apelarea unei functii, adica invocarea codului respectiv, se face folosind numele functiei respective,
urmat de paranteze rotunde, si eventuali parametrii.
"""
f(5)
f('Madalin')


