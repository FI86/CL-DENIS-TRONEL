# Exercice generateur
# 
# Ecrire un generateur en Python qui genere tous les nombres pairs jusqu'a un nombre donne n. 
# Le generateur doit s'arreter lorsque le nombre genere est supérieur a n.

# Generateur
def nombres_pairs(limite):
    for n in range(0, limite+1, 2):
        yield n

# Utilisation du generateur
for p in nombres_pairs(20):
    print(p)
