# Exercice fichier
# 
# Ecrivez un script qui génère automatiquement un fichier texte 
# contenant les tables de multiplication de 2 à 30
# (chacune d’entre elles incluant les termes de 1 à 20 seulement).

import os

def main():
    CHEMIN = os.path.dirname(__file__)

    with open(CHEMIN + "/tables_multiplication (ex. 10).txt", "wt") as f:
        for table in range(2, 31):
            f.write(f"Table de multiplication par {table} : \n") 

            for x in range(1, 21):
                f.write(f"{table} x {x} = {table * x}\n")

if __name__ == "__main__":
    main()
