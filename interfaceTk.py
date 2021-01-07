from tkinter import*
from tkinter import font


# construction de la fenêtre: cette fenêtre contiendra juste un bouton jouer pour démarrer la partie.
fenetre= Tk()
fenetre.geometry("500x800")

# Définition de la police dans cette fenêtre
maPolice=font.Font(family='Arial', size=80, weight='bold')
maPolice1=font.Font(family='Arial', size=20, weight='bold')
# On part du tableau à deux dimensions représentant la grille 

grille_1= [["","","",""],["1","","1",""],["","0","",""],["","","0","0"]]
grille_2= [["","","","1"],["","","0",""],["","1","",""],["","1","1",""]]
grille_3= [["1","","1","","","","","0"],["","","","","","","",""],["","0","","","","","0","0"],["","","1","","1","","",""],["","","","","1","","","0"],["","0","","","","","",""],["","","1","","0","","",""],["","0","","","","","1",""]]

grille=grille_1

reponse=StringVar()  # La variable "reponse" contient le commentaire associé au mot proposé par le joueur. 
reponse.set('')

# On définit les labels qui apparaîtront dans la fenêtre :    
commentaire= Label(fenetre,font=maPolice1, textvariable=reponse) # label qui contient le commentaire Gagné ou Perdu
                                                                    
# Placement des labels sur la fenêtre
commentaire.grid(row=14,column=1,columnspan=70)

    
def change_texte(g,btn,ligne,col):
    if btn['text']=="":
        btn.config(text="0")
    elif btn['text']=="0":
        btn.config(text="1")
    else:
        btn.config(text="")
    g[ligne][col]=btn['text']
    

def verification(g):
    reponse.set('programme à compléter')
    
    
    
# Constuction du tableau de boutons
tableauBoutons=[[None] * len(grille)] * len(grille)    # on l'initialise avec None
# On le remplit avec les boutons
for i in range(len(grille)):
    for j in range(len(grille)):       
        if grille[i][j]!="":
            bouton = Button(fenetre, text= grille[i][j],height=2,width=4,relief='raised', borderwidth=5, state=DISABLED)
        else:
            bouton = Button(fenetre, text= "",height=2,width=4,relief='raised', borderwidth=5)
            bouton.configure(command= lambda b=bouton,x=i, y=j: change_texte(grille,b,x,y))
        tableauBoutons[i][j]=bouton
        # placement des boutons sur la fenêtre
        tableauBoutons[i][j].grid(row=i,column=j)

# Construction et placement du bouton "validationSaisie" 
validationSaisie = Button(fenetre, text ='Vérifier',font=maPolice1,relief='raised', borderwidth=5)
validationSaisie.grid(row=12,column=2,columnspan=25)
validationSaisie.configure(command=lambda :verification(grille))

fenetre.mainloop()


