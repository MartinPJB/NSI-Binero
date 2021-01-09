def transpose(g):
    """Fonction qui, à l'aide d'une grille sous forme de liste contenant des listes, retourne une nouvelle grille
    pour laquelle on a inversé les colonnes et les lignes de la grille d'origine.

    Paramètre(s):
        - g list: Grille à transposer sous la forme de liste de liste. La liste parente peut être composée d'un nombre
            de listes indéfinie mais doit être identique au nombre d'éléments des listes enfants. Les éléments de la
            liste enfant peuvent être de tout type et différents les uns des autres.

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
    """Fonction qui, à l'aide d'une liste, retourne un booléen variant selon si trois éléments consécutifs se situe
    dans cette liste.

    Paramètre(s):
        - liste list: Liste à vérifier, peut comprendre un nombre indéfini d'élément de tout type (sauf None) pouvant
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


assert not verifie_consecutif([6, 2, 1, 1, 1, 2])
assert verifie_consecutif([[12, 12, 12], [14, 14, 14], False])


def verifie_parite(liste):
    """Fonction qui, à l'aide d'une liste, retourne un booléen variant selon si autant de "0" et de "1" se situent dans
    cette liste.

    Paramètre(s):
        - liste list: Liste à vérifier, peut posséder un nombre d'élément indéfini mais doit être pair (sinon le
        résultat sera forcément False) sachant que ceux-ci doivent être les chaînes de caractères "0" ou "1".

    Retourne:
        - boolean: True si la liste contient autant de "0" que de "1", sinon False.

    Exemples:
        >>> verifie_parite(["1", "0", "1", "0"])
        True

        >>> verifie_parite(["0", "1", "1", "0", "1"])
        False
    """
    zeros = 0  # Variable nous permettant de compter le nombre de "0"

    for element in liste:           # Itération de chacun des éléments de la liste où l'on compte le nombre de "0"
        if element == "0":          # (chaîne de caractère), si celui-ci correspond à la moitié du nombre d'élément de
            zeros += 1              # la liste (puisque nous savons que ses éléments sont soit "0" ou "1" et que leur
                                    # nombre est pair), retourne True, sinon False.
    if zeros == len(liste) // 2:
        return True

    return False


assert not verifie_parite(["1", "1", "1", "0"])
assert verifie_parite(["0", "1", "1", "0", "1"])


def verifie_identique(liste):
    """Fonction qui, à l'aide d'une liste, retourne un booléen variant selon si la liste contient au moins deux éléments
    identiques.

    Paramètre(s):
        - liste list: Liste à vérifier, peut posséder un nombre d'élément indéfini sachant que ceux-ci doivent être les
        chaînes de caractères "0" ou "1".

    Retourne:
        - boolean: False si la liste contient au moins deux éléments identiques, sinon True.

    Exemples:
        >>> verifie_identique(["1", "0"])
        True

        >>> verifie_identique(["1", "1", "0"])
        False
    """
    valeurs = []  # Variable nous permettant de stocker les valeurs de la liste "liste"

    for element in liste:          # Itération de chacun des éléments de la liste et vérification de la
        if element in valeurs:     # présence de l'élément dans la liste "valeurs". Si celle-ci y est
            return False           # présente, la fonction retournera False, sinon il l'ajoutera dans
        valeurs.append(element)    # celle-ci. Si aucune valeur n'est identique, la fonction retournera True.

    return True


assert not verifie_identique(["1", "1", "0"])
assert verifie_identique(["1", "0"])
