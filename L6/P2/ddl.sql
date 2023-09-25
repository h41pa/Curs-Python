/*
DDL = Database Definition Language = instructiunile prin care definim structura bazei de date:
1. CREATE
2. DROP
3. ALTER
4. RENAME

*/
-- asa se pot scrie comentarii in limbajul SQL
/*
multiline comment
create database curs;
create database if not exists curs; -- creaza o baza de date (daca nu exista deja)
*/


create database curs;
use curs; -- seteaza baza de date "curs" ca fiind cea pe care lucram in mod curent

/*
Create Table -  instructiunea care ne ajuta sa cream tabele
CREATE TABLE NUmeTabel (
      Attr1 Tip1,
      Attr2 Tip2,
      ....
)   
Tipurile atributelor pot fi:
- INT, TINYINT
- FLOAT
- CHAR, VARCHAR(size)
- BOOL, BOOKEAN

Constrangeri:
- NOT NULL - coloana respectiva nu are voie sa aiba valori nulle
- PRIMARY KEY - Coloana respectiva trebuie sa aiba valori UNICE in tabel. (not null si UNIQUE)
- auto_increment - folosit la coloane de tip int , de obicei la id-uri astfel incat noi
nu mai trebuie sa-i dam o valoare acelei coloane,pentru ca se vor genera automat 
valori incrementale pentru fiecare row.

*/

CREATE TABLE Company (
    ID INT NOT NULL,
    CompanyName varchar(127) NOT NULL,
    Address varchar(255),
    Capital INT,
    PRIMARY KEY (ID)
    
);
/*
FOREIGN KEY = modalitatea prin care un tabel poate avea o relatie cu un alt tabel
Zicem ca tabelul A referentiaza tabelul B, si folosim urmatoarea sintaxa.
FOREIGN KEY (CheieTabelA) REFERENCES TabelB(CheieTabelB), cu conditia ca
CheieTabelB sa fie not null si unique (sau primary key).
*/

CREATE TABLE Employee (
	CNP VARCHAR(13) NOT NULL,
    FirstName VARCHAR(31),
    LastName VARCHAR(31),
    EmploymentDate DATE,
    BirthDate DATE,
    CompanyID INT,
    PRIMARY KEY (CNP),
    FOREIGN KEY (CompanyID) REFERENCES Company (ID)
     

);
/*
ALTER  - instructiune care ne permite sa modificam structura unui element (db sau tabel).
Avem mai multe tipuri de actiuni (pe tabel):
- RENAME table/column TO new_table/new_column
- ADD column
- DROP column
- MODIFY column
*/

ALTER TABLE Company ADD COLUMN IsSRL BOOL DEFAULT True;

/*
Pentru a manipula datele din interiorul bazei noastre de date, folosim urmatoarele instructiuni:
- INSERT - cream o intrare noua in db (adica un row)
- UPDATE - modificam un row (ATENTIE, aici avem de obicei nevoie de WHERE!!!)
- DELETE - stergem un row (ATENTIE, aici avem nevoie de WHERE)
*/
INSERT INTO Company (ID, CompanyName, Address, Capital)
VALUES     (1, "Apple", "Silicon Valley", 10000000),
           (2, "Microsoft", "Bucuresti", 150000),
           (3, "Emag", "Romania", 250000);
INSERT INTO Employee (CNP, FirstName, EmploymentDate, CompanyID)
VALUES ('12345678901', "Marcela", "2020-03-09", 1),
       ('12345908901', "Dan", "2020-04-03", 1),
       ('1234519901', "Marcela", "2020-06-02", 1);
       
INSERT INTO Employee (CNP, FirstName, EmploymentDate, CompanyID)
VALUES ('12342678901', "Mihai", "2020-03-09", 1),
       ('1234509901', "Liviu", "2020-04-03", 2),
       ('123423901', "Gogu", "2020-06-02", 3);
UPDATE Employee SET LastName = 'Popescu' WHERE CNP = '12345678901' ;
DELETE FROM Employee WHERE CNP = '12345678901';

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


