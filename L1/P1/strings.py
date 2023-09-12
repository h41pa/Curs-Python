
"""
Stringurile - sunt tipuri de date care salveaza text folosing ghilimele simple sau duble.

pentru a folosi " ' in text folosim  escape character \"
MyString = "Hello World!"
MyString = 'Hello World!'
len(s) = ne da lungimea unui string , adica numarul de caractere

Escape Characters
Other escape characters used in Python:
Code Result
\'	Single Quote
\\	Backslash
\n	New Line
\r	Carriage Return
\t	Tab
\b	Backspace
\f	Form Feed


"""



string = "Hello World!"
print(len(string)) # 12, se numara tot, inclusiv spatii, taburi, newline
string1 = " \n"
print(len(string1)) # 2, adica un spatiu, si un newline

"""
Metode pe stringuri:
Metodele sunt niste functii care se apleaza pe o anumita variabila

nume_var.metoda()

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

"""

string = "Hello World!"
print('='* 30, 'Starting string metods', '='* 30)
print(string.count('l')) # numara cate caractere l avem in string  =3
print(string.lower())    # converteste stringul la lowercase = hello world!
print(string.upper())    # converteste stringul la uppercase  = HELLO WORLD!
print(string.capitalize())  # capitalize(): Converts the first character the string to Capital Letter
print(string.endswith('d!')) # endswith(): Checks if a string ends with a specified ending
print(string.endswith('ye'))

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# format()	formats string into nicer output
first_name = 'MAdalin'
last_name = 'Chelu'
job = 'Noob'
country = 'Romania'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am MAdalin Chelu. I am a Noob. I live in Romania.


radius = 10
pi = 3.14
area = pi # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0

# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): removes any whitespace from the beginning or the end

challenge = ' thirty days of python '
print(challenge.strip())

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split():Splits String from Left

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title())  # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # True
challenge = '30 days of python'
print(challenge.startswith('thirty'))  # False


print('='* 30, 'Ending string metods', '='* 30)


# Multiline String - folosind " sau '
multiline_string = '''Ana are mere.
Ana merge la scoala.
Ana are 9 ani.'''
print(multiline_string)

# String Concatenation

first_name = 'Madalin'
last_name = 'Chelu'
space = ' '
full_name = first_name  +  space + last_name # sau folosind f strings
print(full_name) #Madalin Chelu

#### Unpacking characters

language = "Python"
a, b, c, d, e, f = language # despachetarea literelor in variabile
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

print('*' * 60)

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
# mai simplu
print(language[0])  # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
last_letter = language[last_index]
print(last_letter) # n

# Daca vrem sa incepem de la final folosim negative index - , -1 e este ultimul index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing Strings
language = 'Python'
print(len(language))
first_three = language[0:3]  # incepe de index 0 pana la index nr 3 dar nu include index 3  = "Pyt"
print(first_three)
last_three = language[3:6]
print(last_three) # hon

# alta cale
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings

language = 'Python'
pto = language[0:6:2] # 2 reprezinta pasul
print(pto) # Pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

txt = "The best things in life are free!"
print("expensive" not in txt)  # TRUE
txt = "The best things in life are free!"
if "expensive" not in txt:  #USING IF
  print("No, 'expensive' is NOT present.")
