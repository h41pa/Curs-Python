
"""
Lista(list) = o strucutra de date Python care poate contine orice alte tipuri de date,
si care este delimitata de paranteze drepte, iar elementele ei sunt delimitate cu virgula.
"""

"""
#######################################################################################################################
Listele :
- sunt mutabile (adica le putem modifica)
- pot tine orice tipuri de date
- sunt accesibile prin index
- indexarea incepe de la 0 si se termina la len(l) -1
- putem accesa si cu indecsi negativi
- pot tine si valori duplicate
"""

lista = [1, 2, 3, 10]

print(type(lista))
"""
Pentru a lucra cu elemente individuale din lista, folosim accesarea directa,
adica prin index. Indexarea incepe de la 0 !!
"""
print(lista[0]) # primul element din lista, adica numarul 1
print(lista[1]) # al doilea element din lista, adica numarul 2
print(lista[3]) # al patrulea element din lista, adica nr 10

"""
Pentru a stii cate elemente aveam intr-o lista, folosim functia len.
"""
print(f'Lista mea are {len(lista)} elemente')
print(f'Deci indexul ultimului element va fi len(l) - 1')
print(f'Iar acel element poate fi accesat cu formula {lista[len(lista) - 1]} sau {lista[-1]}')

"""
Deoarece putem scrie  lista[len(lista) - 1] pentru a gasi ultimul elemnet
Python are o sintaxa speciala care ne permite sa nu mai punem partea cu len(l),
adica putem folosi indecsi negativi

"""
print(f'Ultimul element va fi {lista[-1]}')
print(f'Penultimul element va fi {lista[-2]}')

# print(lista[-5])  # va da eroare, IndexError: list index out of range
# print(lista[4])  # va da eroare, IndexError: list index out of range
#Unpacking List Items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

"""
Listele sunt mutabile - adica le putem modifica atat prin schimbarea elementelor existente,
cat si prin adaugarea unora noi, sau stergerea celor care sunt deja in lista.
"""
print('_' * 80)

l = [1, 2, 3, 10]
print(l) # [1, 2, 3, 10]
l[2] = 7 # schimb valoarea celui de-al treilea element din lista din 3 in 7
print(l) # [1, 2, 7, 10]
l.append(15) # asa adaugam un element nou la finalul listei
print(l)
l.insert(3, 100) # asa inseram un element unde vrem noi, insert(index, element) => inserarea se face inaintea indexului dat ca parametru
print(l) # [1, 2, 7, 100, 10, 15]
last = l.pop() # pop va sterge ultimul element din lista daca nu ii dam nici un argument
print(l) # [1, 2, 7, 100, 10]
first = l.pop(0) # sau va sterge elementul de la indexul mentionat, daca ii dam un argument
print(l)
print(f'Am sters ultimul {last} si primul {first}')


print('_' * 80)

list_strings = ['Ana', 'are', 'multe mere']
print(type(list_strings))
print(list_strings[0]) #Ana
print(list_strings[0][0]) #A
print(list_strings[0][1]) #n

lista_complexa = [
    1,
    2,
    'caise',
    True,
    ['alta', 'lista', 9],
    100,
    False,
    [],
    {}
]
print(type(lista_complexa))
lista_goala = []
print(lista_complexa[4]) # lista interioara este un singur element ['alta', 'lista', 9]
print(lista_complexa[4][0]) # alta

thislist = ["apple", "banana", "cherry"]
if "apple"in thislist:
    print('Yes')
# Change a Range of Item Values

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

"""
If you insert more items than you replace, 
the new items will be inserted where you specified, and the remaining items will move accordingly
"""
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']
"""
if you insert less items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly

"""
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ['apple', 'watermelon']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # ['apple', 'orange', 'banana', 'cherry']

#extend

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

"""
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
"""
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']

"""
remove pentru a sterge un element specific
pop pentru a sterge in fucntie in functie de index
"""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse= True)
print(thislist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)
"""
List methods:

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

