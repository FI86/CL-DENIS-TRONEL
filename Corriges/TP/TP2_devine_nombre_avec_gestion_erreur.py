# TP devine nombre avec gestion d'erreur
# 
# Programme ou l'utilisateur doit deviner un nombre choisi par le programme.
#
# Le programme choisit un nombre entier entre 1 et 100, et l'utilisateur doit deviner ce nombre.
# Il faut verifier la saisie de l'utilisateur afin d'eviter les erreurs de saisies possible.
# Apres chaque essai, le programme donne un indice (trop grand, trop petit ou correct).
# Une fois le nombre devine, afficher un message de reussite avec le nombre d'essai effectue.

# Import
import random

# Fonction principale
def deviner_nombre():
    # Le programme choisit un nombre aleatoire entre 1 et 100
    nombre_a_deviner = random.randint(1, 100)
    
    # Initialisation du nombre d'essais
    essais = 0
    
    print("Bienvenue dans le jeu ! Je pense a un nombre entre 1 et 100. Essaie de le deviner.")
    
    # Le jeu continue jusqu'a ce que l'utilisateur trouve le nombre
    while True:
        # Demander a l'utilisateur de deviner le nombre
        try:
            proposition = int(input("Entrez votre proposition : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        
        essais += 1
        # Comparer la proposition de l'utilisateur avec le nombre a deviner
        if proposition < nombre_a_deviner: print("C'est trop petit. Essaye encore.")
        if proposition > nombre_a_deviner: print("C'est trop grand. Essaye encore.")
        if proposition == nombre_a_deviner: 
            print(f"Bravo ! Vous avez devine le nombre {nombre_a_deviner} en {essais} essais.")
            break

# Appeler de la fonction principale.
if __file__ == "__main__":
    deviner_nombre()
