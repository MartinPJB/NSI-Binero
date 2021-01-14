# Appel des dépendances
from tkinter import *       # Import de tkinter qui nous permettra de créer notre fenêtre
from tkinter import font    # Import de "font" (provenant de tkinter) qui nous permettra de créer nos polices 
from binero import *        # Import de binero qui nous permettra de valider la grille du joueur

# Création de la fenêtre tkinter
fenetre = Tk()
fenetre.geometry("200x300")     # Change la taille de la fenêtre.
fenetre.title("Jeu du binéro")  # Change le titre de la fenêtre.
fenetre.resizable(False, False) # Empêche l'utilisateur de changer la taille de la fenêtre.

# Création d'un canvas pour placer tout au centre
can = Canvas(fenetre, height = 100, width = 100)
can.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# Définition de la police d'écriture dans cette fenêtre
policeTitre = font.Font(family = "Arial", size = 80)
police = font.Font(family = "Arial", size = 10)


# Définition des grilles de binéro (classées par difficulté)
class difficulteeGrilles:
    facile = [["","","",""], ["1","","1",""], ["","0","",""], ["","","0","0"]] #4x4
    moyen = [["","0","","","1",""], ["","","0","","","1"], ["0","","","","0",""], ["","0","","","",""], ["1","","1","","","1"], ["0","","","","1",""]] #6x6
    difficile = [["1","","1","","","","","0"], ["","","","","","","",""], ["","0","","","","","0","0"], ["","","1","","1","","",""], ["","","","","1","","","0"], ["","0","","","","","",""], ["","","1","","0","","",""], ["","0","","","","","1",""]] #8x8


# Définition de la variable "reponse"
reponse = StringVar()
reponse.set("")


# Classe de jeu
class jeu:   
    def __init__(self):
        self.grille = None # Grille de jeu | Sera modifié dans le choix de la difficulté


    def change_texte(self, btn, ligne, col):
        if btn["text"] == "":       # Si rien n'est défini dans le bouton
            btn.config(text = "0")  # changement du texte en "0".
        elif btn["text"] == "0":    # Si le texte du bouton est "0"
            btn.config(text = "1")  # changement du texte en "1".
        else:                       # Sinon, changement du texte en
            btn.config(text = "")   # "".
        self.grille[ligne][col] = btn["text"] # Changement du texte du bouton.

    
    def termine_le_jeu(self):
        self.grille = None
        reponse.set("")
        
        for element in can.grid_slaves():   # S'itère en fonction des éléments présents dans le canvas
            element.grid_forget()           # Supprime l'élément du canvas
            
        self.choix_difficulte()

    def verification(self):                # Cette fonction va vérifier si le joueur a bien fait sa grille de binéro
        if verifie_grille(self.grille):    # Si la grille du joueur est valide, il gagne la partie.
            reponse.set("Bravo!")
            self.termine_le_jeu()
        else:
            reponse.set("Réessaye")
            
    
    def choix_difficulte(self):
        titre = Label(can, font = police, text = "Choix de la difficulté")
        titre.grid(row = 0, column = 0, columnspan = 70)

        #Création des boutons
        boutonFacile = Button(can, text = "Facile", relief = GROOVE, width = 6, borderwidth = 2)
        boutonMoyen = Button(can, text = "Moyen", relief = GROOVE, width = 6, borderwidth = 2)
        boutonDifficile = Button(can, text = "Difficile", relief = GROOVE, width = 6, borderwidth = 2)

        #Placement des boutons
        boutonFacile.grid(row = 2, column = 0, columnspan = 70)
        boutonMoyen.grid(row = 4, column = 0, columnspan = 70)
        boutonDifficile.grid(row = 6, column = 0, columnspan = 70)

        #Configuration des boutons
        boutonFacile.configure(command = lambda : self.lance_le_jeu("facile"))
        boutonMoyen.configure(command = lambda : self.lance_le_jeu("moyen"))
        boutonDifficile.configure(command = lambda : self.lance_le_jeu("difficile"))
        
    
    def lance_le_jeu(self, difficulte):
        self.grille = getattr(difficulteeGrilles, difficulte)                   # Récupère la liste à partir de la difficulté (qui est donnée en string)
        nouvelleTaille = f"{len(self.grille) * 50}x{(len(self.grille) * 50) + 100}"       # Définit la nouvelle taille de la fenetre
        fenetre.geometry(nouvelleTaille)                                        # et l'applique.

        for element in can.grid_slaves():   # S'itère en fonction des éléments présents dans le canvas
            element.grid_forget()           # Supprime l'élément du canvas

        commentaire = Label(can, font = police, textvariable = reponse)     # Créer le label "commentaire" qui nous servira
        commentaire.grid(row = 14, column = 0, columnspan = 70)             # a transmettre des messages au joueur.
        self.creation_tableau()                                                  # Créer le tableau avec la grille



    def creation_tableau(self):
        tableauBouton = [[None] * len(self.grille)] * len(self.grille) # Initialisé avec None

        for i in range(len(self.grille)):
            for j in range(len(self.grille)):
                if self.grille[i][j] != "":
                    bouton = Button(can, text = self.grille[i][j], height = 2, width = 4, relief = GROOVE, borderwidth = 2, state = DISABLED)
                else:
                    bouton = Button(can, text = "", height = 2, width = 4, relief = GROOVE, borderwidth = 2)
                    bouton.configure(command = lambda b = bouton, x = i, y = j: self.change_texte(b, x, y))
                tableauBouton[i][j] = bouton
                tableauBouton[i][j].grid(row = i, column = j)

        validationSaisie = Button(can, text = "Vérifier mon résultat", font = police, relief = GROOVE, borderwidth = 2)
        validationSaisie.grid(row = 12, column = 0, columnspan = 25)
        validationSaisie.configure(command = lambda : self.verification())

jeuBinero = jeu() # Initialise la classe
jeuBinero.choix_difficulte() # Lance la fonction par défaut pour demander la difficulté avant de lancer le jeu
fenetre.mainloop()