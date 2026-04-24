# TP gestion de fichiers
#
# L'utilisateur peut effectuer les actions suivantes :
# Creer un fichier avec un nom donne.
# Lire le contenu d'un fichier.
# Ajouter du texte a un fichier existant.
# Supprimer un fichier.
# Lister tous les fichiers dans un repertoire specifique.
# Le programme doit gerer les erreurs et les cas ou un fichier ou un repertoire est inexistant.

# Import
import os

# Fonction pour creer un fichier et y ecrire du contenu
def creer_fichier(nom_fichier, contenu=""):
    try:
        with open(nom_fichier, 'w') as fichier:
            fichier.write(contenu)

        print(f"Le fichier '{nom_fichier}' a ete cree avec succes.")
    except Exception as e:
        print(f"Erreur lors de la creation du fichier : {e}")

# Fonction pour lire le contenu d'un fichier
def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()

        print(f"Contenu du fichier '{nom_fichier}':\n{contenu}")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")

# Fonction pour ajouter du contenu dans un fichier
def ajouter_contenu(nom_fichier, contenu):
    try:
        with open(nom_fichier, 'a') as fichier:
            fichier.write(contenu)

        print(f"Le contenu a ete ajoute au fichier '{nom_fichier}' avec succes.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de contenu dans le fichier : {e}")

# Fonction pour supprimer un fichier
def supprimer_fichier(nom_fichier):
    try:
        os.remove(nom_fichier)
        print(f"Le fichier '{nom_fichier}' a ete supprime avec succes.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la suppression du fichier : {e}")

# Fonction pour lister les fichiers dans un repertoire
def lister_fichiers(repertoire):
    try:
        fichiers = [f for f in os.listdir(repertoire) if os.path.isfile(repertoire + f)]

        print(f"Fichiers dans le repertoire '{repertoire}' :")
        if fichiers:
            for fichier in fichiers:
                print(f"- {fichier}")
    except FileNotFoundError:
        print(f"Erreur : Le repertoire '{repertoire}' n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la liste des fichiers : {e}")

# Menu pour interagir avec l'utilisateur
def menu():
    # Recuperation du chemin actuel
    CHEMIN = os.path.dirname(__file__) + "/"

    while True:
        print()
        print("Gestion de fichiers :")
        print("1. Creer un fichier")
        print("2. Lire un fichier")
        print("3. Ajouter du contenu dans un fichier")
        print("4. Supprimer un fichier")
        print("5. Lister les fichiers dans un repertoire")
        print("6. Quitter")
        print()

        choix = input("Choisissez une option (1-6) : ")
        
        match choix:
            case '1' :
                nom_fichier = input("Entrez le nom du fichier a creer : ")
                contenu = input("Entrez le contenu du fichier (ou laissez vide) : ")
                creer_fichier(CHEMIN + nom_fichier, contenu)

            case '2' :
                nom_fichier = input("Entrez le nom du fichier a lire : ")
                lire_fichier(CHEMIN + nom_fichier)

            case '3' :
                nom_fichier = input("Entrez le nom du fichier a modifier : ")
                contenu = input("Entrez le contenu a ajouter: ")
                ajouter_contenu(CHEMIN + nom_fichier, contenu)

            case '4' :
                nom_fichier = input("Entrez le nom du fichier a supprimer : ")
                supprimer_fichier(CHEMIN + nom_fichier)

            case '5' :
                repertoire = input("Entrez le repertoire a lister (laisser vide pour le repertoire actuel) : ")
                if not repertoire:
                    repertoire = CHEMIN
                lister_fichiers(repertoire)

            case '6' :
                print("Au revoir !")
                print(CHEMIN)
                break

            case _ :
                print("Option invalide. Veuillez choisir une option entre 1 et 6.")

# Lancer le programme
menu()
