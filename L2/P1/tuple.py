
""""
########################################################
"""
"""
Tuple (tupla) =  o structura de date asemanatoare cu o lista, cu diferenta ca 
tupla este IMUTABILA , odata declarata nu o mai putem schimba in nici un fel.
Sintaxa este cu paranteze rotunde ()

"""
t = (1, 2, 3)

print(type(t))
print(t[0])
print(t[1])
print(len(t))
# t[0] = 7 # va da eroare, nu putem schimba valorile existente  "TypeError: 'tuple' object does not support item assignment"
#del t[0] #va da eroare, nu putem sterge valori "TypeError: 'tuple' object doesn't support item deletion"

"""
Poate tine orice tipuri de date, le tine ordonat, valorile nu trebuie sa fie unice
"""
tupla_comp = (1, 2, True, 1, 2, "string", [100, 101, 102], {0, 100})
print(tupla_comp)
print(type(tupla_comp))
tupla_comp[6].append(103)
print(tupla_comp)

tupla_goala = ()
print(type(tupla_goala))

"""
 TupleMethohs
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""