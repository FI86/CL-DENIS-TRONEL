# On souhaite créer une classe Point représentant un point dans un plan
# cartésien avec des coordonnées (x, y).

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Surcharge de l'opérateur +"""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Surcharge de l'opérateur -"""
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        """Surcharge de l'affichage"""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Surcharge de la representation"""
        return "Point : (x, y)"
    

# Creation d'objet de la classe
p1 = Point(3, 4)
p2 = Point(1, 2)

# Addition des points
p3 = p1 + p2
# Soustraction des points
p4 = p1 - p2

# Affichage de p1
print("p1 :", p1)
# Affichage de p2
print("p2 :", p2)
# Affichage du resultat de l'addition
print("p1 + p2 =", p3)
# Affichage du resultat de la soustraction
print("p1 - p2 =", p4)
# Reprenstation de l'affichage de l'objet Point
print(repr(p1))