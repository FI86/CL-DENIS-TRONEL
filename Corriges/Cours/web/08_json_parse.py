# Transformer un JSON en dictionnaire

# Imports
import json

def main():
    # Définition d'une string JSON
    jsonStr = '''{
            "Sandwich" : "Panini",
            "Sauce" : true,
            "Contenu" : ["Fromage", "Salade", "Tomate"],
            "Prix" : 5}'''

    # Utilisation de loads() pour une chaîne JSON
    # On utilise load() s'il sagit du contenu d'un fichier à convertir.
    dico = json.loads(jsonStr)
    print(type(dico))
    print(type(dico["Sauce"]))
    print(type(dico["Contenu"]))
    print(type(dico["Prix"]))
    
    # Affiche les informations contenu dans la strcuture JSON
    print(f"Sandwich : {dico['Sandwich']}")
    print("Il y a de la sauce !" if (dico['Sauce']) else "Il n'y a pas de sauce !")
    
    for ingredients in dico['Contenu']:
        print(f"ingredients : {ingredients}")

if __name__ == "__main__":
    main()
