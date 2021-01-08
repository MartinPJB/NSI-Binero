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
    resultat = [[None] * len(i) for i in g]  # Création un tableau vide contenant le même nombre d'éléments que g

    for i in range(len(g)):             # Parcours des listes parentes de g
        for j in range(len(g)):         # Parcours des éléments de la liste g[i] (rappel: ici, len(g) == len(g[i]))
            resultat[j][i] = g[i][j]    # Remplace les valeurs vides du tableau de resultat en inversant les
                                        # positions afin d'inverser les colonnes et les lignes de la grille

    return resultat


assert transpose([["1", "2", "3", "4"], ["5", "6", "7", "8"], ["9", "10", "11", "12"], ["13", "14", "15", "16"]]) == \
                 [["1", "5", "9", "13"], ["2", "6", "10", "14"], ["3", "7", "11", "15"], ["4", "8", "12", "16"]]
assert transpose([[34, True], [[False, "25"], 0]]) == [[34, [False, '25']], [True, 0]]


def verifie_consecutif(liste):
    """Fonction qui, à l'aide d'une liste, retourne un boolean variant selon si trois éléments consécutifs se situe
    dans cette liste.

    Paramètre(s):
        - liste list: Liste à vérifier, peut comprendre un nombre indéfini d'élément de tout types (sauf None) pouvant
            différer les uns des autres.

    Retourne:
        - bool: False si trois caractères identiques se suivent, sinon True.

    Exemples:
        >>> verifie_consecutif([6, 2, 1, 1, 1, 2])
        False

        >>> verifie_consecutif([[12, 12, 12], [14, 14, 14], False])
        True
    """
    precedents = [None] * 2  # Création d'un tableau vide stockant les valeurs à vérifier

    # Itération de chacun des éléments de la liste, si l'un d'eux est identique avec les deux éléments précédents,
    # retourne False, sinon, on continue en assignant le premier élément de precedents à son second indice et l'élément
    # itéré au premier indice de precedents

    for element in liste:
        if element == precedents[0] and element == precedents[1]:
            return False
        else:
            precedents[1] = precedents[0]
            precedents[0] = element

    return True
