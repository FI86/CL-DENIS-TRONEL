"""Test sur les fichiers binaires."""

# Exemple d'acces aux fichiers binaires
import struct
import pickle 

from os import path

# Chemin du fichier
CHEMIN = path.dirname(__file__)

########### Fichier binaire avec bytearray ###########
# Ecriture dans un fichier binaire
with open(CHEMIN + "/bytearray.bin", "wb") as f:
    donnees = bytearray([72, 101, 108, 108, 111])  # équivalent a "Hello"
    f.write(donnees)
    donnees = "\ncoucou".encode("utf-8")
    f.write(donnees)

# Lecture depuis un fichier binaire
with open(CHEMIN + "/bytearray.bin", "rb") as f:
    contenu = f.read()
    # Affiche : b'Hello\ncoucou'
    print(contenu)
    # Affiche correctement
    print(contenu.decode("utf-8"))


########### Fichier binaire avec struct ###########
# Ecriture
with open(CHEMIN + "/struct.bin", "wb") as f:
    f.write(struct.pack("<i", 1234))  # 'i' signifie entier (4 octets)

# Lecture
with open(CHEMIN + "/struct.bin", "rb") as f:
    contenu = f.read()
    valeur = struct.unpack("<i", contenu)[0]
    print(valeur)  # Affiche : 1234


########### Fichier binaire avec pickle ###########
# Objets a enregistrer
score1 = {"joueur 1": 15, "joueur 2": 1, "joueur 3": 15, "joueur 4": 3}
score2 = {"joueur 1": 5, "joueur 2": 7, "joueur 3": 12, "joueur 4": 18}

# Objet a recuperer a la lecture du fichier
recupScore1 = {}
recupScore2 = {}

# Ecriture de fichier binaire
with open(CHEMIN + "/pickle.bin", "wb") as f:
    # ecriture
    pickle.dump(score1, f)
    pickle.dump(score2, f)

# Lecture de fichier binaire
with open(CHEMIN + "/pickle.bin", "rb") as f:
    # Lecture
    recupScore1 = pickle.load(f)
    recupScore2 = pickle.load(f)

print(recupScore1)
print(recupScore2)
