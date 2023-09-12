"""
Functia print ne ajuta sa afisam informatii in terminal.
print(ceva, altceva, blabla) = putem afisa oricate chestii, cu virgiula intre ele.
Functiile se apeleaza folosind sintaxa:
nume( parametrii )

"""

print("Mere", "Pere", "salutare", 1234, True)
# print(Ce faci) # va da eroare, nu este tip de data valid (SyntaxError: invalid syntax. Perhaps you forgot a comma?)

name = "Madalin Chelu"
print("Numele meu este " + name)

#Functia print trece pe o linie noua la fiecare apelare
print("Numele meu este")
print(name)

age = 30
#print("Varsta mea este :" + age) # va da Eroare nu putem concatena str cu int , doar str cu str , de acea folosim f-strings
"""
f-strings => un mod mai pythonic de a afisa variabile in mesajele noastre 
punem f '' si numele variabile intre {}
"""
print(f'Numele meu este {name} si am {age} ani.')
