"""
Pentru a lucra cu fisiere (general) avem nevoie sa:
    1. deschidem fisierul in modul dorit (w, r, a)
    2. facem ce dorim (citim, scriem, etc)
    3. * inchidem fisierul (daca folosim un context manager, nu mai e nevoie sa il inchidem manual).

open('name.txt')    => sintaxa pentru deschidere fisier in mod citire (r) => default.
open('name.txt', 'w')   => w = mod scriere, ATENTIE, va suprascrie ceea ce avem.
open('name.txt', 'a')   => a = mod append, care va adauga ceea ce vrem sa scriem la finalul fisierului.
"""
with open('files/file.txt') as my_file:
    # my_file.write('ceva') # va arunca io.UnsupportedOperation: not writable
    my_lines = my_file.readlines() # citesc toate liniile din fisier intr-o lista
    for line in my_lines:# fiecare linie din fisier va avea un '\n' la final (adica un caracter newline)
        print(line)

print('_' * 80)

with open('files/other.txt') as my_file:
    for line in my_file:  # context managerul imi da deja un obiect iterabil, asa ca pot citi fisierul direct linie cu linie
        print(line)
print('_' * 80)
with open('files/new.txt', 'w') as new_file:
    new_file.writelines(['Hello\n', 'Have a god day!\n', 'bye\n'])

with open('files/new.txt', 'a') as new_file:

    new_file.write('Astfel adaugam mai mult text la finalul fisierului nostru...')

with open('files/other.txt', 'a') as my_file:
    my_file.write('Hello !!!')
    print('Hello world !', file=my_file)
# putem folosi si print pentru a scrie intr-un fisier
# print va pune automat un newline atunci cand scrie