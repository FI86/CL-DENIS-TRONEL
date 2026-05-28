# Cours sur les annotations

# Imports
import sys
from typing import Union, Optional

# Nom du module
module = sys.modules[__name__]

# Annotation de fonction / méthode simple
def addition1(x: int, y: int) -> int:
    """
    Une fonction addition
    """
    return x + y

# Annotation complex avant la v3.10
ma_variable = Union[int, float, complex]

# Annotation complex a partir de la v3.10
nombres = int | float | complex

def addition2(x: nombres, y: nombres) -> ma_variable:
    """
    Une autre fonction addition
    """
    return x + y

# Annotation seule, la variable n'est pas définie dans ce cas
valeur_min: int

# Définition d'une variable valeur_max annotée comme int
valeur_max: int = 10

# Variables avec un type optionel avant v3.10
x: Optional[int]

# Variables avec un type optionel depuis v3.10
x: int | None


# ==============
# INTROSPECTION 
# ==============

# Affichage des variables, fonctions, et classes annotées
def dump_annotations(module):
    from inspect import isfunction, isclass
    from typing import get_type_hints

    # vars() -> retourne les variables locales comme locals()
    # vars(obj) -> retourne les attributs de l'objet, comme obj.__dict__
    # vars(module) -> retourne les imports, classes, fonctions et variables du module, comme module.__dict__

    print("Variables globales :")
    print(getattr(module, "__annotations__", {}))

    print("\nFonctions :")
    for nom, obj in vars(module).items():
        if isfunction(obj):
            print(nom, get_type_hints(obj))

    print("\nClasses :")
    for nom, obj in vars(module).items():
        if isclass(obj):
            print(nom, get_type_hints(obj))


# Appel de la fonction d'introspection pour connaitre les annotations.
dump_annotations(module)
