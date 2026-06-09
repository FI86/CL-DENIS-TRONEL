# Utilisation du module requests.auth
import requests
from requests.auth import HTTPBasicAuth

def main():
    # Accès à une URL qui demande une authentication
    # Le format de l'URL demande Nom / MDP
    url = "http://httpbin.org/basic-auth/Axel/MDP"

    # Création d'un objet HTTPBasicAuth
    ba = HTTPBasicAuth('Axel', 'MDP')

    # Envoi de la requête avec authentification
    resultat = requests.get(url, auth = ba)
    printResults(resultat)


def printResults(res: requests.Response):
    print(f"Code retour : {res.status_code}\n")
    print("Données retournées : ----------------------")
    print(res.text)

if __name__ == "__main__":
    main()
