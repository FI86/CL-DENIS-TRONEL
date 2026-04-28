# Traiter une exception
nombre = input("Entrez un nombre : ")

try:
    nombre = int(nombre)
except ValueError:
    print("Désolé la valeur saisie n'est pas un nombre.")

# Double exception
try:
    numerateur = int(input("Entrez un numérateur : "))
    denominateur = int(input("Entrez un dénominateur : "))
    resultat = numerateur / denominateur
    print("Le résultat de la division est :", resultat)
except ValueError:
    print("Désolé, la valeur saisie n'est pas un nombre.")
except ZeroDivisionError:
    print("Désolé, la division par zéro n'est pas permise.")

# Récupérer le message d’une exception
nombre = input("Entrez nombre : ")

try:
    nombre = int(nombre)
except Exception as e:
    print(e)

# Sans Exception except intercepte vraiment tout
# (meme les Keyboard interrupt, SystemExit ou GeneratorExit).
# C'est generalement pas conseillé, il vaut mieux intercepter que l'ensemble des Exceptions.
print("Appuie sur Ctrl+C pour tester...")

try:
    # Interception d'un SystemExit
    # import sys
    # sys.exit(1)
    while True:
        pass  # boucle infinie sortie par ctrl+c (Keyboard interrupt)
    
except:
    print("Exception interceptée ! (même Ctrl+C)")

# Clause else
# Le bloc else permet de distinguer la partie du code qui est susceptible de 
# produire une exception de celle qui fait partie du comportement nominal du 
# code mais qui ne produit pas d’exception.
try:
    numerateur = int(input("Entrez un numérateur : "))
    denominateur = int(input("Entrez un dénominateur : "))
    resultat = numerateur / denominateur
except (ValueError, ZeroDivisionError):
    print("Désolé, quelque chose ne s'est pas bien passé.")
else:
    print("Le resultat de la division est :", resultat)

# Post-traitement
# Un bloc finally est systématique appelé même que le try soit interrompu ou non.
try:
    numerateur = int(input("Entrez un numérateur : "))
    denominateur = int(input("Entrez un dénominateur : "))
    resultat = numerateur / denominateur
except (ValueError, ZeroDivisionError):
    print("Désolé, quelque chose s'est mal passé.")
else:
    print("Le resultat de la division est :", resultat)
finally:
    print("Afficher ceci quel que soit le résultat.")

# Lever une exception
try:
    x = input("Saisissez un nombre : ")

    if int(x) < 0:
        raise ValueError("La valeur ne doit pas être négative")
except ValueError as e:
    print(e)

# Gerer une exception dans une classe dediee.
class MauvaiseValeurError(Exception):
    """Exception levée lorsque la valeur fournie est invalide."""
    
    def __init__(self, valeur, message="Valeur invalide détectée"):
        self.valeur = valeur
        self.message = f"{message} : {valeur}"
        # Appel du constructeur de la classe mère pour bien initialiser l'objet.
        super().__init__(self.message)

# Exemple d'utilisation
def traiter_valeur(x):
    if x < 0:
        raise MauvaiseValeurError(x, "La valeur ne peut pas être négative")
    
    return x * 2

try:
    resultat = traiter_valeur(-5)
except MauvaiseValeurError as e:
    print(f"Erreur capturée : {e}")


# Structure complete du try
try:
    pass
except Exception as e:
    pass
else:
    pass
finally:
    pass