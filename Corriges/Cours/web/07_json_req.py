# Utilisation du module JSON

# Imports
import requests
import json

def obtenir_json(url, timeout=5) -> dict | None:
    """
    Fonction générique :
    - vérifie si le site répond
    - vérifie le code HTTP
    - sécurise le parsing JSON
    """

    try:
        # Envoi d'une requête HTTP GET
        reponse = requests.get(url, timeout=timeout)

        # Si code HTTP != 200 => erreur
        if not reponse.ok:
            print(f"[ERREUR] Site HS ou réponse invalide ({reponse.status_code}) : {url}")
            return None

        # Tentative de parsing JSON
        return reponse.json()

    except requests.exceptions.RequestException as e:
        print(f"[ERREUR RÉSEAU] Impossible d'accéder à {url}")
        print(f"Détail : {e}")
        return None

    except json.JSONDecodeError:
        print(f"[ERREUR JSON] Réponse invalide (pas du JSON) : {url}")
        return None
    

def httpbin():
    # Envoi d'une requête HTTP GET
    url = "http://httpbin.org/json"
    
    # Utilisez la fonction JSON intégrée pour renvoyer des données analysées
    donneeDico = obtenir_json(url)

    if donneeDico is None:
        print("httpbin est indisponible.")
        return
    
    print(json.dumps(donneeDico, indent=4))

    # Accès aux données JSON
    print(f"Clés : {list(donneeDico.keys())}")
    print(f"Titres : {donneeDico['slideshow']['title']}")
    print(f"Il y a {len(donneeDico['slideshow']['slides'])} slides")

def json_place_holder():
    # Envoi d'une requête HTTP GET
    url = "https://jsonplaceholder.typicode.com/todos/1"
    donneeDico = obtenir_json(url)

    if donneeDico is None:
        print("jsonplaceholder est indisponible.")
        return

    print(json.dumps(donneeDico, indent=4))

    # Accès aux données JSON (nouvelle structure)
    print(f"Clés : {list(donneeDico.keys())}")
    print(f"Titre : {donneeDico['title']}")
    print(f"Complété : {donneeDico['completed']}")


if __name__ == "__main__":
    httpbin()
    print()
    print()
    json_place_holder()
