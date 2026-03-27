# Remarque le nom des fichiers doivent être differents des noms des dossiers.
# Fichiers dans le même dossier (package)
import conditions_boucles
conditions_boucles.main()

# avec un alias
import conditions_boucles as cb
cb.main()

# Importation d'une fonction du module conditions_boucles
from conditions_boucles import main
main()

# Importation d'une fonction du module conditions_boucles avec alias
from conditions_boucles import main as m
m()

# Fichiers dans d'autres dossiers (packages) avec le nom du dossier parent
import Cours.Importations.testImports
Cours.Importations.testImports.fctTest()

# Fichiers dans d'autres dossiers (packages) sans le nom du dossier parent
import Importations.testImports
Importations.testImports.fctTest()

# Fichiers dans d'autres dossiers (packages) avec le nom du dossier parent avec alias
import Cours.Importations.testImports as ti
ti.fctTest()

# Import d'une fonction du module testImports
from Cours.Importations.testImports import fctTest
fctTest()

# Import d'une fonction du module testImports avec un alias
from Cours.Importations.testImports import fctTest as ft
ft()
