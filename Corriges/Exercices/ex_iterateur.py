# Exercice iterateur
# 
# Ecris une classe CompteurPair qui est un itérateur.
# Cet itérateur renvoie les nombres pairs à partir d’un entier de départ donné (debut),
# jusqu’à une valeur maximale (fin, exclusive).
# La méthode __iter__() doit retourner self.
# La méthode __next__() doit retourner le prochain nombre pair ou lever StopIteration quand la limite est atteinte.
# Le debut peut être pair ou impair, mais l’itérateur ne doit retourner que les pairs >= debut.

class CompteurPair:
    def __init__(self, debut=2, fin=20):
        if isinstance(debut, int | float):
            debut = int(debut)
            # Commence au premier pair >= debut.
            self.__courant = debut if debut % 2 == 0 else debut + 1
        else:
            self.__courant = 2

        self.__fin = int(fin) if isinstance(fin, int | float) else 20

    def __iter__(self):
        return self

    def __next__(self):
        if self.__courant > self.__fin:
            raise StopIteration
        
        nbr_pair = self.__courant
        self.__courant += 2
        # Ou faire a, b = b, b+2
        # nbr_pair, self.__courant = self.__courant, self.__courant + 2
        return nbr_pair


def main():
    compteur = CompteurPair(5, 15)

    for nombre in compteur:
        print(nombre)

if __name__ == "__main__":
    main()
