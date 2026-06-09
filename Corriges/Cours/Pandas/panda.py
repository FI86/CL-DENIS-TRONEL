"""
Installation necessaire :
module pandas et openpyxl
"""

# On importe les librairies
from os import path
import pandas as pd
import sqlite3  # utile pour l'exemple SQL

CHEMIN = path.dirname(__file__)

######## Fichier CSV #######
# Lire un fichier CSV
df_csv = pd.read_csv(CHEMIN + "/exemple.csv")

# Afficher les 5 premières lignes
print("=== CSV ===")
print(df_csv.head())

# Exporter vers un nouveau fichier CSV
df_csv.to_csv(CHEMIN + "/exemple_exporte.csv", index=False)

######## Fichier Excel #######
# Lire un fichier Excel (1 seule feuille)
df_excel = pd.read_excel(CHEMIN + "/exemple.xlsx", sheet_name="Feuille1")

print("=== Excel : Aperçu des données ===")
print(df_excel.head())


### Manipulations de données sur Excel ###

# 1. Sélectionner une colonne
print("\n--- Colonne 'Nom' ---")
print(df_excel["Nom"])

# 2. Filtrer les personnes dont l'âge est supérieur à 30
print("\n--- Personnes avec Age > 30 ---")
print(df_excel[df_excel["Age"] > 30])

# 3. Trier les données par âge décroissant
print("\n--- Tri par Age décroissant ---")
print(df_excel.sort_values(by="Age", ascending=False))

# 4. Ajouter une nouvelle colonne (par ex. Age dans 5 ans)
df_excel["Age+5"] = df_excel["Age"] + 5
print("\n--- Ajout d'une colonne 'Age+5' ---")
print(df_excel)

# 5. Regrouper par Ville et calculer l'âge moyen
print("\n--- Âge moyen par ville ---")
print(df_excel.groupby("Ville")["Age"].mean())

# 6. Supprimer une colonne (par ex. 'Age+5')
df_excel = df_excel.drop(columns=["Age+5"])
print("\n--- Après suppression de la colonne 'Age+5' ---")
print(df_excel.head())


# Exporter vers un nouveau fichier Excel après manipulations
df_excel.to_excel(CHEMIN + "/exemple_exporte.xlsx", index=False)


######## Fichier JSON ########
# Lire un fichier JSON
df_json = pd.read_json(CHEMIN + "/exemple.json")

# Afficher un aperçu
print("=== JSON ===")
print(df_json.head())

# Exporter en JSON
df_json.to_json(CHEMIN + "/exemple_exporte.json", orient="records", indent=4, force_ascii=False)


####### Fichier SQL ##########
# Connexion à une base SQLite
connexion = sqlite3.connect(CHEMIN + "/exemple.db")

# Lire une table SQL directement en DataFrame
df_sql = pd.read_sql("SELECT * FROM clients", connexion)

print("=== SQL ===")
print(df_sql.head())

# Exporter un DataFrame vers une nouvelle table SQL
df_sql.to_sql("clients_exportes", connexion, if_exists="replace", index=False)

# Toujours fermer la connexion
connexion.close()
