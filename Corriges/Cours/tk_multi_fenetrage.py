# Se connecter avec un mot de passe puis ouvrir des fenêtres
"""Module d'exemple de multi fenêtrage"""

from tkinter import Event, Widget, Tk, Button, Label, Widget, messagebox, Entry, Toplevel

fen1 :Toplevel = None
fen2 :Toplevel = None
btn_fen1 :Button = None
btn_fen2 :Button = None


# Fonction qui sera appeler pour la fermeture de la fenetre 1 ou 2
def on_close(fenetre :Toplevel, bouton :Button):
    """Fonction générique de fermeture de fenêtre et reactiver le bouton correspondant."""
    global fen1, fen2
    fenetre.destroy()
    
    # Remet à None la bonne variable globale selon la fenêtre
    if fenetre == fen1:
        fen1 = None
    elif fenetre == fen2:
        fen2 = None
    
    # Réactive le bouton correspondant
    if bouton:
        bouton.config(state="normal")


# Fermeture de la fenetre principale si les fenetre 1 et 2 sont fermer.
def gerer_echap_principal(event :Event) -> None:
    """
    Gère la touche Echap :
    - Ferme la fenêtre fille qui a le focus (fen1 ou fen2)
    - Sinon ferme la fenêtre principale (root2) quand il n'y a plus de fenetre fille ouverte.
    """
    global fen1, fen2
    # Passe par une variable widget pour que VSCode detecte les fonctions au lieu d'etre en blanc
    widget: Widget = event.widget
    
    # Fenetre qui a le focus
    focused: Toplevel = widget.winfo_toplevel()

    # Vérifie si la fenetre 1 existe et que la variable fen1 n'est pas None ainsi que le focus est sur fen1
    if fen1 is not None and fen1.winfo_exists() and (focused == fen1):
        on_close(fen1, btn_fen1)
        return
    
    # Vérifie si la fenetre 2 existe et que la variable fen2 n'est pas None ainsi que le focus est sur fen2
    if fen2 is not None and fen2.winfo_exists() and (focused == fen2):
        on_close(fen2, btn_fen2)
        return
    
    # Fermer la fenêtre principale (root2) si les autres fenetres sont fermees.
    if (fen1 is None or not fen1.winfo_exists()) and (fen2 is None or not fen2.winfo_exists()):
        focused.destroy()

def fenetre1() -> None:
    """Création de la fenêtre de test 1"""
    global fen1

    if fen1 is None or not fen1.winfo_exists():
        fen1 = Toplevel()
        fen1.transient(fen1.master)
        fen1.geometry("300x300+200+200")
        Label(fen1, text="Fenetre 1").pack()
        # command passe par une lambda car on a des parametre obligatoire dans la finction on_close
        # si la fonction n'avait pas de parametre command=on_close aurais suffit
        # en fait, lambda cree uner fonction anonyme sans parametre et donc on_close(...) sera executer seulement au moment du clique
        Button(fen1, text="Quitter", command=lambda: on_close(fen1, btn_fen1)).pack()
        fen1.bind("<Escape>", lambda e: on_close(fen1, btn_fen1))

        # Gere la fermeture de la fenetre via la croix
        fen1.protocol("WM_DELETE_WINDOW", lambda: on_close(fen1, btn_fen1))

        # Si le bouton existe, on le grise
        if btn_fen1:
            btn_fen1.config(state="disabled")
    else:
        fen1.lift() # remet la fenetre 1 au premier plan.


def fenetre2() -> None:
    """Création de la fenêtre de test 2"""
    global fen2

    # Si la variable gloable est à None ou si la fenetre2 n'existe pas
    if fen2 is None or not fen2.winfo_exists():
        fen2 = Toplevel()
        fen2.transient(fen2.master)
        fen2.geometry("200x200+800+500")
        fen2.title("Fenetre 2")
        Label(fen2, text="Fenetre 2").pack()
        Button(fen2, text="Quitter", command=lambda: on_close(fen2, btn_fen2)).pack()
        fen2.bind("<Escape>", lambda e: on_close(fen2, btn_fen2))

        # gere la fermeture de la fenetre via la croix
        fen2.protocol("WM_DELETE_WINDOW", lambda: on_close(fen2, btn_fen2))

        # Si le bouton existe, on le grise
        if btn_fen2:
            btn_fen2.config(state="disabled")
    else:
        fen2.lift()


# Fenêtre principale.
def fenetre_principale() -> None:
    """Création de la fenêtre principale"""
    global btn_fen1, btn_fen2
    root2 = Tk()
    root2.title('Fenêtre principale')
    root2.geometry('800x600+500+300')

    Label(root2, text='Le mot de passe est correct, \
Bienvenue à la fenêtre principale.', wraplength=250).pack(padx=10)
    
    btn_fen1 = Button(root2, text="Fenetre 1", command=fenetre1)
    btn_fen1.pack(pady=5)

    btn_fen2 = Button(root2, text="Fenetre 2", command=fenetre2)
    btn_fen2.pack(pady=5)

    root2.bind("<Escape>", gerer_echap_principal)
    root2.mainloop()

# Fenêtre de connexion
# evenement permet de binder la fonction à un widget (demande un paramètre)
def test_ok(evenement) -> None:
    """Test du mot de passe"""
    if entry.get() == 'abc123':
        # Ferme la fenêtre de connexion.
        quitter_fen_mdp(evenement)
        # Création de la fenêtre principale.
        fenetre_principale()
    else:
        messagebox.showwarning("Attention", "Mauvais mot de passe !")

# la fonction destroy() demande un evenement (event)
# meme si c'est invisible
def quitter_fen_mdp(event):
    root1.destroy()

# Programme principal
root1 = Tk()
root1.title('Fenêtre de connexion')
root1.geometry('300x150+600+200')
Label(root1, text='Veuillez saisir le mot de passe : abc123').pack()
entry = Entry(root1)
entry.bind("<Return>", test_ok)
root1.bind("<Escape>", quitter_fen_mdp)
entry.pack()
entry.focus_set()
# Déterminer si le mot de passe est correct.
Button(root1, text="Ok", command=lambda: test_ok(None), width=15).pack(pady=5)
# Ferme la fenêtre de connexion.
Button(root1, text="Quitter", command=root1.destroy, width=15).pack(pady=5)
# Attend d'accepter la fenetre de connexion
# avant d'ouvrir la fenêtre principale.
root1.mainloop()
