# Utilisation du module requests

# Import
import requests

# =========================
# CONFIGURATION
# =========================
UTILISE_HTTPBIN = False # True = httpbin / False = postman ou w3school

def afficheResultat(res: requests.Response):
    print(f"Code retour : {res.status_code}")
    print()
    print("Entêtes : ----------------------")
    print(f"{res.headers}")
    print()
    print("Données retournées : ----------------------")
    print(res.text)
    
def main():
    # Utilisation de requests pour envoyer une requete HTTP GET standard
    url = "http://httpbin.org/xml" if UTILISE_HTTPBIN else "https://www.w3schools.com/xml/simple.xml"
    resultat = requests.get(url)
    afficheResultat(resultat)
    
    # Envoi de paramètres à une URL via une reqête GET
    # Notez que requests s'en chargent pour vous, pas d'encodage manuel
    # et retourne les résultats sous forme JSON
    parametres = {'cle1' : 'valeur1', 'cle2' : 'valeur2'}
    
    url = "https://httpbin.org/get" if UTILISE_HTTPBIN else "https://postman-echo.com/get"
    resultat = requests.get(url, params = parametres)
    afficheResultat(resultat)

    # Envoi de paramètres à une URL via une reqête POST
    url = "https://httpbin.org/post" if UTILISE_HTTPBIN else "https://postman-echo.com/post"
    resultat = requests.post(url, data = parametres)
    afficheResultat(resultat)

    # Envoi d'une entête personalisée à un serveur
    url = "https://httpbin.org/get" if UTILISE_HTTPBIN else "https://postman-echo.com/get"
    entete = {'User-Agent' : 'mon user agent'}
    resultat = requests.get(url, headers = entete)
    afficheResultat(resultat)

if __name__ == "__main__":
    main()
