# Utilisation d'urllib.error Gestion des erreurs et des codes d'état

# Imports
import urllib.request
from urllib.error import HTTPError, URLError 
from http import HTTPStatus
from http.client import HTTPResponse

def main():
    url = "http://no-such-server.org"       # Génère URLError
    # url = "http://httpbin.org/status/404"   # Génère HTTPError
    # url = "http://httpbin.org/html"         # Devrait fonctionner

    # Utiliser la gestion des exceptions pour tenter l'accès à l'URL
    try:
        resultat: HTTPResponse = urllib.request.urlopen(url)
        print(f"Code retour : {resultat.status}")

        if (resultat.getcode() == HTTPStatus.OK):
            print(resultat.read().decode('utf-8'))
    # Se produit lorsque le serveur renvoie un code d'erreur de non-succès
    except HTTPError as err:
        print(f"Erreur : {err.code}")
    # Se produit lorsque quelque chose ne va pas avec l'URL elle-même
    except URLError as err:
        print(f"Ce serveur n'existe pas. {err.reason}")
    except Exception as e:
        print(f"Une erreur non attendue est survenue : {e}")

if __name__ == "__main__":
    main()
