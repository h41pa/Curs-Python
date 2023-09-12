# Primul meu fisier python => este un fisier python deoarece are extensia .py
# Diezul este un caracter special care ne permite sa scriem comentarii
# Comentariu = un text care NU va fi citit de catre compilator, adica nu este cod
# Comentariile sunt folosite ca niste notite, in care noi incercam sa explicam o mica bucata de cod
# Cu CTRL + / putem comenta si decomenta rapid una sau mai multe linii
# Diezul permite comentarii doaar pe linia pe care se afla si el, adica comentarii single-line

"""
Comentariu multi-line (adica pe mai multe linii)
Asa pot scrie cat text vreau eu, pe cate linii vreau,
Si nu mai trebui sa pun alte caractere speciale.
"""

'''
Putem folosi atat ghilimele simple,
cat si duble, DAR foarte important: folosim peste tot ceea ce am ales.
Consistency is key!
'''

# Functia print = functia care ne ajuta sa afisam text in consola
print("Hello, world! How are you?")

"""
Indentare Python
Indentarea se referă la spațiile de la începutul unei linii de cod.

În cazul în care în alte limbaje de programare, indentarea în cod este doar pentru lizibilitate,
indentarea în Python este foarte importantă.

Python folosește indentarea pentru a indica un bloc de cod.

"""
if 5 > 2:
  print("Five is greater than two!")

# if 5 > 2:
# print("Five is greater than two!")
"""
va da eroare de indentare
IndentationError: expected an indented block after 'if' statement on line 36
"""