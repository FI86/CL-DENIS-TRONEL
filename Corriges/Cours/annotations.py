# Annotation de fonction / méthode simple
def addition1(x: int, y: int) -> int:
    """Une fonction addition"""
    return x + y

# Annotation complex avant la v3.10 :
# from typing import Union
# nombres = Union[int, float, complex]

# Annotation complex a partir de la v3.10 :
nombres = int | float | complex

def addition2(x: nombres, y: nombres) -> nombres:
    """Une autre fonction addition"""
    return x + y

help(addition1)
help(addition2)

# Annotation de variables / attributs
# Définition d'une variable valeur_max annotée comme int
valeur_max: int = 10

# Annotation seule, la variable n'est pas définie dans ce cas
valeur_min: int

# Affichage des variables annotées
print(__annotations__)
