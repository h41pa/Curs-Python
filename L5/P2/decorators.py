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

    print('Hi, my name is Madalin')

say_hello()
introduce_yourself()


"""
De ce folosim decoratori? In general, pentru a adauga o anumita functionalitate in mai multe locuri.
Exemplu din Django -> decoratorul de login_required
DRY = Don't Repeat Yourself

@login_required
def view_all_products():
    ....

"""

print('_' * 80)

"""
Pentru a decora functii cu parametrii, avem nevoie sa stim si de existenta parametrilor in decorator.

   *args - arguments, sau parametri pozitionali ai unei functii .Atunci cand nu stim exact cati parametri
POZITIONALI va avea o functie, pasam *arg, doarece acei paramatri vor fi "impachetati" intro tupla numita args,
iar folosing steluta, facem operatia de despachetare. Packing/Unpacking

   **kwargs - keyword arguments, adica parametrii NUMITI ai unei functii. sunt "impachetati" sub forma unui 
dictionar si sunt despachetati folosind doua stelute.
    
~~~~~~ Sintaxa finala a unui decorator(care functioneaza cu orice tipuri de functii) ~~~~~~

def decorator(func_originala):
    def inner_func(*args, **kwargs):
        ... pre-procesare [optional]
        result = func_originala(*args, **kwargs)
        ... post-procesare [optional]
        return result
    return inner_func
    


"""

def decorator(func):
    def inner_func(*args, **kwargs): # aici avem nevoie de acelasi nr de parametri ca si functia originala
        print('Adding some stuffs')
        print(f'My positional params are: {args}')
        print(f'My keyword params are: {kwargs}')
        result = func(*args, **kwargs) # aici trebuie sa apelam functia originala cu parametrii primit,
        # si sa nu uita, sa returnam rezultatul la final
        print('Done adding stuffs')
        return result


    return inner_func

def introduce(func):
    def inner_func(*args, **kwargs):
        print('Hello there !')
        result = func(*args, **kwargs)
        print('Bye bye !')
        return result
    return inner_func

@decorator
def sum(a, b):
    return a + b

print(sum(10, 17))

print('_' * 80)

@decorator
@introduce
def sum2(a, b, c):
    return a + b + c

print(sum2(1, 2, 4))

print('_' * 80)
@decorator
@introduce
def sum3(a, b, c=0, d=100):
    return a + b + c + d
print(sum3(1, 2, c=5)) # echivalent cu decorator(introduce(sum3(1, 2, c=5))

"""
Exemplu de login required (luat din Flask)

def login_required(func):
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required
"""

"""
Putem avea mai multi decoratori pentru aceeasi functie!
Chaining = inlantuire a decoratorilor, adica acestia se apeleaza pe rand, de sus in jos.

@dec1
@dec2
def func(...):
    ...


Apelarea unei functii decorate ar fi echivalent cu:
dec1 ( dec2 ( func () ))


@login_required
@user_is_admin
def view_products():
    ....

"""