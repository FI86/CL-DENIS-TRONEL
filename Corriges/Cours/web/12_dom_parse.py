# Utilisation du module DOM pour analyser un document XML en mémoire.

# Imports.
import xml.dom.minidom as xmlmd
import requests

# ===========================
# Configuration du programme.
# ===========================
UTILISE_HTTPBIN = False


def obtenir_texte(noeud: xmlmd.Element, balise: str) -> str:
    # Cette fonction permet d'extraire le texte d'une balise XML de manière sécurisée.

    elements = noeud.getElementsByTagName(balise)

    # Si aucun élément n'est trouvé, on retourne une chaîne vide.
    if not elements:
        return ""

    child = elements[0].firstChild

    # Si le nœud texte est vide, on retourne une chaîne vide.
    if child is None:
        return ""

    # On retourne la valeur du noeud texte.
    return child.nodeValue or ""


# Fonction principale
def main():
    # On définit l'URL selon la source XML choisie.
    url = "http://httpbin.org/xml" if UTILISE_HTTPBIN else "https://www.w3schools.com/xml/simple.xml"

    try:
        # On effectue une requête HTTP pour récupérer le contenu XML.
        reponse = requests.get(url, timeout=5)

        # On vérifie que la requête a réussi.
        reponse.raise_for_status()

    except requests.exceptions.RequestException as e:
        # En cas d'erreur réseau, on affiche un message et on arrête le programme.
        print("Erreur réseau ou site indisponible")
        print(e)
        return

    # On parse le document XML pour le transformer en arbre DOM.
    domtree = xmlmd.parseString(reponse.text)

    # On récupère le noeud racine du document XML.
    racine = domtree.documentElement

    # Si le noeud racine est inexistant, on arrête le programme.
    if racine is None:
        return

    # On affiche le nom du noeud principal.
    print(f"Le noeud principal est : '{racine.nodeName}'")

    if UTILISE_HTTPBIN:
        # On affiche l'attribut title du noeud racine.
        print(f"Titre : '{racine.getAttribute('title')}'")

        # On récupère toutes les balises item et slide du document.
        items = domtree.getElementsByTagName("item")
        slides = domtree.getElementsByTagName("slide")

        # On affiche le compte des balises.
        print(f"Il y a {items.length} balise(s) item")
        print(f"Il y a {slides.length} balise(s) slide")

        # On crée une nouvelle balise item.
        nouveauItem = domtree.createElement("item")

        # On ajoute un texte à cette balise.
        nouveauItem.appendChild(domtree.createTextNode("Nouvel élément"))

        # On ajoute cet élément à la première balise slide.
        premierSlide = domtree.getElementsByTagName("slide")[0]
        premierSlide.appendChild(nouveauItem)

        # On recompte les balises item après modification.
        items = domtree.getElementsByTagName("item")
        print(f"Maintenant, il y a {items.length} balise(s) item")
    else:
        # On récupère toutes les balises food du document.
        foods = domtree.getElementsByTagName("food")

        # On affiche le nombre de balises "food".
        print(f"Nombre de Foods : {foods.length}")

        # On parcourt chaque food pour afficher ses données.
        for food in foods:
            name = obtenir_texte(food, "name")
            price = obtenir_texte(food, "price")
            calories = obtenir_texte(food, "calories")
            print()
            print("--- Food ---")
            print(f"Nom : {name}")
            print(f"Prix : {price}")
            print(f"Calories : {calories}")

        # On crée une nouvelle balise food.
        nouveauFood = domtree.createElement("food")

        # On crée et remplit la balise name.
        nom = domtree.createElement("name")
        nom.appendChild(domtree.createTextNode("Nouvel aliment"))

        # On crée et remplit la balise price.
        price = domtree.createElement("price")
        price.appendChild(domtree.createTextNode("$0"))

        # On crée et remplit la balise calories.
        calories = domtree.createElement("calories")
        calories.appendChild(domtree.createTextNode("0"))

        # On ajoute les sous-balises à la balise food.
        nouveauFood.appendChild(nom)
        nouveauFood.appendChild(price)
        nouveauFood.appendChild(calories)

        # On ajoute la nouvelle food à la racine du document XML.
        racine.appendChild(nouveauFood)

        # On recompte les balises food après modification.
        foods = domtree.getElementsByTagName("food")
        print(f"\nAprès ajout -> Foods : {foods.length}")


if __name__ == "__main__":
    main()