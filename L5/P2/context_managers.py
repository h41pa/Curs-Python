"""
Context manager = o implemnetare care ne permite sa gestionam resurse contextul.
Exemple de resurse : fisiere, conexiuni la baza de date, conexiuni la un server, etc.
In general, aceste tipuri de resurse trbuie sa fie deschise si mai apoi inchise.

cel mai utilizat context manager este cu with.

with dechide(ceva.txt) as handler:
      fa ceva cu handler
# aici, dupa ce s-a terminat blocul with, NU vom mai avea acces la handler

ECHIVALENT CU

handler = deschide(ceva) => conexiune la db, fisier, etc.
fa ceva cu handler...
inchide(ceva)

"""

f = open('my_file.txt') # deschidem un fisier pentru citire
lines = f.readlines() # citim toate liniile din fisier
print(lines) # le afisam
f.close() # IMPORTANT : inchidem fisierul
print()

with open('my_file.txt') as my_file:
    for line in my_file:
        print(f'Line: {line}')

# Aici va da eroare, deoarece context managerul with a INCHIS deja fisierul
print(my_file.readlines())      # va da ValueError: I/O operation on closed file.