# Utilisation de requests.exceptions
import requests
from requests.exceptions import HTTPError, Timeout 

def main():
    # Utilisation de requests pour envoyer une requete HTTP GET standard
    try:
        url = "http://httpbin.org/status/404"
        url = "http://httpbin.org/delay/5"
        resultat = requests.get(url, timeout=2)
        # raise_for_status lève une exception s'il y a une erreur HTTP
        # le code est retourné dans la reponse
        resultat.raise_for_status()
        printResults(resultat)
    except HTTPError as err:
        print(f"Error: {err}")
    except Timeout as err:
        print(f"Délais dépassé de la requête : {err}")
    
def printResults(res: requests.Response):
    print(f"Code retour : {res.status_code}\n")
    print("Données retournées : ----------------------")
    print(res.text)

if __name__ == "__main__":
    main()
