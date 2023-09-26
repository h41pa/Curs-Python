"""
API = Application Programing Interface
Este un standard care ne permite sa realizam comunicarea intrea anumite aplicatii.
In mod uzual, noi ne vom referi la o arhitectura de tipul client-server.

Client =  aplicatia care "consuma" API-ul, adica cea care cere informatii prin API de la un server

-> cel mai des clientul nostru poate fi un browser sau o aplicatie mobila

Server = aplicatie care "produce" un API, adica cea care ofera date pentru client

REST = REpresentational Stateless Transfer

Este un set de costrangeri arhitecturale care permite ca aceasta comunicare client-server sa se
realizeze cat mai usor cu putinta.

Intr-un REST API, avem un set de 6 reguli care trebuie sa fie urmate:

1. Trebuie sa avem o interfata uniforma pentru resurse .
     https://serverulmeu.ro/
     Calea trebuie sa fie intuitiva pentru orice resursa, si sa urmeze o anumita structura:
    /articles => aici trebuie sa putem lua lista de articole
                => in general, nu vom putea lua *toate* resursele din prima de pe un endpoint de genul acesta
                asa ca trebuie sa ne folosim de filtrare si paginatie
    /articles/?page=1
    /articles/?category=travel&page=2
    /articles/<id> => /articles/1 pentru primul articol
                        /articles/10001
    /articles/<id>/comments => luam lista de comentarii pentru un articol
    /comments/<comment_id> => primim un singur comentariu

In REST, vorbim despre resurse (in exemplul de mai sus articole si comentarii), si acestea de obicei vor
avea urmatoarele endpoints (URLs pentru API):
    /resourcesX/ => aici putem sa luam intreaga lista de resursa X, SI putem crea o noua resursaX
    /resourcesX/<id> => aici putem lua o singura resursaX, cea cu id-ul ID, o putem updata, sau o putem sterge
    /resourcesX/<id>/resourcesY => aici putem accesa toate resurseleY care sunt in relatie cu resursaX

2. Stateless = sa nu se mentina state-ul (statusul) - nu se tin sesiuni, cookies, etc. deoarece
orice resursa trebuie sa fie accesibila de catre oricine in acelasi fel.

3. Cacheable = anumite resurse pot fi cache-uite pentru acces mai rapid.

4. Decuplarea client - server = avem 2 aplicatii care opereaza individual, si care comunica,
iar asta inseamna ca putem la orice moment sa:
    - rescriem una dintre ele FARA a fi nevoie sa o rescriem si pe cealalta
    - putem avea mai multi clienti deserviti de acelasi server (web emag, app mobila emag)
    - un client poate cere resurse de la mai multe servere

5. Arhitectura in straturi (layered) = acest principiu se refera la faptul ca pe noi nu ne intereseaza
    cine ne ofera resursele cerute (daca este serverul, sau sunt si alte aplicatii auxiliare)

6. Code on demand [optional] => practic, serverul poate raspunde in anumite cazuri si cu cod executabil,
    nu doar cu date statice.



"""


"""
Exemplu de API care raspunde in format JSON.

https://dummyjson.com/products => primim o lista de produse (doar primele 30, e paginat)
https://dummyjson.com/products?limit=50&skip=30 => primim urmatoarele 50 produse (se "sare" peste primele 30)
Ca sa primesc toate cele 100 produse dintr-o data, putem face:
https://dummyjson.com/products?limit=100 

Daca dorim sa facem un sistem de paginare din 10 in 10, putem face asa:
https://dummyjson.com/products?limit=10
https://dummyjson.com/products?limit=10&skip=10
https://dummyjson.com/products?limit=10&skip=20
https://dummyjson.com/products?limit=10&skip=30
...

https://dummyjson.com/products/1 => primim produsul cu ID-ul 1

Daca ID-ul produsului nu exista, vom primi un mesaj de eroare:
https://dummyjson.com/products/101


Relatii intre resurse: un product are o categorie. Putem lua toate categoriile existente cu endpointul:
https://dummyjson.com/products/categories

Si putem filtra toate produsele dintr-o anumita categorie cu endpointul:
https://dummyjson.com/products/category/smartphones

"""