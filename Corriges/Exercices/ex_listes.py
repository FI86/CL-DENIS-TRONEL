# Exercice listes
# 
# Écrivez un programme qui analyse un par un tous les éléments d’une 
# liste de mots (par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra'])
# pour générer deux nouvelles listes.  L’une contiendra les mots comportant moins de 6 caractères, 
# l’autre les mots comportant 6 caractères ou davantage

def main():
    liste = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
    liste1 = []
    liste2 = []
    liste3 = []
    liste4 = []

    # solution 1    
    for element in liste:
        if len(element) < 6: liste1.append(element)
        else: liste2.append(element)

    # solution 2
    liste3 = [elem for elem in liste if len(elem) < 6]
    liste4 = [elem for elem in liste if len(elem) >= 6]

    print(liste1)
    print(liste2)
    print(liste3)
    print(liste4)
    
if __name__ == "__main__":
    main()
