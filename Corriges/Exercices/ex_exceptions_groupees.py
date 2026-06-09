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
fichiers = ["fichier1.txt", "fichier2.txt", "fichier3.txt"]

# Creer une liste pour stocker les exceptions.
exceptions = []

# Parcourir chaque fichier et simuler des erreurs.
for fichier in fichiers:
    try:
        # Utiliser match-case pour simuler les erreurs selon le fichier.
        match fichier:
            case "fichier1.txt" | "fichier3.txt":
                # Simuler un fichier introuvable.
                raise FileNotFoundError(f"{fichier} introuvable.")
            case "fichier2.txt":
                # Simuler un probleme de permission.
                raise PermissionError(f"{fichier} interdit.")
            case _:
                # Simuler une lecture reussie.
                print(f"{fichier} lu avec succes.")
    except Exception as e:
        # Ajouter l'exception a la liste.
        exceptions.append(e)

# Creer un ExceptionGroup avec toutes les exceptions.
eg = ExceptionGroup("Erreur lors du traitement des fichiers.", exceptions)

# Afficher le message global pur sans le nombre de sous-exceptions.
print("Message global :", eg.args[0])

# Affiche le nombre de FileNotFoundError.
# Solution 1 : en utilisant une comprehension de liste.
# Filtrer et compter les FileNotFoundError dans le groupe.
nb_fichiers_introuvables = len([exg for exg in eg.exceptions if isinstance(exg, FileNotFoundError)])
print(f"Solution 1 : Nombre de fichiers introuvables : {nb_fichiers_introuvables}")


# Solution 2 : en utilisant except*
# Utiliser except* pour filtrer les FileNotFoundError dans le groupe.
try:
    # Capturer uniquement les FileNotFoundError.
    raise eg
except* FileNotFoundError as fnfe:
    # Afficher le nombre de fichiers introuvables.
    print("Solution 2 : Nombre de fichiers introuvables :", len(fnfe.exceptions))
except* PermissionError as pe_group:
    pass
    # print("Nombre de fichiers interdits :", len(pe_group.exceptions))


# Solution 3 : si beaucoup de type d'exception different.
# Liste de tous les types a capturer.
types = [FileNotFoundError]
dico = {"FileNotFoundError": "Fichiers introuvables", 
        "PermissionError" : "erreur de permission"}

# Boucle sur chaque type pour compter les exceptions.
for type in types:
    nb = len([exception for exception in eg.exceptions if isinstance(exception, type)])
    
    if type is FileNotFoundError:
        # Affichage personalise.
        print(f"Solution 3 : Nombre de {dico[type.__name__].lower()} : {nb}")
        # Affichage avec le type.
        print(f"Solution 3 : Nombre de {type.__name__} :", nb)


# Suite du programme.
# Afficher chaque message d'exception individuel.
print("Details des exceptions :")

for exception in eg.exceptions:
    print("-", exception)
