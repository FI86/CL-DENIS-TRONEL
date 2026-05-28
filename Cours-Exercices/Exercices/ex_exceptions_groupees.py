# Exercice sur les exceptions groupees.
# 
# Cree une liste de fichiers : contenant les noms (fichier1.txt, fichier2.txt, fichier3.txt)
# Parcourir cette liste et essayer de simuler la lecture de chaque fichier :
#       Pour fichier1.txt et fichier3.txt, lever un FileNotFoundError.
#       Pour fichier2.txt, lever un PermissionError.
# 
# Regroupe toutes ces exceptions dans un ExceptionGroup avec un message global :
# "Erreur lors du traitement des fichiers".
# 
# Afficher :
#       Le message global pur.
#       Le nombre de FileNotFoundError.
#       Chaque message individuel.
# 
# Exemple d'affichage attendu :
# 
# Message global : Erreur lors du traitement des fichiers.
# Nombre de fichiers introuvables : 2
# Details des exceptions :
# - fichier1.txt introuvable.
# - fichier2.txt interdit.
# - fichier3.txt introuvable.



# Creer une liste de fichiers a traiter.

# Creer une liste pour stocker les exceptions.

# Parcourir chaque fichier et simuler des erreurs.
        # Utiliser match-case pour simuler les erreurs selon le fichier.
                # Simuler un fichier introuvable.

                # Simuler un probleme de permission.

                # Simuler une lecture reussie.

        # Ajouter l'exception a la liste.

# Creer un ExceptionGroup avec toutes les exceptions.

# Afficher le message global pur sans le nombre de sous-exceptions.

# Filtrer et compter les FileNotFoundError dans le groupe.

# Afficher chaque message d'exception individuel.
