"""
Slicing (felierea) = operatia care ne permite sa accesam mai multe elemte dintr- lista
sau dintr-un string(care este de fapt doar o lista de caractere)
Sintaxa
lista[start:stop:pass] -> pas este optiona; ,valoarea lui default este 1
- start reprezinta indexul de la care incepem accesarea, acesta este inclus in valoarea finala
- stop reprezinta indexul la care ne oprim, dar acesta nu inclus in valoarea finala
- pas (step) - reprezinta viteza cu care ne miscam de la start la stop , default 1

"""

#    0  1  2  3  4  5  6  7  8
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[2:5]) # # voi obtine elementele din lista originala care sunt la indecsii 2->5, adica [3, 4, 5]
print(l[5:2:-1]) # invers  [6, 5, 4]

print(l[0:len(l):2]) # voi obtine elementele de la indecsii pari [1, 3, 5, 7, 9]

"""
Daca start =  inceputul listei (sau finalul daca mergem cu pass negativ) putem sari peste aceasta valoare
Daca stop = sfarsitul liste ( sau inceputul daca mergem cu pass negativ) putem sari  peste aceasta valoare
"""

print(l[::2]) # echivalent cu print(l[0:len(l):2])  [1, 3, 5, 7, 9]
"""
O metoda foarte simpla de a inversa o lsita este sa o parcurgem cu pas de  -1
"""
print(l[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

"""
Deoarece stringurile sunt practic liste de caractere , si la ele se aplica aceleasi reguli de slicing!
"""
string = "Dan are pere"
print(string[3:10]) #  are pe
print(string[::2]) # Dnaepr
print(len(string)) # 12
print(string[10:100])  # nu va da eroare, dar vom primi doar caracterele existente pana la sfarsitul stringului

# NU DENUMITI VARIBILELE LIST
list = [100, 200]   # <= DON'T