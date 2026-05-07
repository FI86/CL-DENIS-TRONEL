# Se connecter avec un mot de passe puis ouvrir des fenêtres

        # Fenetre transitoire. Elle apparait toujours devant sa fenetre parent.
        # Si la fenetre parents est iconifiée, la fenetre transitoire aussi.

        # On utilise grab_set() pour que la fenêtre Toplevel puisse recevoir des événements
        # et empêcher les utilisateurs d'interagir avec la fenêtre principale. 
        #        
        # annulation du clic sur la croix de la fenetre


    # ferme les fenetres 1 et 2 et supprimer leurs objets respectif
    # pour permette de quitter la fenetre pricipale


    # raccourci clavier

        # il est possible de ne pas indiquer "event" en parametre de fonction,
        # mais dans ce cas il faut utiliser "lamdbda event: fonction()" pour le binding

    # quitte la fenetre principale si les deux autres fenetres sont fermer
