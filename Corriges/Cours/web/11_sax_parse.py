# Utilisation de l'analyseur xml.sax selon la source.

# Imports
import requests
import xml.sax

# =========================
# CONFIGURATION
# =========================
UTILISE_HTTPBIN = False   # True = httpbin / False = w3schools

# Définition de la sous-classe ContentHandler pour notre contenu
# Fonctionne avec des evenements
class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.buffer = ""

        self.compteur_slide = 0
        self.compteur_item = 0
        self.compteur_food = 0

        self.estTitre = False
        self.estName = False

        self.estPrix = False
        self.estCalories = False

    # startElement s'execute à chaque nouvel élément
    def startElement(self, nomBalise, attrs):
        if UTILISE_HTTPBIN:
            match (nomBalise):
                case "slideshow":
                    print(f"Titre slideshow : {attrs['title']}")
                case "slide":
                    self.compteur_slide += 1
                case "item":
                    self.compteur_item += 1
                case "title":
                    self.estTitre = True
                    self.buffer = ""
        else:
            match (nomBalise):
                case "food":
                    self.compteur_food += 1
                case "name":
                    self.estName = True
                    self.buffer = ""
                case "price":
                    self.estPrix = True
                    self.buffer = ""
                case "calories":
                    self.estCalories = True
                    self.buffer = ""
            
    # endElement s'execute à la fin de chaque élément
    # On affiche le texte cumuler dans le buffer ici
    def endElement(self, nomBalise):
        texte = self.buffer.strip()

        if UTILISE_HTTPBIN:
            match nomBalise:
                case "title": print(f"Titre : {texte}")
        else:
            match (nomBalise):
                case "name":
                    if texte: print(f"Nom : {texte}")
                case "price":
                    if texte: print(f"Prix : {texte}")
                case "calories":
                    if texte: print(f"Calories : {texte}")

    # characters s'execute quand on accède au texte d'un élément
    # on accumule le texte dans le buffer
    def characters(self, contenu):
        self.buffer += contenu

    # startDocument s'execute au début du document
    def startDocument(self):
        print("Je commence !")

    # endDocument s'execute à la fin du document
    def endDocument(self):
        print("J'ai fini !")


def main():
    # Création d'un nouveau gestionnaire de contenu avec xml.SAX
    gestionnaire = MyContentHandler()

    # Utilisation de requests pour obtenir les données XML du serveur
    # rappel : requests auto-décode le contenu
    url = "http://httpbin.org/xml" if UTILISE_HTTPBIN else "https://www.w3schools.com/xml/simple.xml"
    
    try:
        reponse = requests.get(url, timeout=5)
        reponse.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Erreur réseau ou site indisponible")
        print(e)
        return
    
    # Appel de la méthode parseString sur le contenu XML reçu.
    xml.sax.parseString(reponse.text, gestionnaire)

    # Affiche le contenu XML transformé
    print("=" * 30)
    print(f"{reponse.text}")
    print("=" * 30)

    # Affichage des quelques infos inéréssantes une fois fini.
    if UTILISE_HTTPBIN:
        print(f"Il y a {gestionnaire.compteur_slide} slides")
        print(f"Il y a {gestionnaire.compteur_item} elements")
    else:
        print(f"Foods détectés : {gestionnaire.compteur_food}")

if __name__ == "__main__":
    main()
