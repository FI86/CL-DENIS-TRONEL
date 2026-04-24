# TP Calculatrice modulaire
# 
# Module menu de la calculatrice modulaire.
#
# Ce module contient 3 fonctions qui permettent :
# L'affichage d'un menu.
# La saisie du choix dans ce menu.
# La saisie d'un nombre qui sera utilise pour le calcul choisi.

# Afficher le menu
def afficher_menu():
    print()
    print("Bienvenue dans la calculatrice modulaire !")
    print("Choisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance")
    print("6. Racine carree")
    print("7. Quitter")
    print()

# Choix dans le menu
def demander_choix():
    return input("Entrez le numero de l'operation (1 a 7) : ")

# Demander un nombre (pour le calcul)
def demander_nombre(message):
    while True:
        try:
            return float(input(message))
        except Exception:
            print("Erreur de saisie.")
            continue