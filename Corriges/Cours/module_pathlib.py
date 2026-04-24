# Fichier d'exemples avec le module pathlib

# Imports
from pathlib import Path
import datetime
import time
import platform

def main():
    CHEMIN = Path(__file__).parent
    ELEM = CHEMIN / "osFichierTest.txt"
    # Afficher le chemin courant, le nom de l'OS
    print(CHEMIN)
    print(Path(ELEM).name)
    print(Path.cwd())
    print(platform.system())

    # Vérification de l'existence d'un élément et de son type
    print(f"L'élément existe : {ELEM.exists()}")
    print(f"L'élément est un fichier : {ELEM.is_file()}")
    print(f"L'élément est un dossier : {ELEM.is_dir()}")

    # Manipuler les informations sur le chemin du fichier
    print(f"Le chemin du fichier : {ELEM.resolve()}")
    print(f"Le chemin du fichier et sa désignation : {ELEM.resolve().parent, ELEM.name}")

    # Obtenir la date de modification du fichier
    print(f"Date de modification du fichier : {time.ctime(ELEM.stat().st_mtime)}")
    print(f"Date de modification du fichier : {datetime.datetime.fromtimestamp(ELEM.stat().st_mtime)}")

    # Calculer le temps écoulé depuis la dernière modification
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(ELEM.stat().st_mtime)
    print(f"Il s'est passé {td} depuis la dernière modification")
    print(f"Ou, {td.total_seconds()} secondes")

    # Gestion de fichier texte
    # Suppression du fichier
    ELEM.unlink()

    # Ecriture initiale (creation du fichier si non existant)
    ELEM.write_text("Bonjour !\n")

    # Modification : on lit l'ancien contenu puis on ajoute du texte
    ancien_contenu = ELEM.read_text()
    nouveau_contenu = ancien_contenu + "Ligne ajoutée.\n"
    ELEM.write_text(nouveau_contenu)

    # Lecture finale
    contenu = ELEM.read_text()
    print(contenu)

    # Suppression du contenu
    ELEM.write_text("")
    print("fichier vidé.")


if __name__ == "__main__":
    main()
