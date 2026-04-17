# Lire et écrire dans les fichiers textes
import os

def main():
    # Chemin du fichier
    CHEMIN = os.path.dirname(__file__)

    # Ouvrir un fichier pour ecriture et le créer s'il n'existe pas
    f = open(CHEMIN + "/textfile.txt", "w")

    # Ouvrir un fichier pour ajouter du contenu à la fin
    # f = open(CHEMIN + "/textfile.txt", "a")

    # Ecrire quelques lignes des données dans le fichier
    for i in range(10):
        f.write(f"Ligne {i + 1}\n")

    # Fermer le fichier à la fin des opérations
    f.close()

    # Ouvrir le fichier en mode lecture avec with
    # (permet de ne pas mettre la fonction close() car le with
    # ferme automatiquement l'environnement dès qu'on sort de celui-ci)       
    with open(CHEMIN + "/textfile.txt", "r") as f:
        # Tester que le fichier est bien ouvert en mode lecture
        if f.mode == 'r': 
            # Lire le contenu du fichier
            contenu1 = f.read()
            print(contenu1)
            f.seek(0)
            contenu2 = f.read()
            print(contenu2)
            f.seek(0)

            # Lire qu'une ligne par appel
            f1 = f.readline()
            print(f1)
            f1 = f.readline()
            print(f1)
            f.seek(0)
            
            print("lire fichier")
            while (ligne := f.readline()) != "":
                print(ligne.strip())

            # Lire les lignes individuellement dans une liste
            f.seek(0)
            fl = f.readlines()
            print()
            print(*fl, sep="")
            print()

            for x in fl:
                # On enleve le \n de la ligne du fichier
                print(x.replace("\n", ""))
                # On enleve le \n du print
                print(x, end="")
                # On ne recupere pas l'\n de l'element de la liste
                print(x[:-1])
                # On supprime tout les \n au debut et a la fin du texte de la variable x
                print(x.strip("\n")) # Ou print(x.strip())

if __name__ == "__main__":
    main()