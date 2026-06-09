# Utilisation du module urllib pour envoyer des données vers un serveur HTTP.

# Imports.
import requests
import urllib.request
import urllib.parse
from http.client import HTTPResponse

# =========================
# Configuration du programme.
# =========================
UTILISE_HTTPBIN = False # True = httpbin / False = postman


def main():
    # On choisit l'URL selon le service utilisé.
    url = "https://httpbin.org/get" if UTILISE_HTTPBIN else "https://postman-echo.com/get"


    # Connaitre l'encodage du site auquel on accède.
    r = requests.get(url)
    print("encodage utilisé :", r.encoding)

    # On crée un dictionnaire de données à envoyer au serveur.
    args = {"nom": "Francoise Hardy", "auteur": "True"}

    # On encode les données au format URL (clé=valeur&clé=valeur).
    donnee = urllib.parse.urlencode(args)

    # =========================
    # Requête HTTP GET.
    # =========================
    # On construit une requête GET avec les paramètres dans l'URL.
    # Sans header la plupart des sites modernes refusent la requete.
    req = urllib.request.Request(f"{url}?{donnee}", headers={"User-Agent": "Mozilla/5.0"})

    try:
        # On envoie la requête au serveur et on récupère la réponse.
        with urllib.request.urlopen(req) as resultat:
            # On précise le type de la réponse HTTP.
            resultat: HTTPResponse

            # On affiche le code de retour HTTP.
            print(f"Code retour : {resultat.status}")

            # On affiche les données retournées par le serveur.
            print("Données GET : ----------------------")
            print(resultat.read().decode("utf-8"))
    except Exception as e:
        # On capture les erreurs éventuelles lors de la requête GET.
        print("Erreur GET :", e)

    # =========================
    # Requête HTTP POST.
    # =========================
    # On définit l'URL de destination pour la requête POST.
    url = "https://httpbin.org/post"

    # On encode les données au format binaire pour l'envoi POST.
    donnee_post = urllib.parse.urlencode(args).encode("utf-8")

    # On construit une requête POST avec les headers nécessaires.
    req_post = urllib.request.Request(url, 
                                      data = donnee_post, 
                                      headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/x-www-form-urlencoded"}
                                      )

    try:
        # On envoie la requête POST et on récupère la réponse.
        with urllib.request.urlopen(req_post) as resultat:
            # On affiche le code de retour HTTP.
            print()
            print(f"Code retour POST : {resultat.status}")

            # On affiche les données retournées par le serveur.
            print("Données POST : ----------------------")
            print(resultat.read().decode("utf-8"))
    except Exception as e:
        # On capture les erreurs éventuelles lors de la requête POST.
        print("Erreur POST :", e)


if __name__ == "__main__":
    main()
