/*
DML = data manipulation language = instructiunile prin care lucram cu datele propriu-zise:
1. INSERT
2. UPDATE
3. DELETE
4. SELECT

*/

SELECT * FROM curs.company;
/*
SELECT = cuvantul cheie prin care putem interoga baza de date pentru a citi informatii din tabele.

SELECT <nume coloane> FROM <nume tabel>
* (steluta) => toate coloanele

- LIMIT <nr> => limitam numarul de rows pe care le aducem din tabel
- COUNT 	 => numaram cate rows sunt in tabel
- WHERE <conditie>	 => ma ajuta sa restrang rezultatele query-ului folosind conditia data.
*/
-- LUAM TOATE COMPANIILE DIN TABELA , prima data doar 2 , iar apoi toate
SELECT ID, CompanyName FROM Company;
SELECT * FROM Company;
-- luam primii 3 angajati din tabela
SELECT * FROM employee LIMIT 3;
-- selectam numarul total de angajati din tabela
SELECT COUNT(*) FROM employee;
-- selectam toti angajatii in ordinea numelui descrescator
SELECT * FROM employee ORDER BY FirstName desc;
-- selectam toti angajatii care si-au setat ziua de nastere
SELECT * FROM employee WHERE BirthDate IS NOT NULL;
-- selectam toti angajatii dintr-o anumite companie
SELECT * FROM employee WHERE CompanyID = 1;

/*
GROUP BY - ne permite sa grupam mai multe rows in functie de una sau mai multe coloane,
in general pentru a aplica un agregator pe ea (MIN, MAX, SUM, COUNT, AVG)
*/
SELECT COUNT(*), CompanyID FROM employee GROUP BY CompanyID; 
/*
JOIN = modalitatea de a "uni" doua sau mai multe tabele care au o relatie intre ele
Sunt mai multe tipuri de join, in functie de ce anume ne dorim..alter

SELECT <ceva> FROM TabelA
INNER JOIN TabelB ON TabelA.camp1=TabelB.camp2;

In INNER JOIN se vor selecta pt join doar randurile care au valori (adica care nu-s nulle)
din fiecare din cele doua tabele.
LEFT JOIN - se vor selecta toate rows din TabelA, si doar rows cu valori non-nulle din TabelB
RIGHT JOIN - invers ca mai sus
CROSS JOIN - va returna toate valorile din ambele tabele, chiar daca acestea au si valori nulle
*/

SELECT FirstName, CompanyName FROM employee CROSS JOIN company ON employee.CompanyID = company.ID;
-- putem aliasa anumite coloane pentru a obtine un rezultat mai frumos, sau pentru a avea queries mai scurte
SELECT FirstName AS fn, LastName AS ln FROM employee
