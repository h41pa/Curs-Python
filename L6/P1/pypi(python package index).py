"""
Uneori, vrem sa folosim cod gata facut de alti developeri in proiectul nostru;
dar acel cod nu face parte din Py Standard Lib.

PYPI (Python Package Index) = ca un fel de Github, unde oamenii isi pot partaja pachetele Python.
Un pachet Python = o mini-librarie care are anumite functionalitati pe care le vrem in proiectul nostru.

Spre deosebire de PSL, pachetele de pe PYPI trebuie *instalate* inainte sa le putem importa si folosi.
Pentru instalare, folosim un utilitar din terminal numit pip, cu sintaxa
    -> pip install nume_pachet
"""

"""
pip install requests => prima data se vor cauta toate dependintele pachetului requests:
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests     
        => vedem mai sus ca requests depinde de 4 alte pachete.

Versioning: requests-2.30.0
Atunci cand pip instaleaza un pachet, se ia in mod standard ultima versiune.

Daca vrem sa instalam alta versiune, trebuie sa ii specificam lui pip:
    -> pip install requests==2.28.0     (unde 2.28.0 este numarul versiunii pe care o vrem).

Pentru a vedea toate pachetele instalate intr-un venv, folosim comanda:
    -> pip list

Pentru a putea lucra in echipa, deoarece nu avem posibilitatea de a "partaja" venv-urile (avem sisteme de operare diferite),
folosim urmatoare modalitate:
    1. Scriem toate dependintele proiectului nostru intr-un fisier special, cu urmatoarea comanda:
    -> pip freeze > requirement.txt
    2. De fiecare data cand cineva vrea sa foloseascca proiectul nostru, TREBUIE sa instaleze dependintele pe care
        le-am generat noi, pentru a ne asigura ca folosim toti acelasi setup de proiect.
    -> pip install -r requirements.txt

"""
import requests

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)