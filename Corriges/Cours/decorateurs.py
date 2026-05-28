# decorateur simple retournant la fonction d'origine
def decorateur(fonction):
    print(f"Nom de la fonction : {fonction.__name__}")
    return fonction

# fonction simple auquel le decorateur est appliqué
# equivaut à : # decorateur(addition1(x, y))
@decorateur
def addition1(x, y):
    return x + y

print(f"resultat = {addition1(10, 5)}")
print("-" * 20)

# Décorateur créant une nouvelle fonction qui affiche les nombres ainsi que 
# le retour de l'appel de la fonction original
def decorateur2(fonction):
    # Nouvelle fonction se comportant comme la fonction à décorer
    def nouvelle_fonction(a, b):
        print(f"Addition des nombres{a} et {b}")
        # Appel de la fonction originale
        retour = fonction(a, b)
        print(f"{retour = }".capitalize())
        return retour
    # Ne pas oublier de retourner notre nouvelle fonction
    return nouvelle_fonction

# decorateur2(addition2x, y))
@decorateur2
def addition2(x, y):
    return x + y

print(f"resultat = {addition2(10, 5)}")
print("-" * 20)

# decorateur(decorateur2(addition3(x, y)))
@decorateur
@decorateur2
def addition3(x, y):
    return x + y

print(f"resultat = {addition3(10, 5)}")
print("-" * 20)

# decorateur2(decorateur(addition4(x, y)))
@decorateur2
@decorateur
def addition4(x, y):
    return x + y

print(f"resultat = {addition4(10, 5)}")
print("-" * 20)

# décorateur avec paramètres
def decoRepeter(nbFois):
    # décorateur
    def decorateur(fonction):
        def nouvelleFonction(*args, **kwargs):
            for i in range(nbFois):
                print(f"répétition : {i}")
                resultat = fonction(*args, **kwargs)

            return resultat

        return nouvelleFonction

    return decorateur
            
@decoRepeter(5)
def addition5(x, y):
    return x + y

print(f"resultat = {addition5(5, 10)}")
print("-" * 20)

# récupération des informations docstring d'une fonction décorée.
from functools import wraps

def decorateur3(f):
    """ mon décorateur"""
    @wraps(f)
    def fonction(*args, **kwargs):
        return f(*args, **kwargs)
    
    return fonction

@decorateur3
def addition6(x, y):
    """mon docstring"""
    return x + y

print(f"resultat = {addition6(5, 10)}")
help(addition6)
help(decorateur3)
