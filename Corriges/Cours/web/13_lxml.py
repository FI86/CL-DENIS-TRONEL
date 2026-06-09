# Utilisation du module lxml pour analyser un document en mémoire

# Imports
import requests
import lxml.etree as etree

UTILISE_HTTPBIN = False

# Fonction principale
def main():
    compteurSlide = 0
    compteurItem = 0

    # Utilisation de requests pour récupéree les données XML
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

    # Construction d'un ElementTree
    # reponse.content donne le contenu de resultat en byte
    doc = etree.fromstring(reponse.content)
    print(doc.tag)

    if UTILISE_HTTPBIN:
        # On accède aux differents éléments comme des listes.
        print(doc.attrib['title'])

        # Itération sur les balises slide
        for elem in doc.findall('slide'):
            # On affiche le nom de la balise courante.
            print(elem.tag)

            # On parcourt les balises title contenues dans le slide.
            for element in elem.findall('title'):
                # On affiche le texte du titre.
                print(element.text)

        # Création d'une nouvelle balise slide et on lui ajoute un texte.
        nouveauSlide = etree.SubElement(doc, "slide")
        nouveauSlide.text = "Ceci est un nouveau slide"

        # Compte le nombre des balises voulues.
        compteurSlide = len(doc.findall(".//slide"))
        compteurItem = len(doc.findall(".//item"))
        compteurItem2 = len(doc.findall("item"))

        print(f"Il y a {compteurSlide} balise(s) slide")
        print(f"Il y a {compteurItem} balise(s) item")
        print(f"Il y a {compteurItem2} balise(s) item")
    else:
        # On récupère toutes les balises food du document.
        compteurFood = len(doc.findall(".//food"))
        print(f"Foods : {compteurFood}")

        # On parcourt chaque élément food.
        for food in doc.findall(".//food"):
            # On récupère les différentes informations de l'aliment.
            name = food.findtext("name", default="")
            price = food.findtext("price", default="")
            calories = food.findtext("calories", default="")

            print()
            print("--- Food ---")
            print(f"Nom : {name}")
            print(f"Prix : {price}")
            print(f"Calories : {calories}")

        # On crée une nouvelle balise food.
        nouveau_food = etree.SubElement(doc, "food")

        # On crée la balise name, price et calories et leurs contenus.
        etree.SubElement(nouveau_food, "name").text = "Nouvel aliment"
        etree.SubElement(nouveau_food, "price").text = "$0"
        etree.SubElement(nouveau_food, "calories").text = "0"

        # On recompte les balises food après modification du document.
        compteurFood = len(doc.findall(".//food"))
        print()
        print(f"Après ajout -> Foods : {compteurFood}")

if __name__ == "__main__":
    main()