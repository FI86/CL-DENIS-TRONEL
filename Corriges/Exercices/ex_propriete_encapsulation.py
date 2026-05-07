# Exercice propriete, encapsulation et destructeur
# Créez une classe Animal :
#     Attributs privés : _nom, _age
#     Propriétés pour accéder et modifier nom et age avec vérification (âge >= 0).
#     Une méthode parler() qui affiche "L'animal fait un bruit."
#     Un destructeur (__del__) qui affiche :
#     "{nom} a été retiré du zoo."
# Créez deux classes filles :
#     Chien, redéfinit parler() → affiche "{nom} aboie : Woof!"
#     Chat,  redéfinit parler() → affiche "{nom} miaule : Miaou!"
# Créez une fonction faire_parler(animaux) qui prend une liste d’objets Animal et appelle leur méthode parler().


# Classe Animal
class Animal:
    """Classe définisant un animal au sens général."""

    # Constructeur
    def __init__(self, nom, age):
        """Constructeur classe Animal."""
        self._nom = nom
        self._age = age

    # Proprietes
    @property
    def nom(self):
        """Getteur pour le nom de l'animal."""
        return self._nom

    @property
    def age(self):
        """Getteur pour l'age de l'animal."""
        return self._age

    @age.setter
    def age(self, value):
        """Setter pour mofier l'age."""
        if value < 0:
            raise ValueError("L'âge ne peut pas être négatif.")
        else:
            self._age = value
    
    @nom.setter
    def nom(self, nom):
        """Setter pour mofier le nom."""
        self._nom = nom

    # Methode parler
    def parler(self):
        """Methode qui fait parler un animal."""
        print(f"L'animal {self.nom} fait un bruit.")

    # Destructeur
    def __del__(self):
        """Destructeur."""
        print(f"{self.nom} a été retiré du zoo.")

    def __str__(self) -> str:
        """Affichage des infos sur l'animal."""
        return f"L'animal {self.nom} à {self.age} ans."
    

# Classe Chien
class Chien(Animal):
    """Classe définisant un chien."""
    def __init__(self, nom, age):
        """Constructeur classe Chien."""
        super().__init__(nom, age)
    
    def parler(self):
        """Methode qui fait parler un chien."""
        print(f"{self.nom} aboie : Woof!")

    def __str__(self) -> str:
        """Affichage des infos sur le chien."""
        return f"Le chien {self.nom} à {self.age} ans."


# Classe Chat
class Chat(Animal):
    """Classe définisant un chien."""
    def __init__(self, nom, age):
        """Constructeur classe Chat."""
        super().__init__(nom, age)
    
    def parler(self):
        """Methode qui fait parler le chat."""
        print(f"{self.nom} miaule : Miaou!")

    def __str__(self) -> str:
        """Affichage des infos sur le chat."""
        return f"Le chat {self.nom} à {self.age} ans."


# Fonction qui fait parler un animal
def faire_parler(animaux: list[Animal]):
    """Methode qui fait parler tous les animaux."""
    for animal in animaux:
        animal.parler()


def main():
    """Fonction principale."""
    animal = Animal("toto", 4)
    rex = Chien("Rex", 5)
    minou = Chat("Minou", 3)

    print(animal)
    print(rex)
    print(minou)
    print()

    liste_animal: list[Animal] = [animal, rex, minou]
    faire_parler(liste_animal)
    print()
    
# Programme principal
if __name__ == "__main__":
    main()

    # La fin de programme Déclenche le destrcuteur __del__ pour chaque objet crée.
