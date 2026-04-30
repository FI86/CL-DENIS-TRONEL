# Exemple de destructeur

# Classe Tableau
class Tableau:
    # limitation de la création des attributs à ceux indiqués
    __slots__ = ('tableau')

    # Constructeur de la classe
    def __init__(self):
        # Initialiser le tableau avec 100 éléments
        self.tableau = [0] * 100
    
    # Destructeur de la classe
    def __del__(self): 
        print("Je suis le destructeur")
 
        # Vider le tableau
        self.tableau.clear()
 
 
tab1 = Tableau()
tab2 = Tableau()
tab2.tableau = [1, 2, 3]

# erreur si on creer un attribut suplementaire non prévu dans __slots__
# si on enlèvle __slots__ c'est possible sans erreur
# tab2.autre = 0

# Execution du destructeur pour l'objet tab1
del tab1
print("fin de programme")
# Execution du destructeur pour l'objet tab2 à la fin du programme
