# Définition d'énumerations via la classe Enum
from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    POMME = 1
    CITRON = 2
    ORANGE = 3
    TOMATE = 4
    POIRE = auto()

class Status(Enum):
    HTTP_OK = 200
    HTTP_CREATED = 201
    HTTP_ACCEPTED = 202
    HTTP_NON_AUTHORITATIVE = 203
    HTTP_NO_CONTENT = 204
    HTTP_PARTIAL_CONTENT = 206
    HTTP_MULTIPLE_CHOICES = 300
    HTTP_MOVED_PERMANENTLY = 301
    HTTP_MOVED_TEMPORARILY = 302
    HTTP_SEE_OTHER = 303
    HTTP_NOT_MODIFIED = 304
    HTTP_BAD_REQUEST = 400
    HTTP_UNAUTHORIZED = 401
    HTTP_PAYMENT_REQUIRED = 402
    HTTP_FORBIDDEN = 403
    HTTP_NOT_FOUND = 404
    HTTP_METHOD_NOT_ALLOWED = 405
    HTTP_INTERNAL_SERVER_ERROR = 500
    HTTP_NOT_IMPLEMENTED = 501
    HTTP_BAD_GATEWAY = 502

def main():
    # Enum possède des valeurs et de types facilement lisible
    print(Fruit)
    print(type(Fruit.POMME))

    print(Fruit.POMME)
    print(repr(Fruit.POMME))

    # # Enum possède les propriétés nom et valeur
    print(Fruit.POIRE.name, Fruit.POIRE.value)
    print()

    # # Status
    print(Status)

    print(Status(200))
    print(Status['HTTP_UNAUTHORIZED'])
    print(Status.HTTP_BAD_REQUEST)

    print(Status(200).value)
    print(Status(200).name)
    print(Status['HTTP_OK'].value)


    # # Afficher la valeur générée automatiquement
    print(Fruit.POIRE.value)

    # # Les énumérations sont hachables.
    # # Elles peuvent être utilisées comme clés de dictionnaire
    mesFruits = {}
    mesFruits[Fruit.CITRON.name] = "Mon citron"
    print(mesFruits[Fruit.CITRON.name])
    print(mesFruits)

if __name__ == "__main__":
    main()