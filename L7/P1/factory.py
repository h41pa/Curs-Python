"""
Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română
în limba specificata
- translations va fi un dicționar cu acele cuvinte,
exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa

- localize va fi o funcție care pentru un parametru de intrare,
ne va da traducerea lui în acea limba (exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda
(preferabil statica sau de clasa)
numita get_translator(language) –
in functie de parametrul language, returnează un translator object.

"""

from abc import ABC

class AbstractTranslator(ABC):

    def localize(self, text):
        return NotImplementedError


class EnglishTranslator(AbstractTranslator):

    def __init__(self):
        self.translations = {
            'masina': 'car',
            'om': 'human',
            'curs': 'course',
            'salut!': 'hello!'
        }

    def localize(self, text):
        if text in self.translations:
            return self.translations[text]
        print('Traducerea nu exista')

class SpanishTranslator(AbstractTranslator):

    def __init__(self):
        self.translations = {
            'masina': 'coche',
            'om': 'hombre',
            'curs': 'clase',
            'salut!': 'hola!'
        }


    def localize(self, text):
        if text in self.translations:
            return self.translations[text]
        print('Traducerea nu exista...')

class FrenchTranslator(AbstractTranslator):
    def __init__(self):
        self.translations = {
            'masina': 'voiture',
            'om': 'homme',
            'curs': 'course',
            'salut!': 'bonjour!'
        }
    def localize(self, text):
        if text in self.translations:
            return self.translations[text]

        print('Traducerea nu exista...')


class TranslatorFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_translator(language):
        if language == 'en':
            return EnglishTranslator()
        elif language == 'fr':
            return FrenchTranslator()
        elif language == 'es':
            return SpanishTranslator()
        else:
            return ValueError(f'limba nu exista {language}')


translators = []
translators.append((TranslatorFactory.get_translator('en')))
translators.append((TranslatorFactory.get_translator('fr')))
translators.append((TranslatorFactory.get_translator('es')))

for t in translators:
    print(t.localize('masina'))
