"""
if (daca) =  ne permite sa decidem daca o anumita bucata de cod se executa sau nu, daca est adevarata se executa
Sintaxa:

if conditie:
   acest cod
   va fi executat
   atata timp cat exte indentat corect
...

"""

age = 19

print('Inainte de if')

if age > 18:
    #aceste linii indentate se vor executa daca conditia age >18 este adevarata
    print('Esti major')
    print('Felicitari!')
print('Dupa if')
print("_" * 80)
"""
else(altfel) - functioneaza doar cu if, si este blocul de cod ce sa va executa atunci cand conditia este falsa
if conditie:
    bloc de cod IF
else:
    bloc de cod ELSE

"""
nota_trecere = 5
nota_primita = int(input("Introdu nota:\n"))
if nota_primita >= nota_trecere:
    print(f'Felicitari ai trecuta cu {nota_primita}')
else:
    print("Din pacate ai picat, mai incearca !")

print("_" * 80)

"""
Putem avea oricate nivele de imbricare pentru if-uri, DAR
trebuie sa decidem cat inseamna prea mult
Rule of thumb: 3 nivele de indentare sunt suficiente, daca sunt necesare mai multe,
ar trebui gasita alta solutie
"""

age = int(input('Varsta te rog :'))
if age >= 18:
    print('Felicitari esti major')
    if age >= 65:
        print('felcitari esti pensionar ')
        if age > 100:
            print('Felicitari , esti centagenar')
else:
    print('Esti minor')

print("#" * 60)


"""

The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition.

elif (else-if)

if conditie1:
    cod executat cand conditie1 este adevarat
elif conditie2:
    cod executat cand conditie2 este adevarat
elif conditie3:
    cod executat cand conditie3 este adevarat
....
else:
    cod executat cand niciuna dintre conditiile de mai sus nu sunt adevarate
"""


years_of_experience = int(input("Introdu anii de experienta : "))
if years_of_experience < 0:
    print("Ai gresit valoarea ...")
else:
    if years_of_experience == 0:
        print("Esti intern")
    elif years_of_experience < 3:
        print("Esti junior")
    elif years_of_experience < 5:
        print("Esti mid")
    elif years_of_experience < 10:
        print("Esti senior")
    else:
        print("Felicitari este pensionar")


print("#" * 60)
# Short Hand If ... Else
a = 2
b =500
print('A') if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")