"""
Decorators = functii speciale care ne permit sa augmentam alte functii.
Putem face anumite actiuni folosind decoratorii atat inainte, cat si dupa apelarea functiei decorate
Sintaxa de folosire:
@decorator
def nume_functie_decorata(....):

Sintaxa de implementare:
def decorator_func(decorated_func):
    def inner_func():
        # actiuni inainte de apelarea functiei decorate
        decorated_func()
        # actiuni DUPA functia decorata

    return inner_func
"""

def sayhiandbye(func):
    def inner_func():
        print('Hi')
        func()
        print('Bye')
    return inner_func

@sayhiandbye
def say_hello():
    print('Hi i am your function')

@sayhiandbye
def introduce_yourself():
    name = input("numele tau :")
    print(f'Hi, my name is {name}')

say_hello()
introduce_yourself()


"""
De ce folosim decoratori? In general, pentru a aduga o anumita functionalitate in mai multe locuri.
Exemplu din Django -> decoratorul de login_required
DRY = Don't Repeat Yourself

@login_required
def view_all_products():
    ....

"""

print('_' * 80)

"""
Pentru a decora functii cu parametrii, avem nevoie sa stim si de existenta parametrilor in decorator.
"""
