"""

URL = Uniform Resource Locator

https://www.emag.ro/laptopuri/filter/capacitate-memorie-f7886,4-gb-v27569/c?ref=lst_leftbar_7886_27569

1. http SAU https = protocolul prin care accesam URL-ul,
    HyperText Transfer Protocol / Secure

2. wwww = world wide web [optional]

3. emag.ro = domeniul aplicatiei, si acesta este de fapt "numele" site-ului nostru
    emag - numele propriu zis
    .ro = TLD (top-level domain) => romania
    .co.uk => UK
    .net, .edu, .gov

4. path: /laptopuri/filter/capacitate-memorie-f7886,4-gb-v27569/c
    - calea de pe server care ne zice noua ce resursa cautam
    - seamana foarte mult cu calea locala pentru un fisier

5. ?ref=lst_leftbar_7886_27569
    - toata partea de dupa semnul intrebarii este partea numita query parameters
    - acesti query params sunt niste informatii pe care NOI le trimitem catre server
        pentru a putea primi un raspuns cat mai corect si mai specific
    - ?qp1=valoare1&qp2=valoare2&qp3=valoare3
    - formatul este ? urmat de <nume_query_param>=<valoare_query_param>
        si sunt legati intre ei de caracterul &
    Acesti query params se folosesc de obicei pentru:
    1. paginatie: URL/?page=5
    2. filtrare: URL/?category=laptops&memory=4GB
    3. sortare: URL/?sort=asc&sort_by=price


"""
"""
<protocol>://<www>.<domeniu>.<tld>/<path>?<qp1=val1&qp2=val2>
https://www.olx.ro/oferte/q-apartament-2-camere-zorilor/?page=3

Dupa o filtrare, se schimba URL-ul:
https://www.olx.ro/oferte/q-apartament-2-camere-zorilor/?search%5Bfilter_float_price:to%5D=100000
"""