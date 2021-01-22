from tkinter import *
from tkinter import font
from tkinter import messagebox
from binero import verifie_grille

# Création de la fenêtre racine tkinter à taille fixe
racine = Tk()
racine.title("Binero")
racine.resizable(False, False)

# Définition des polices d'écriture utilisées
polices = {
    "h1": font.Font(family="Arial", size=18, weight="bold"),
    "h2": font.Font(family="Arial", size=14, weight="bold"),
    "default": font.Font(family="Arial", size=10)
}

# Définition des grilles de départ pour le jeu de binero (classées par difficulté)
grilles = [
    [["", "", "", ""], ["1", "", "1", ""], ["", "0", "", ""], ["", "", "0", "0"]],  # Grille facile (4x4)
    [["", "0", "", "", "1", ""], ["", "", "0", "", "", "1"], ["0", "", "", "", "0", ""],  # Grille moyenne (6x6)
     ["", "0", "", "", "", ""], ["1", "", "1", "", "", "1"], ["0", "", "", "", "1", ""]],
    [["1", "", "1", "", "", "", "", "0"], ["", "", "", "", "", "", "", ""],  # Grille difficile (8x8)
     ["", "0", "", "", "", "", "0", "0"], ["", "", "1", "", "1", "", "", ""],
     ["", "", "", "", "1", "", "", "0"], ["", "0", "", "", "", "", "", ""],
     ["", "", "1", "", "0", "", "", ""], ["", "0", "", "", "", "", "1", ""]]
]


class ChoixDifficulte:
    """Classe d'interface Tkinter permettant à l'utilisateur de sélectionner une difficulté."""

    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.frame_principale = Frame(self.parent)
        self.frame_principale.grid(column=1, row=1, sticky="nsew", padx=25, pady=(4, 8))

        Label(self.frame_principale, font=polices["h1"], text="Jeu du Binero", anchor="center") \
            .grid(column=1, row=1, pady=(0, 4))
        Label(self.frame_principale, font=polices["default"], text="Veuillez choisir une difficulté :",
              anchor="center").grid(column=1, row=2)

        # Groupement des boutons de difficulté (utilisation du lambda pour faire passer des arguments dans la fonction)
        self.frame_boutons = Frame(self.frame_principale)
        self.frame_boutons.grid(column=1, row=3, sticky="s")

        Button(self.frame_boutons, text="Facile", font=polices["default"], relief=GROOVE,
               command=lambda: self.commande_boutons(0)).grid(column=1, row=1, sticky="ew")
        Button(self.frame_boutons, text="Moyen", font=polices["default"], relief=GROOVE,
               command=lambda: self.commande_boutons(1)).grid(column=1, row=2, sticky="ew")
        Button(self.frame_boutons, text="Difficile", font=polices["default"], relief=GROOVE,
               command=lambda: self.commande_boutons(2)).grid(column=1, row=3, sticky="ew")

    def commande_boutons(self, difficulte):
        """Méthode qui permet d'appeler le callback avec la grille correspondant à la difficulté donné par l'utilisateur
        après avoir détruit frame_principale et ses éléments. Supprime également l'objet associé à la classe.

        Paramètres:
            - difficulte int: Difficulté demandé pour la partie à venir (0 vaut facile, 1 vaut moyen, 2
        vaut difficile)
        """
        self.frame_principale.destroy()

        self.callback(grilles[difficulte])


class GrilleJeu:
    def __init__(self, parent, grille, callback):
        self.parent = parent
        # Création de self.grille par compréhension afin d'éviter que la valeur ne soit assignée par référence
        self.grille = [[grille[x][y] for y in range(len(grille[x]))] for x in range(len(grille))]
        self.callback = callback

        self.frame_principale = Frame(self.parent)
        self.frame_principale.grid(column=1, row=1, sticky="nsew", padx=25, pady=(4, 8))

        Label(self.frame_principale, font=polices["h2"], text="À vous de jouer !", anchor="center") \
            .grid(column=1, row=1, pady=(0, 4))

        self.frame_boutons = Frame(self.frame_principale)
        self.frame_boutons.grid(column=1, row=3)

        # Création de la grille de jeu
        self.grille_boutons = []

        for i in range(len(self.grille)):
            self.grille_boutons.append([])

            for j in range(len(self.grille[i])):
                if self.grille[i][j] == "":
                    bouton = Button(self.frame_boutons, text="", height=2, width=4, relief=GROOVE, borderwidth=2)
                    bouton["command"] = lambda bouton=bouton, j=j, i=i: self.modification_bouton(bouton, j, i)
                    # Notation bouton=bouton, j=j, i=i dans la fonction anonyme afin de mettre à jour ses paramètres à
                    # chaque fois
                else:
                    bouton = Button(self.frame_boutons, text=self.grille[i][j], height=2, width=4, relief=GROOVE,
                                    borderwidth=2, bg="gray85", state=DISABLED)

                bouton.grid(row=i, column=j)
                self.grille_boutons[i].append(bouton)

        # Groupe de boutons de "contrôle" permettant à l'utilisateur de valider ou réinitialiser la partie
        self.groupe_controles = Frame(self.frame_principale)
        self.groupe_controles.grid(column=1, row=4, pady=(4, 0))

        Button(self.groupe_controles, text="Valider", font=polices["default"], relief=GROOVE, borderwidth=2,
               command=self.verification).grid(column=1, row=1)

        Button(self.groupe_controles, text="Réinitialiser", font=polices["default"], relief=GROOVE, borderwidth=2,
               command=self.reinitialisation).grid(column=2, row=1)

    def modification_bouton(self, bouton, x, y):
        """Méthode qui met à jour les différents éléments de l'interface lorsque l'utilisateur interagit avec
        l'interface.

        Paramètres:
            - bouton tkinter.Button: Bouton à modifier.
            - x int: Position d'abscisse du bouton par rapport à la grille.
            - y int: Position d'ordonnée du bouton par rapport à la grille.
        """
        if bouton["text"] == "":
            bouton["text"] = "0"
        elif bouton["text"] == "0":
            bouton["text"] = "1"
        else:
            bouton["text"] = ""
        self.grille[y][x] = bouton["text"]  # Répond à la nécessité de mettre à jour la grille de base

    def verification(self):
        if verifie_grille(self.grille):
            messagebox.showinfo(title="Vous avez gagné",
                                message="Félicitations ! Votre grille est valide et vous avez gagné.")
            self.frame_principale.destroy()

            self.callback(self.parent)
        else:
            messagebox.showerror(title="Erreur dans la grille",
                                 message="Oh non ! Une erreur est invalide, veuillez réessayer.")

    def reinitialisation(self):
        """Méthode qui permet de réinitialiser la grille visuelle à ses valeurs prédéfinies."""
        for i in range(len(self.grille_boutons)):
            for j in range(len(self.grille_boutons[i])):
                if self.grille_boutons[i][j]["state"] != DISABLED:
                    self.grille_boutons[i][j]["text"] = ""
                    self.grille[i][j] = ""


def debut_interface(parent):
    """Fonction qui démarre l'interface par le choix de difficulté avec pour callback, la grille de jeu. Cette fonction
    est récursive s'arrêtant lorsque l'utilisateur ferme le programme et **dois** donc **absolument** être exécuté en
    fin de programme."""
    ChoixDifficulte(parent, lambda grille: GrilleJeu(racine, grille, debut_interface))


debut_interface(racine)
racine.mainloop()
