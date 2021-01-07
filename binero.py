#Fonction pour transposer un tableau
def transpose(g):
    resultat = [[""] * len(i) for i in g] #Va créer un tableau contenant le même nombre d'éléments que g mais vide
    for i in range(len(g[0])): #Va parcourir chacun des éléments de g
        for j in range(len(g)): #Va parcourir les tableaux de tableau de g (ses éléments)
            resultat[j][i] = g[i][j] #Va ensuite entrer les valeurs dans le tableau "resultat"
    return resultat

assert transpose([["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15","16"]]) == [['1', '5', '9', '13'], ['2', '6', '10', '14'], ['3', '7', '11', '15'], ['4', '8', '12', '16']]