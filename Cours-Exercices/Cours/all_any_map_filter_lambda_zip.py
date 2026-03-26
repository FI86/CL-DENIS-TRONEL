# Fichier d'exemples pour les lambda, all, any, map et filter

# all (si toutes les conditions sont vraie)

# any (si une des conditons est vraie)

# map applique une transformation à tout les éléments d'un itérable
# (une fois le map parcouru le curseur ne revient pas et n'est pas réutilisable)

# Conversion en liste d'un map

# filter : filtre avec un prédicat les éléments d'un itérable et retourne un booléen

# lambda

# Fonction native zip
    # La taille du tuple et de la liste de nombres sont different.
    # Convertir en liste car zip est un iterateur (comme map et filter)

    # Option strict=True (strict=False par defaut) depuis la version 3.10.

    # Genere une erreur "ValueError" car les listes ne sont pas de la meme longueur
    # resultat = list(zip(listeNombres, tupleNombres, strict=True))
    # print(resultat)

    # Dezipper


# Fonction principale
def main():
    pass
    # Appel par fonction sans lambda

    # Appel avec lambda on a plus besoin des fonctions qui sont utilisées qu'une fois.

    # Appel la fonction pour zipper et dezipper.


if __name__ == "__main__":
    main()