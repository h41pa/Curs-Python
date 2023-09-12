
"""
For (pentru) este un cilcu repetitiv care ne permite sa parcurgem colectii Python
sau intervale de numere
range = functie care ne ofera un interval ( o lista de indecsi)
range(start, stop, step)
- start = de unde incepe intervalul (inclusiv), daca nu il punem, va fi de la 0
- stop = unde ne oprim (exclusiv), este obligatoriu
- step = pasul, daca nu il punem, va fi 1
"""
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(1, 6))) # [1, 2, 3, 4, 5]
print(list(range(2, 10, 2))) #[2, 4, 6, 8]
print(set(range(0, 6))) # {0, 1, 2, 3, 4, 5}
print(tuple(range(1, 6))) # (1, 2, 3, 4, 5)
print(list(range(5, 0, -1))) #[5, 4, 3, 2, 1]

"""
Sintaxa lui fir este:

for <var> in <colectie>:
    fa ceva cu <var>

"""
numbers = range(1, 10, 2)   # va fi [1, 3, 5, 7, 9]
print('Incepe bucla FOR')
for number in numbers:
    print(f'Am ajuns la numarul {number}')
    print('Mergem mai departe ...')
print('Am terminat cu bucla FOR')

"""
cu for putem iera peste orice coelctie python (list, dict, set, tuple)
"""
print('#' * 80)

students = ['Vlad', 'Octavian', 'Diana', 'Petru', 'Ana Maria', 'Roxana']
for nerd in students:
    print(f'Salut eu sunt {nerd} si studiez Python !')
print('#' * 80)
cars = {
    'VW Polo': 12000,
    'Mercedes Benz': 30000,
    'Jeep Compass': 23000
}
print(f'Masina  Pret')
for car_name in cars:
    # in cazul dictionarelor, for va merge prin cheile acestuia
    car_price = cars[car_name]
    print(f'{car_name} {car_price}')
print()
# for name, price in cars.items():
#     print(f'Nume : {name} , Pret : {price}')
"""
In cazul unui dictionar, putem itera direct si peste chei, si peste valori, folosind items:

for <key>, <value> in <my_dictionary>.items():
    fa ceva cu <key> si cu <value>
"""
print('_' * 80)
for car_name, car_price in cars.items():
    print(f'{car_name}  {car_price}')

"""
Putem imbrica for-urile (adica sa avem for in for).
"""
print('_' * 80)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for elem in row:
        print(elem)

print('_' * 80)
# in total vom avea 25 iteratii
for x in range(5):
    for y in range(5):
        print(f'{x} x {y} = {x * y}')

    print('Next')


