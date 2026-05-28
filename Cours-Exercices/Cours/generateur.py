# Fichier d'exemple de generateur

# générateur simple


# appels un générateur


# ou boucler sur un générateur


# le générateur ne peut etre lu qu'une fois
# et provoque une erreur de type StopIteration si on essai encore de lire
# via next() après la fin de la génération


# il est possible de mettre un return dans une fonction génératrice
# mais les yield suivant seront ignorés


# générateur avec arguments


# envoi d'un paramètre à un générateur via send()


# ajouter une valeur à un générateur

    # parcour des parametres

        # retourne elem.pop(0) et recupere le parametre envoyé par send()

        # si le paramètre de send n'est pas None
        # on le rajoute à la liste générée

        # send consomme une itération et renvoi "b"
        # le "b" s'affiche donc avant le "a" car il est retourné immediatement
        # par le send alors que le a est afficher seulement apres le if


# pour eviter que le send retourne une valeur on fait un yield sans expression
# tant qu'il y a un parametre transmis

            # cette ligne permet de quitter le while car yield est comme yield None.


# sous générateur via yield from

# un parametres envoyer sera pris en compte dans le générateur
# avant ou après le sous générateur selon le moment de l'envoi

# générateur en compréhension

# passage d'un générateur en argument d'une fonction

# on peut enlever une paire de parenthèse

# close

# print(next(chiffres)) provoque une erreur de type StopIteration
# car le générateur à été stoppé.

# exception

