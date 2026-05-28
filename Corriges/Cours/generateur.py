# Fichier d'exemple de generateur

# générateur simple
def generateur():
    yield 4
    yield
    yield "abc"

# appels un générateur
gen = generateur()
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print("-" * 20)

# ou boucler sur un générateur
gen = generateur()

for i in gen:
    print(i)

# le générateur ne peut etre lu qu'une fois
# et provoque une erreur de type StopIteration si on essai encore de lire
# via next() après la fin de la génération
print(list(gen))
# print(next(gen))
print("-" * 20)

# il est possible de mettre un return dans une fonction génératrice
# mais les yield suivant seront ignorés
# si on essai de refaire un next() sur le generateur,
# une exception de type StopIteration aura lieu et retournera la valeur du return
# mais pas avec une boucle for qui ignorera le return.
def generateur2():
    yield 4
    yield
    return 2
    yield "abc"

gen2 = generateur2()

while True:
    try:
        print(next(gen2))
    except StopIteration as e:
        print(e.value)
        break

print("-" * 20)

# générateur avec arguments
def fibonacci(n, a = 0, b = 1):
    for _ in range(n):
        yield a
        a, b = b, a + b

print("fibonacci commencant au debut : ", list(fibonacci(10)))
print("fibonacci commencant avec des valeurs personnalisées : ", list(fibonacci(5, 6, 7)))
print("-" * 20)

# envoi d'un paramètre à un générateur via send()
def fibonacci2(n, a = 0, b = 1):
    for _ in range(n):
        retour = yield a
        print("retour =", retour)
        a, b = b, a + b

fib = fibonacci2(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(fib.send(50))
print(next(fib))
print("-" * 20)

# ajouter une valeur à un générateur
def liste(*args):
    liste = list(args)

    # parcour des parametres
    while liste:
        # retourne elem.pop(0) et recupere le parametre envoyé par send()
        retour = yield liste.pop(0)

        # si le paramètre de send n'est pas None
        # on le rajoute à la liste générée
        if retour is not None:
            liste.append(retour)

lettres = liste("a", "b", "c")

for lettre in lettres:
    if lettre == "a":
        # send consomme une itération et renvoi "b"
        # le "b" s'affiche donc avant le "a" car il est retourné immediatement
        # par le send alors que le a est afficher seulement apres le if
        print(lettres.send("d"))

    print(lettre)

# pour eviter que le send retourne une valeur on fait un yield sans expression
# tant qu'il y a un parametre transmis
print("-" * 20)

def liste2(*args):
    elem = list(args)

    while(elem):
        retour = yield elem.pop(0)

        while retour is not None:
            elem.append(retour)
            # cette ligne permet de quitter le while car yield est comme yield None.
            retour = yield
    

lettres = liste2("a", "b", "c")

for lettre in lettres:
    if lettre is not None:
        print(lettre)

    if lettre == "b":
        lettres.send("d")
    

# sous générateur via yield from
print("-" * 20)

def longue_liste():
    yield 0
    yield from liste2(1, 2, 3)
    yield 4

# un parametres envoyer sera pris en compte dans le générateur
# avant ou après le sous générateur selon le moment de l'envoi
chiffres = longue_liste()

for chiffre in chiffres:
    print(chiffre)

print("-" * 20)

chiffres = longue_liste()
print(next(chiffres))
print(next(chiffres))
print(chiffres.send("valeur"))
print(next(chiffres))
print(next(chiffres))
print(next(chiffres))
print(next(chiffres))

# générateur en compréhension
print("-" * 20)
puissance2 = (x ** 2 for x in range(10))
print(type(puissance2))
print(sum(puissance2))

# passage d'un générateur en argument d'une fonction
print(sum((x ** 2 for x in range(10))))

# on peut enlever une paire de parenthèse
print(sum(x ** 2 for x in range(10)))

# close
print("-" * 20)
chiffres = longue_liste()
print(next(chiffres))
chiffres.close()

# print(next(chiffres)) provoque une erreur de type StopIteration
# car le générateur à été stoppé.

# exception
print("-" * 20)

def generateur3():
    for i in range(1, 10):
        try:
            yield i
        except ValueError:
            print("une erreur")

gen3 = generateur3()
print(next(gen3))
print(next(gen3))
gen3.throw(ValueError)
print(next(gen3))
