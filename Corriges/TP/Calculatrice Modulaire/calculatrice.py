# TP Calculatrice modulaire
# 
# Programme principal de la calculatrice modulaire.
#
# Ecrire le code d'une calculatrice qui permet a l'utilisateur de realiser
# des operations mathematiques de base telles que l'addition, la soustraction,
# la multiplication, la division, la puissance et la racine carrée.

# Imports des modules necessaires.
import operations as op
import menu

# Fonction Principale
def calculatrice():
    while True:
        menu.afficher_menu()

        # Demander a l'utilisateur de choisir une option
        choix = menu.demander_choix()

        match choix:
            # Quitter
            case '7':
                print("Au revoir!")
                break
            
            # Racine carree
            case '6':
                a = menu.demander_nombre("Entrez un nombre : ")
                print(f"Resultat : {op.racine_carree(a)}")
            
            # Autres choix du menu
            case '1' | '2' | '3' | '4' | '5':
                a = menu.demander_nombre("Entrez le premier nombre : ")
                b = menu.demander_nombre("Entrez le deuxieme nombre : ")

                # Operations autres que la racine carree
                match choix:
                    case '1': print(f"Resultat : {op.addition(a, b)}")
                    case '2': print(f"Resultat : {op.soustraction(a, b)}")
                    case '3': print(f"Resultat : {op.multiplication(a, b)}")
                    case '4': print(f"Resultat : {op.division(a, b)}")
                    case '5': print(f"Resultat : {op.puissance(a, b)}")
            # Choix en dehors du menu
            case _:
                print("Choix invalide, veuillez essayer a nouveau.")

# Lancer la calculatrice
if __name__ == "__main__":
    calculatrice()
