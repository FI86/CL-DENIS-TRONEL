# exemple iterateur avec les methodes __next__ et __iter__
class Impairs:
    def __init__(self, limite):
        self.__limite = limite
        self.__courant = 1  # commence à 1 (premier nombre impair)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__courant > self.__limite:
            raise StopIteration
        valeur = self.__courant
        self.__courant += 2  # on saute au nombre impair suivant
        return valeur


impairs = Impairs(25)
# code reel de la boucle for, mais a ne pas faire
try:
    it = impairs.__iter__()
    while True:
        print(it.__next__())
except StopIteration:
    pass

print()
impairs = Impairs(15)

# code normal
for elem in impairs:
    print(elem)
