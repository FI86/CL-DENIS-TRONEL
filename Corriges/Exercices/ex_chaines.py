# Exercice chaines
chaine = "Retrouvez tous les mots dans une chaine de caractères"

# 1 - Retrouvez tous les mots dans une chaine de caractères sous forme de liste
listeChaine = chaine.split()
print(*listeChaine)
print("-" * 20)

# 2 – Retrouver tous les mots qui se terminent par un caractère donné
print(*[mot for mot in listeChaine if mot.endswith("s")])
print("-" * 20)

# 3 – Retrouver tous les mots qui commencent par un caractère donné
print(*[mot for mot in listeChaine if mot.startswith("c")])
print("-" * 20)

# 4 - Retrouver tous les mots qui contiennent au moins 4 caractères
print(*[mot for mot in listeChaine if len(mot) >= 4])
print("-" * 20)

# 5 - Retrouver tous les mots qui possèdent exactement n caractères.
n = 4
print(*[mot for mot in listeChaine if len(mot) == n])
        