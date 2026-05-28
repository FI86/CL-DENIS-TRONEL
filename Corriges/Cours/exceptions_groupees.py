# Cours sur les exceptions groupees.
# Necessite Python 3.11+

# Classe vide heritante d'Exceptions permetant de filtrer les erreurs dans except*
class ValidationError(Exception):
    pass


# Verification d'email et age.
def verifier(email, age):
    # Liste d'errreur.
    erreurs = []

    # Si l"email n'a pas d'@.
    if "@" not in email:
        # Ajoute une exception de type ValidationError.
        erreurs.append(ValidationError("Email invalide"))

    # Si l'age est inferieur a 18 ans.
    if age < 18:
        # Ajoute une exception de type ValidationError.
        erreurs.append(ValidationError("Age minimum : 18 ans"))

    # Simulation d'un bug. Ajout d'une exception de type TypeError.
    erreurs.append(TypeError("Bug interne"))

    # Creation de l'exception groupee si une erreur est survenue.
    if erreurs:
        raise ExceptionGroup("Erreurs détectées", erreurs)


# Programme principal.
if __name__ == "__main__":
    try:
        # On fait une erreur d'email et d'age.
        verifier("toto.gmail.com", 15)

    # Recuperation de toute les erreurs de type ValidationError (la classe qu'on a cree).
    except* ValidationError as eg:
        print("\nErreurs utilisateur :")
        
        for e in eg.exceptions:
            print("-", e)

    # Recuperation de toute les erreurs de type TypeError.
    except* TypeError as eg:
        print("\nErreur technique détectée :")
        
        for e in eg.exceptions:
            print("-", e)

        print()
        # Affiche le messsage globale du groupe d'exception et le nombre d'erreur dans le groupe.
        print(eg)
        # Affiche le messsage globale du groupe d'exception.
        print(eg.args[0])
        # Affiche le nombre d'erreur dans le groupe.
        print(f"Nombre d'erreur TypeError : {len(eg.exceptions)}")

    # Creation d'une liste d'exception.
    eg = ExceptionGroup("Problèmes multiples", [
        FileNotFoundError("fichier1.txt introuvable"),
        PermissionError("fichier2.txt interdit"),
        FileNotFoundError("fichier3.txt introuvable")])

    # Filtrer et compte les FileNotFoundError via une comprehension de liste.
    cpt = len([exc for exc in eg.exceptions if isinstance(exc, FileNotFoundError)])
    print("Nombre de FileNotFoundError :", cpt)

    # Fin de try, on continue le programme.
    print("\nFin de programme.")
