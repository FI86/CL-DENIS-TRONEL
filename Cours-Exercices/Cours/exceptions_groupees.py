# Cours sur les exceptions groupees.
# Necessite Python 3.11+

# Classe vide heritante d'Exceptions permetant de filtrer les erreurs dans except*


# Verification d'email et age.
    # Liste d'errreur.

    # Si l"email n'a pas d'@.
        # Ajoute une exception de type ValidationError.

    # Si l'age est inferieur a 18 ans.
        # Ajoute une exception de type ValidationError.

    # Simulation d'un bug. Ajout d'une exception de type TypeError.

    # Creation de l'exception groupee si une erreur est survenue.


# Programme principal.
if __name__ == "__main__":
    pass
        # On fait une erreur d'email et d'age.

    # Recuperation de toute les erreurs de type ValidationError (la classe qu'on a cree).

    # Recuperation de toute les erreurs de type TypeError.

        # Affiche le messsage globale du groupe d'exception et le nombre d'erreur dans le groupe.

        # Affiche le messsage globale du groupe d'exception.

        # Affiche le nombre d'erreur dans le groupe.


    # Creation d'une liste d'exception.

    # Filtrer et compte les FileNotFoundError via une comprehension de liste.

    # Fin de try, on continue le programme.
