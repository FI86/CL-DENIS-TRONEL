# TP Calculatrice modulaire
# 
# Module operations pour la calculatrice modulaire.
# 
# Ce module comporte les fonctions d'operations mathematiques de base.

# Addition
def addition(a, b):
    return a + b

# Soustraction
def soustraction(a, b):
    return a - b

# Multiplication
def multiplication(a, b):
    return a * b

# Division
def division(a, b):
    if b == 0:
        return "Erreur : Division par zero!"
    return a / b

# Puissance
def puissance(a, b):
    return a ** b

# Racine carre si le nombre est positif
def racine_carree(a):
    if a < 0:
        return "Erreur : Nombre negatif pour la racine carree!"
    return a ** 0.5
