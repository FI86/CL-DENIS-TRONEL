# Exercice iterateur
# 
# Ecris une classe CompteurPair qui est un itérateur.
# Cet itérateur renvoie les nombres pairs à partir d’un entier de départ donné (debut),
# jusqu’à une valeur maximale (fin, exclusive).
# La méthode __iter__() doit retourner self.
# La méthode __next__() doit retourner le prochain nombre pair ou lever StopIteration quand la limite est atteinte.
# Le debut peut être pair ou impair, mais l’itérateur ne doit retourner que les pairs >= debut.

class CompteurPair:
    def __init__(self, debut, fin):
        self.__courrant = debut if debut % 2 == 0 else debut + 1  # commence au premier pair >= debut
        self.__fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.__courrant >= self.__fin:
            raise StopIteration
        valeur = self.__courrant
        self.__courrant += 2
        return valeur


def main():
    compteur = CompteurPair(3, 11)
    for nombre in compteur:
        print(nombre)

if __name__ == "__main__":
    main()
