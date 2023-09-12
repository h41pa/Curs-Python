"""
Operatori aritmetici:
+ (adunare)
- (scadere)
* (inmultire)
/ (impartire cu virgula)
// (impartire cu rest)
** (ridicarea la putere)
% (restul impartirii) -> se numeste modulo
"""

a, b = 17, 5
print(a + b)
print(a - b)
print(a * b)

print(a / b)    # va da rezultatul float, adica 3.4
print(a // b)   # va da catul impartirii, adica 3
print(a % b)    # va da restul impartirii, adica 2

print(a ** 5)   # va da 17 la puterea 5, adica 1 419 857

"""
Exista operatori arimetici care se pot folosi si pealte tipuri de date:
+ (adunare) - se poate folosi pe stringuri, pentru concatenare
* (inmultire) = se polae folosi pe un string cu un integer, si face o concatenare repetata

"""
print("a" + "b" + "cde")  # abcde
print("a" * 10)  # aaaaaaaaaa

"""
Operatori de atribuire (asignare)
= (egal) - operatorul prin care atribuim direct o valoare unei variabile
nume_var op= valoare
"""
x = 5           # atribuire
y = "string"    # atribuire
z = True        # atribuire

# toate operatiile aritmetice ne permit sa stocam valoarea obtinuta
# tot in aceleasi variabile, folosind aceasta sintaxa scurta

x -= 3  # echivalent cu x = x - 3
print(x)
x += 7  # echiv cu x = x + 7
x *= 2  # echiv cu x = x * 2
x **= 3 # echiv cu x = x ** 3
print(x)
print('_' * 80)

"""
Operatori de comparatie (rezultatul va fi mereu boolean, adica adevarat sau fals)
== (dublu egal) - verifica egalitatea
!= (semnul exclamarii si egal) - verifica inegalitate, adica diferit
>   (mai mare)
<   (mai mic)
>= (mai mare sau egal)
<= (mai mic sau egal)
"""
c, d = 10, 5
print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)
print('=' * 60)

"""
Operatori logici (si, sau, negare) - functioneaza pe boolene
and => da adevarat doar daca ambele valori sunt True
or => da adevarat daca cel putin o valoare este True
not => schimba valoarea (True devine False, si False devine True)
"""
age = 17
is_adolescent = age >= 13 and age <= 19

salary = 15000
parents_are_rich = False
person_is_rich = parents_are_rich or salary > 30000

print(parents_are_rich, not parents_are_rich)   # not trebuie pus in fata variabilei