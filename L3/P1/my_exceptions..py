"""
Exceptiile sunt modalitatea lui Python de a ne zice noua ca programatori ca ceva
nu a mers bine in cod.
Exceptie vs eroare: in Python sunt destul de similare, dar in alte limbaje de programare sunt diferite.

Exceptiile: se intampla DOAR in anumite cazuri in codul nostru, de obicei atunci cand avem de a face
cu input de la utilizator.
"""

"""
Folosim exceptiile ca un mecanism de protejare a programului nostru,
astfel incat acesta sa nu crape chiar si in situatii in care nu totul merge perfect.

try:
    aici avem codul
    care ar putea arunca o exceptie
except:
    aici avem codul care va fi apelat DACA in timpul
    executiei blocului try a aparut o exceptie
"""

age_intervals = ['0-18', '18-35', '35-65', '65+']
for i in range(len(age_intervals)):
    print(f'{i} : {age_intervals[i]}')
try:
    user_ai = int(input(f'In ce interval de varsta te afli?\n'))
    print(f'Te afli in intervalul {age_intervals[user_ai]}')
except ValueError:
    print('Exceptie, nu ai introdus un NUMAR')
except IndexError:
    print('Exceptie, ai introdus un numar, DAR nu unul intre 0 si 3')
finally:
    """
        Un use-case posibil pentru finally este atunci cand incercam sa citim dintr-un fisier.
        Chiar daca citim fara eroare, sau daca dam de o eroare pe parcurs,
        la final trebuie sa inchidem fisierul, iar aceasta actiune se face in finally.
        """
    print(f'This is finally. Acest cod este MEREU executat!')

print('Am terminat programul')
