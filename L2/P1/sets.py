
"""
Set =  o structura de date care nu permite duplicate.
Seturile nu sunt ordonate si nici indexate, putem  adauga sau sterge elemente din ele
Sintaxa:
{ elem1, elem2, elem3, .... elemX }
"""
s = {1, 2, 3, 1}
print(type(s))
print(s)    # va printa {1, 2, 3}, deoarece setul nu permite duplicate
s.add(7)
s.add(3)
print(s) # va printa {1, 2, 3, 7}
s.remove(2)  # vom scoate elementul cu valoarea 2
print(s) # {1, 3, 7}
"""
Si setul poate tine apropae orice tipuri de date:
- toate tipurile basic(int, float, bool, string) 
- liste NU
- dictionare NU
- alte seturi NU
- tuple Da
Practic setul poate  avea doar valori inmutabile (care nu pot fi modificate)
"""
set_complex = {1, 2, True, False, 'Ana are mere'}
print(set_complex)
set_gol = {} # nu putem face asa, asta e dictionar
set_gol = set()
set_gol.add(100)
set_gol.add(12)
set_gol.add(True)
set_gol.add('string')
print(set_gol)
set_gol.clear()
print(set_gol) # cu clear stergem elementele din set set()

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.intersection(b)) # intersection = elementele comune {4, 5}
print(a.difference(b))     # diferenta = elemente care exista in a, dar nu in b {1, 2, 3}
print(b.difference(a)) #  {8, 6, 7}
print(a.union(b)) # union = suma elementelor din cele 2 seturi (unice) {1, 2, 3, 4, 5, 6, 7, 8}

"""
Set Methods

add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""