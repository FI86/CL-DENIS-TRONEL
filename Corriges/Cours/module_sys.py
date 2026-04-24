# Fichier d'exemples avec le module sys.

# Import
import sys

def main():
    print("Resume des principales fonctionnalites du module sys :")
    
    # Version de Python
    print(f"\nVersion de Python : {sys.version}")
    print(f"Version info : {sys.version_info}")
    
    # Arguments de la ligne de commande
    print("\nArguments de la ligne de commande :")

    for i, arg in enumerate(sys.argv):
        print(f"Argument {i} : {arg}")
    
    sys.path.insert(0, "C:\\Windows\\temp")
    
    # Chemins de recherche des modules
    print("\nChemins de recherche des modules :")
    for path in sys.path:
        print(path)
    
    # Plateforme actuelle
    print(f"\nPlateforme actuelle : {sys.platform}")
    
    # Encodage par défaut
    print(f"\nEncodage par défaut : {sys.getdefaultencoding()}")
    
    # Taille maximale des entiers
    print(f"\nTaille maximale d'un entier : {sys.maxsize}")
    
    # Exécuter la sortie standard et d'erreur
    print("\nExemple de sortie standard :")
    sys.stdout.write("Ceci est un message sur la sortie standard.\n")
    sys.stderr.write("Ceci est un message sur la sortie d'erreur.\n")
    
    # Quitter le programme
    print("\nLe programme va se terminer avec sys.exit(0)")
    sys.exit(0)

if __name__ == "__main__":
    main()
