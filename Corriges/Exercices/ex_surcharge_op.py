# Exercice surcharge op
# 
# On souhaite modeliser une classe Rectangle representant un rectangle dans un plan cartesien.
# Un rectangle est defini par :
#     Sa largeur (largeur)
#     Sa hauteur (hauteur)
#
# Vous devez :
# 
# Implementer la classe Rectangle avec un constructeur prenant en parametre largeur et hauteur.
# Surcharger les operateurs suivants :
#     +   : pour additionner deux rectangles (somme des largeurs et hauteurs respectives).
#     *   : pour multiplier un rectangle par un entier (multiplier la largeur et la hauteur).
#     ==  : pour comparer si deux rectangles ont la meme surface.
#     str : pour afficher un rectangle sous la forme "Rectangle(largeur, hauteur)".
# Tester la classe avec differents cas.

# Classe Rectangle
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def __add__(self, other):
        """Surcharge de l'operateur + (addition des dimensions)"""
        if isinstance(other, Rectangle):
            return Rectangle(self.largeur + other.largeur, self.hauteur + other.hauteur)
        
        return NotImplemented

    def __mul__(self, facteur):
        """Surcharge de l'operateur * (multiplication des dimensions)"""
        # Verifie que le facteur est un entier
        if isinstance(facteur, int):
            return Rectangle(self.largeur * facteur, self.hauteur * facteur)
        else:
            raise TypeError("Le facteur doit etre un entier")

    def __eq__(self, other):
        """Surcharge de l'operateur == (comparaison de surface)"""
        if isinstance(other, Rectangle):
            return (self.largeur * self.hauteur) == (other.largeur * other.hauteur)
        
        return NotImplemented

    def __str__(self):
        """Surcharge de l'affichage"""
        return f"Rectangle({self.largeur}, {self.hauteur})"


# Programme principale
def main():
    # Creation d'objet
    r1 = Rectangle(4, 5)
    r2 = Rectangle(2, 3)

    # Addition des rectangles
    r3 = r1 + r2

    # Multiplication par un entier
    r4 = r1 * 2
    
    # Rectangle avec meme surface
    r5 = Rectangle(10, 2)

    # Affichage des resultats
    print("r1 :", r1)
    print("r2 :", r2)
    print("r1 + r2 =", r3)
    print("r1 * 2 =", r4)
    print("r1 et r5 ont-ils la meme surface ?", r1 == r5)

# Execution du programme principal
if __name__ == "__main__":
    main()
