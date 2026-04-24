# Fichier d'exemples avec le module pathlib

# Import
import subprocess

def main():
    print("Resume des principales fonctionnalites du module subprocess :")
    
    # Executer une commande simple avec call (ex: 'echo Hello World')
    print("\nExecution d'une commande simple avec call :")
    result = subprocess.call(["cmd", "/c", "echo Hello, World!"])
    print("Sortie call :", result)

    # Executer une commande simple avec getstatusoutput (ex: 'echo Hello World')
    print("\nExecution d'une commande simple avec getstatustoutput :")
    status, result = subprocess.getstatusoutput(["cmd", "/c", "echo Hello, World!"])
    print("code de retour getstatusoutput :", status)
    print("Sortie getstatusoutput :", result)

    # Executer une commande simple avec run (ex: 'echo Hello World')
    print("\nExecution d'une commande simple :")
    result = subprocess.run(["cmd", "/c", "echo Hello, World!"], capture_output=True, text=True)
    print("code de retour run :", result.returncode)
    print("Sortie run :", result.stdout.strip())

    # Executer une commande et recuperer la sortie
    print("\nListe des fichiers du repertoire courant :")
    result = subprocess.run(["dir"], capture_output=True, text=True, shell=True)
    print("Sortie run :", result.stdout.strip())
    
    # Executer une commande avec gestion des erreurs
    print("\nExecution d'une commande invalide :")
    result = subprocess.run(["command_invalide"], capture_output=True, text=True, shell=True)
    print("Code de retour :", result.returncode)
    print("Erreur :", result.stderr.strip())
    
    # Utilisation de Popen pour executer une commande en arriere-plan
    print("\nExecution en arriere-plan avec Popen :")
    process = subprocess.Popen(["cmd", "/c", "timeout 5"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    print("Processus lance avec PID :", process.pid)
    process.wait()
    print("Processus termine.")

if __name__ == "__main__":
    main()
