# Utilisation d'urllib pour obtenir des informations

# Imports
import requests
import urllib.request
from http.client import HTTPResponse


# =========================
# CONFIGURATION
# =========================
UTILISE_HTTPBIN = False # True = httpbin / False = w3schools

def main():
    # URL utilisée dans notre exemple
    url = "http://httpbin.org/xml" if (UTILISE_HTTPBIN) else "https://www.w3schools.com/xml/simple.xml"

    # Connaitre l'encodage du site auquel on accède.
    r = requests.get(url)
    print("encodage utilisé :", r.encoding)

    # Ouverture de l'URL pour obtenir certaines données
    with urllib.request.urlopen(url) as requete:
        requete: HTTPResponse
        # Affichage du code de retour qui devrait être 200 (OK)
        print(f"Code de retour : {requete.status}")

        # Affichage des infos d'entête
        print("Entête : ----------------------")
        print(requete.getheaders())

        # Affichage des données
        print("Données retournées : ----------------------")
        # print(requete.read().decode("us-ascii"))
        print(requete.read().decode("utf-8"))


if __name__ == "__main__":
    main()