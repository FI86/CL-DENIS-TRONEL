# Traiter les données JSON renvoyées par un serveur

# Import
import json

def main():
    # Définition d'une string JSON
    jsonStr = '''{
            "Sandwich" : "Panini",
            "Sauce" : true,
            "Contenu" : [
                "Fromage",
                "Salade",
                "Tomate"],
            "Prix" : 5}'''

    try:
        # Transformation du JSON en dictionnaire
        dico = json.loads(jsonStr)

        # Affichage du contenu du JSON
        print(f"Sandwich: {dico['Sandwich']}")
        print("Il y a de la sauce !" if (dico['Sauce']) else "Il n'y a pas de sauce !")
        
        for contenu in dico['Contenu']:
            print(f"contient : {contenu}")

    except json.JSONDecodeError as err:
        print(f"JSON = {jsonStr}")
        print("Oups, Erreur de décodage du JSON :")
        print(f"Message d'erreur : {err.msg}")
        print(f"Ligne N° : {err.lineno} - Colonne N° : {err.colno}")

if __name__ == "__main__":
    main()
