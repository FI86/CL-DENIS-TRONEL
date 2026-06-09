# Exercice fichier binaire
# 
# Creer un programme Python qui :
#   Cree une liste de nombres entiers.
#   Ecrit ces nombres dans un fichier binaire avec struct, bytearray et/ou pickle.
#   Relit le fichier binaire.
#   Affiche les nombres lus a l'ecran.
# 
# Les fichiers binaires s'appelleront : nombres_bytearray.bin, nombre_struct.bin et/ou nombre_pickle.bin

# Imports
import struct
import pickle
from os import path

# Chemin du fichier
CHEMIN = path.dirname(__file__)

# Cree une liste de nombres entiers.
nombres = [10, 20, 30, 40, 50]

# Ouvre un fichier binaire en mode ecriture.
fichier_struct = open(CHEMIN + "/nombres.bin", "wb")
fichier_pickle = open(CHEMIN + "/nombres_pickle.bin", "wb")
fichier_bytearray = open(CHEMIN + "/nombres_bytearray.bin", "wb")

### Avec Struct ###
# Parcourt chaque nombre de la liste.
for nombre in nombres:
    # Transforme le nombre en format binaire.
    data = struct.pack("i", nombre)
    # Ecrit le nombre dans le fichier.
    fichier_struct.write(data)

### Avec pickle ###
# Enregistre la liste dans le fichier.
pickle.dump(nombres, fichier_pickle)

### Avec bytearray ###
# Cree un tableau binaire a partir de la liste.
# Puis ecrite ce tableau dans le fichier.
donnees = bytearray(nombres)
fichier_bytearray.write(donnees)

# Ferme le fichier apres ecriture.
fichier_struct.close()
fichier_pickle.close()
fichier_bytearray.close()

# Ouvre le fichier binaire en mode lecture.
fichier_struct = open(CHEMIN + "/nombres.bin", "rb")
fichier_pickle = open(CHEMIN + "/nombres_pickle.bin", "rb")
fichier_bytearray = open(CHEMIN + "/nombres_bytearray.bin", "rb")

# Cree une liste vide pour stocker les nombres lus.
nombres_lus_struct = []
nombres_lus_pickle = []
nombres_lus_bytearray = []

### Avec struct ###
# Lit le fichier tant qu il reste des donnees.
while True:
    # Lit 4 octets depuis le fichier.
    data = fichier_struct.read(4)
    # Verifie si la lecture est terminee.
    if not data:
        break
    # Convertit les octets en entier.
    nombre = struct.unpack("i", data)[0]
    # Ajoute le nombre a la liste.
    nombres_lus_struct.append(nombre)

### Avec pickle ###
# Lit la liste depuis le fichier.
nombres_lus_pickle = pickle.load(fichier_pickle)

### Avec bytearray ###
# Lit le fichier et transforme en liste.
nombres_lus_bytearray = list(fichier_bytearray.read())

# Ferme le fichier apres lecture.
fichier_struct.close()
fichier_pickle.close()
fichier_bytearray.close()

# Affiche les nombres lus depuis le fichier.
print(f"Nombres lus avec struct : {nombres_lus_struct}")
print(f"Nombres lus avec pickle : {nombres_lus_pickle}")
print(f"Nombres lus avec bytearray : {nombres_lus_bytearray}")
