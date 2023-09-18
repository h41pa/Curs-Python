"""
Virtual environment (virtualenv) = un mediu virtual (venv) este de fapt un folder special in care se instaleaza
toate pachetele de care are nevoie proiectul nostru, impreuna cu versiunea dorita de Python, si cea de pip.

Venv = sunt necesare din mai multe motive:
    1. nu toate proiectele vor avea nevoie de anumite pachete, si atunci nu are sens sa "incarcam" toate pachetele
        la fiecare proiect.
    2. uneori vom avea proiecte care ruleaza pe versiuni diferite de Python (3.8.5 vs 3.11.0); iar aceaste versiuni
        nu sunt compatibile
    3. uneori vom avea proiecte care au nevoie de versiuni diferite ale aceluiasi pachet, si atunci aceste versiuni
        nu sunt compatibile.

Venv = un mediu izolat, in care ruleaza proiectul nostru, definit de versiunea de Python, si de lista lui de dependinte.
Atunci cand lucram intr-un virtualenv, vom avea acces la o versiune de Python "locala", adica un executabil
clonat din versiunea globala.

Pentru a crea un virtualenv din Pycharm, mergem la:
    => File => Settings => Project: Nume Proiect (in stanga) => Project Interpreter
    Apoi in dreapta sus avem linkul de "Add interpreter" => Add Local Interpreter
    Care va deschide o fereastra in care putem adauga un venv existent, sau putem crea unul nou.

"""
