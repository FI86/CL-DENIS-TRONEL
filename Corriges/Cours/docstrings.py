# ============================================
# DOCSTRING DU MODULE (choisir un seul style)
# ============================================

# ----- Style PEP 257 -----
"""
Ce module gère des opérations simples sur des comptes bancaires.

Contient :
- Une classe CompteBancaire
- Deux fonctions : calcul_interet et convertir_euros_dollars
"""

# ----- Style Google -----
"""
Ce module fournit des opérations bancaires simples.

Modules:
    CompteBancaire: Classe représentant un compte bancaire.
    calcul_interet: Fonction pour calculer des intérêts.
    convertir_euros_dollars: Fonction de conversion de devise.

Exemple:
    compte = CompteBancaire("Alice", 100)
    compte.deposer(50)
"""

# ----- Style NumPy -----
"""
Opérations simples pour gérer des comptes bancaires.

Ce module comprend :
- Une classe pour représenter un compte bancaire.
- Des fonctions utilitaires pour les intérêts et la conversion de devises.

Classes
-------
CompteBancaire
    Représente un compte bancaire.

Fonctions
---------
calcul_interet(solde, taux_annuel)
    Calcule l’intérêt annuel.

convertir_euros_dollars(montant_eur, taux_conversion)
    Convertit un montant en dollars.
"""

# ============================================
# CLASSE (Style Google)
# ============================================

class CompteBancaire:
    """
    Représente un compte bancaire simple.

    Attributes:
        titulaire (str): Nom du titulaire du compte.
        solde (float): Solde actuel du compte.
    """

    def __init__(self, titulaire, solde=0.0):
        """
        Initialise un nouveau compte bancaire.

        Args:
            titulaire (str): Le nom du titulaire du compte.
            solde (float, optional): Le solde initial. Défaut = 0.0.
        """
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        """
        Dépose de l'argent sur le compte.

        Args:
            montant (float): Le montant à déposer.

        Returns:
            float: Le nouveau solde.
        """
        self.solde += montant
        return self.solde


# ============================================
# FONCTION (Style NumPy)
# ============================================

def calcul_interet(solde, taux_annuel):
    """
    Calcule l'intérêt annuel basé sur un taux.

    Parameters
    ----------
    solde : float
        Le solde du compte.
    taux_annuel : float
        Le taux d’intérêt annuel (ex. 0.05 pour 5%).

    Returns
    -------
    float
        L’intérêt annuel généré.
    """
    return solde * taux_annuel


# ============================================
# FONCTION (Style PEP 257)
# ============================================

def convertir_euros_dollars(montant_eur, taux_conversion):
    """Convertit un montant en euros vers dollars.

    Paramètres :
    montant_eur -- montant en euros à convertir
    taux_conversion -- taux de conversion euro -> dollar

    Retourne :
    Le montant équivalent en dollars.
    """
    return montant_eur * taux_conversion
