def transpose(g):
    resultat = g
    
    colonne = []
    for i in range(len(g)):
        for j in range(len(g[i])):
            colonne.append(g[j][i])
            print(i, j)
            
    print(colonne)
        
transpose([["1","0","1","0"],["1","0","1","0"],["0","1","1","0"],["1","1","0","0"]])