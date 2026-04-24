# TP gestion parc vehicule
# 
# Vous travaillez pour une societe qui gere un parc de vehicules.
# Ce parc contient differents types de vehicules, tels que des voitures et des camions.
# Vous devez developper un programme en Python pour gerer ce parc en utilisant
# des classes et l’heritage.

# Creation de la classe de base Vehicule :
# Cette classe doit inclure les informations de base communes a tous les vehicules,
# telles que la marque, le modele, l'annee de fabrication, et le numero d'immatriculation.
# La classe doit egalement disposer d'une methode pour afficher ces informations
# sous forme de chaîne de caracteres.

# Creation de la classe Voiture qui herite de Vehicule :
# La classe Voiture doit etendre la classe Vehicule en ajoutant un attribut supplementaire,
# le nombre de portes.
# La classe Voiture doit redefinir la methode d'affichage des informations pour
# inclure le nombre de portes.

# Creation de la classe Camion qui herite de Vehicule :
# La classe Camion doit etendre la classe Vehicule en ajoutant un attribut supplementaire,
# la capacite de charge maximale (en kilogrammes).
# La classe Camion doit redefinir la methode d'affichage des informations pour
# inclure la capacite de charge.

# Creation de la classe ParcVehicules :
# La classe ParcVehicules doit gerer un ensemble de vehicules, c’est-a-dire une
# liste de vehicules.
# Elle doit permettre d’ajouter un vehicule au parc a l’aide d’une methode ajouter_vehicule.
# Elle doit egalement permettre d’afficher tous les vehicules presents dans le parc
# a l’aide d’une methode afficher_parc.

# Classe de base pour un vehicule
class Vehicule:
    def __init__(self, marque, modele, annee, immatriculation):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.immatriculation = immatriculation

    def afficher_details(self):
        return f"{self.marque} {self.modele} ({self.annee}) - Immatriculation: {self.immatriculation}"


# Classe derivee pour les voitures
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, immatriculation, nombre_portes):
        super().__init__(marque, modele, annee, immatriculation)
        self.nombre_portes = nombre_portes

    def afficher_details(self):
        return f"{super().afficher_details()} - {self.nombre_portes} portes"


# Classe derivee pour les camions
class Camion(Vehicule):
    def __init__(self, marque, modele, annee, immatriculation, capacite_charge):
        super().__init__(marque, modele, annee, immatriculation)
        self.capacite_charge = capacite_charge

    def afficher_details(self):
        return f"{super().afficher_details()} - Capacité de charge: {self.capacite_charge} kg"


# Classe de gestion de parc de vehicules
class ParcVehicules:
    def __init__(self):
        self.vehicules: list[Vehicule] = []

    def ajouter_vehicule(self, vehicule: Vehicule):
        self.vehicules.append(vehicule)

    def afficher_parc(self):
        if not self.vehicules:
            print("Le parc est vide.")
        else:
            for vehicule in self.vehicules:
                print(vehicule.afficher_details())


# Programme Pincipal
def main():
    parc = ParcVehicules()

    # Creation d'objets de véhicules (Voitures et Camion)
    voiture1 = Voiture("Toyota", "Corolla", 2020, "AB-123-CD", 4)
    voiture2 = Voiture("Honda", "Civic", 2018, "EF-456-GH", 4)
    camion1 = Camion("Volvo", "FH16", 2021, "IJ-789-KL", 20000)

    # Ajout de véhicules
    parc.ajouter_vehicule(voiture1)
    parc.ajouter_vehicule(voiture2)
    parc.ajouter_vehicule(camion1)

    # Affichage du parc de véhicules
    parc.afficher_parc()

# Execution du programme principal
if __name__ == "__main__":
    main()
    