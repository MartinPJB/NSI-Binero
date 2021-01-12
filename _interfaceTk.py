# Appel des dépendances
from tkinter import *       # Import de tkinter qui nous permettra de créer notre fenêtre
from tkinter import font    # Import de "font" (provenant de tkinter) qui nous permettra de créer nos polices 
from binero import *        # Import de binero qui nous permettra de valider la grille du joueur
import time                 # Import de time qui nous permettra de faire attendre le joueur 1 seconde à la fin de sa partie (si il gagne)

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
facile = [["","","",""], ["1","","1",""], ["","0","",""], ["","","0","0"]] #4x4
moyen = [["","0","","","1",""], ["","","0","","","1"], ["0","","","","0",""], ["","0","","","",""], ["1","","1","","","1"], ["0","","","","1",""]] #6x6
difficile = [["1","","1","","","","","0"], ["","","","","","","",""], ["","0","","","","","0","0"], ["","","1","","1","","",""], ["","","","","1","","","0"], ["","0","","","","","",""], ["","","1","","0","","",""], ["","0","","","","","1",""]] #8x8

grille = None #Sera modifié dans le choix de la difficulté


# Définition de la variable "reponse"
reponse = StringVar()
reponse.set("")


# Définition des fonctions
def change_texte(g, btn, ligne, col):
    if btn["text"] == "":       # Si rien n'est défini dans le bouton
        btn.config(text = "0")  # changement du texte en "0".
    elif btn["text"] == "0":    # Si le texte du bouton est "0"
        btn.config(text = "1")  # changement du texte en "1".
    else:                       # Sinon, changement du texte en
        btn.config(text = "")   # "".
    g[ligne][col] = btn["text"] # Changement du texte du bouton.


def verification(g):                # Cette fonction va vérifier si le joueur a bien fait sa grille de binéro
    if verifie_grille(g):           # Si la grille du joueur est valide, il gagne la partie.
        reponse.set("Bravo!")
    else:
        reponse.set("Réessaye.")


def choix_difficulte():        
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
    boutonFacile.configure(command = lambda : lance_le_jeu("facile"))
    boutonMoyen.configure(command = lambda : lance_le_jeu("moyen"))
    boutonDifficile.configure(command = lambda : lance_le_jeu("difficile"))


def lance_le_jeu(difficulte):
    grille = eval(difficulte)                                               # Récupère la liste à partir de la difficulté (qui est donnée en string)
    nouvelleTaille = f"{len(grille) * 50}x{(len(grille) * 50) + 100}"       # Définit la nouvelle taille de la fenetre
    fenetre.geometry(nouvelleTaille)                                        # et l'applique.

    for element in can.grid_slaves():   # S'itère en fonction des éléments présents dans le canvas
        element.grid_forget()           # Supprime l'élément du canvas

    commentaire = Label(can, font = police, textvariable = reponse)     # Créer le label "commentaire" qui nous servira
    commentaire.grid(row = 14, column = 0, columnspan = 70)             # a transmettre des messages au joueur.
    creation_tableau(grille)                                            # Créer le tableau avec la grille 


def creation_tableau(g):
    tableauBouton = [[None] * len(g)] * len(g) # Initialisé avec None

    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] != "":
                bouton = Button(can, text = g[i][j], height = 2, width = 4, relief = GROOVE, borderwidth = 2, state = DISABLED)
            else:
                bouton = Button(can, text = "", height = 2, width = 4, relief = GROOVE, borderwidth = 2)
                bouton.configure(command = lambda b = bouton, x = i, y = j: change_texte(g, b, x, y))
            tableauBouton[i][j] = bouton
            tableauBouton[i][j].grid(row = i, column = j)

    validationSaisie = Button(can, text = "Vérifier mon résultat", font = police, relief = GROOVE, borderwidth = 2)
    validationSaisie.grid(row = 12, column = 0, columnspan = 25)
    validationSaisie.configure(command = lambda : verification(g))

choix_difficulte() # Lance la fonction par défaut pour demander la difficulté avant de lancer le jeu
fenetre.mainloop()