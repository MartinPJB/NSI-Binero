def transpose(g):
    """Fonction qui, à l'aide d'une grille sous forme de liste contenant des listes, retourne une nouvelle grille
    pour laquelle on a inversé les colonnes et les lignes de la grille d'origine.

    Paramètre(s):
        - g list: Grille à transposer sous la forme de liste de liste. La liste parente peut être composé d'un nombre de
            listes indéfinie mais doit être identique au nombre d'éléments des listes enfants. Les éléments de la liste
            enfant peuvent être de tout type et différents les uns des autres.

    Retourne:
        - list: Résultat de la fonction pour lequel on a inversé les colonnes et les lignes du paramètre g.

    Exemples:
        >>> transpose([["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15","16"]])
        [['1', '5', '9', '13'], ['2', '6', '10', '14'], ['3', '7', '11', '15'], ['4', '8', '12', '16']

        >>> transpose([[34, True], [[False, "25"], 0]])
        [[34, [False, '25']], [True, 0]]
    """
    resultat = [[""] * len(i) for i in g]   # Création un tableau vide contenant le même nombre d'éléments que g

    for i in range(len(g)):                 # Parcours des listes parentes de g
        for j in range(len(g)):             # Parcours des éléments de la liste g[i] (rappel: ici, len(g) == len(g[i]))
            resultat[j][i] = g[i][j]        # Remplace les valeurs vides du tableau de resultat en inversant les
                                            # positions afin d'inverser les colonnes et les lignes de la grille
    return resultat

assert transpose([["1", "2", "3", "4"], ["5", "6", "7", "8"], ["9", "10", "11", "12"], ["13", "14", "15", "16"]]) == \
                 [["1", "5", "9", "13"], ["2", "6", "10", "14"], ["3", "7", "11", "15"], ["4", "8", "12", "16"]]
assert transpose([[34, True], [[False, "25"], 0]]) == [[34, [False, '25']], [True, 0]]

def verifie_parite(liste):
    """Fonction qui, à l'aide d'une grille sous forme de liste, retourne True si celle-ci contient autant de 0 que de 1,
    Sinon retourne False.

    Paramètre(s):
        - liste list: Grille à vérifier

    Retourne:
        - boolean: Résultat de la vérification de parité.

    Exemples:
        >>> verifie_parite(["1","0","1","0"])
        True

        >>> verifie_parite(["1","1","1","0"])
        False
    """
    zero, un = 0, 0   #Variables qui nous permettrons de compter le nombre de 0 et de 1
    for i in liste:
        if i == "1":
            un += 1   #Ajoute 1 à la variable "un" à la rencontre d'un "1"
        else:
            zero += 1 #Ajoute 0 si i n'est pas égal à "1"
    if zero == un:
        return True   #Retourne True si le nombre de 0 et de 1 est égal
    return False

print(verifie_parite(["1","1","1","0"]))