# Transformer un diconnaire en JSON

# Import
import json

def main():
    # Définition d'un dictionnaire
    dico = {
        "Sandwich": "Panini",
        "Sauce": True,
        "Contenu": ["Fromage",
                    "Salade",
                    "Tomate"],
        "Prix": 5}
    
    print(dico)

    # Transformation du dictionnaire en JSON
    jsonStr = json.dumps(dico, indent=4)
    
    # Affichage du JSON
    print("JSON : --------")
    print(jsonStr)

if __name__ == "__main__":
    main()