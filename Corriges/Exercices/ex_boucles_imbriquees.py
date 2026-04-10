# Exercice boucles imbriquees
# 
# Écrivez un programme qui affiche les 20 premiers résultats de la table 
# de multiplication par un nombre entré par l’utilisateur
# Demander à l’utilisateur de rejouer.
# « Voulez-vous rejouer ? » Réponse possible oui ou non

def main():
    reponse = ""

    while reponse.upper().strip() != "NON":
        valeur = input("Quelle table de multiplication : ")

        for x in range(1, 21):
            print(f"{valeur} x {x} = {int(valeur) * x}")
        
        reponse = input("Voulez-vous rejouer ? ")

    # Ou en utilisant le walrus ":="

    while (reponse := input("Voulez-vous jouer ? ").upper().strip()) != "NON":
        valeur = input("Quelle table de multiplication : ")

        for x in range(1, 21):
            print(f"{valeur} x {x} = {int(valeur) * x}")

if __name__ == "__main__":
    main()
    