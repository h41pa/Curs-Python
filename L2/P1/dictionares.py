
"""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""

"""
Dictionary (dictionar) = o strucutra de date de tipul cheie - valoare
cu mentiunea ca cheile trebuie sa fie unice

Sintaxa:
{
    cheie1: valoare1,
    cheie2: valoare2,
    cheieX: valoareX
}
"""

"""
#######################################################################################################################
In valorile dictionarelor putem pune orice tipuri de date,
dar cheile sunt putin mai restrictionate:
- toate tipurile basic(int, float, bool, string) 
- NU putem folosi o lista ca si cheie
- NU putem folosi un alt dictionar ca si cheie
- NU putem folosi un set ca si cheie
- PUTEM folosi o tupla ca si cheie
Practic, cheile unui dictionar pot fi doar tipuri de date imutabile
"""

d = {
    'dictionary': 'dictionar',
    'car': 'masina',
    'programming': 'programare'
}
print(d)

train = {
    'white': 'rocks',
    'red': 'iron',
    'blue': 'cereals',
    'yellow': 'rocks',
    'pink': 'rocks',
    #'white': '' # nu pot avea chei duplicate
}

"""
Un dictionar se acceseaza la fel ca si o lista , cu diferenta ca aici nu avem indecsi,
asa ca accesam pe baza cheilor
"""
print(train['white']) # rocks
print(train['red']) # iron

"""
Daca folosim numere intregi incepand cu 0 intr-un dictionar, este la fel ca si o lista
"""

dict_as_list = {
    0: 'Ana',
    1: 'are',
    2: 'mere'
}
my_list = ['Ana', 'are', 'mere']
print(dict_as_list[0], my_list[0])



db = {
    True: 'Acesta este true',
    False: 'False',
    # True: '' # nu putem repeta cheile
}
print(db)
dictionar_gol = {}

dict_complex = {
    'id': 1,
    'name': ['Madalin', 'Chelu'],
    'height': 1.88,
    'course': {
        'name': 'Python + Testare automata',
        'start date': '27 martie 2023'
    }
}
print(dict_complex)
print(dict_complex['name'][0]) # Madalin
print(dict_complex['name'][1]) # Chelu
print(dict_complex['course']["name"]) # Python + Testare automata

"""
Pentru a afla dimensiunea unui dictionar, folosim len
Dictionarile sunt mutabile (adica le putem schimba, adauga/sterge valori)

"""
print('_' * 80)
print(len(dict_complex))
dict_complex['id'] = 10 # schimbarea valorii se face prin atribuirea unei noi valori pe vechea cheie
dict_complex['age'] = 31 # adaugarea unui nou element (cheie-valoare)
print(dict_complex)

del dict_complex['course'] # stergerea unui element din dictionar
print(dict_complex) # {'id': 10, 'name': ['Madalin', 'Chelu'], 'height': 1.88, 'age': 31} - course key deleted
"""
Putem vedea toate cheile unui dictionar folosind metoda keys()
Putem vedea toate valorile unui dictionar folosind metoda values()
Putem verifica daca o cheie exista intr-un dictionat inaine de a cere valoarea acesteia folosind get
"""
print(dict_complex.keys())
print(dict_complex.values())

#print(dict_complex['course'])   # va da eroare KeyError: 'course'
print(dict_complex.get('course')) # va da None, o valoare speciala Python care reprezinta absenta valorii
print(dict_complex.get('age')) # 31
dict_complex.clear() # va sterge toate elementele din dictionar
print(dict_complex) # va afisa {}, adica dictionarul gol



"""
Methods
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""