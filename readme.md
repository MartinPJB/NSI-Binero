# NSI - Projet n°2 [Classe de première]
*Instructions de projet*

## Règles du Binero

Pour jouer au Binero, les règles du jeu sont simples : remplir une grille à l'aide des chiffres *0* ou *1*. 3 règles sont à respecter :

* Pas plus de deux *0* ou deux *1* consécutifs sur une ligne ou sur une colonne
* Chaque ligne et chaque colonne contiennent autant de *0* que de *1*
* Deux lignes ou deux colonnes ne peuvent être identiques

## Grille d'un jeu de Binero

Nous considérerons qu'une grille de jeu est une liste de listes, et que chaque ligne de la grille de jeu est une liste de "*0*" , "*1*" ou "" *(case vide)*.

![Grille de départ d'un jeu de Binero](https://user-images.githubusercontent.com/34278608/103937626-4f3f7580-5129-11eb-8c44-ca50b888c7a6.png)

La grille dans l'image ci-dessus peut se traduire par :

```python
grille = [["", "", "", ""], ["1", "", "1", ""], ["", "0", "", ""], ["", "", "0", "0"]]
```

Cette représentation est la représentation habituelle d'une grille de jeu en programmation. L'interface utilisateur peut ensuite être prise en charge de différentes façons. Nous utiliserons *Tkinter*. Le fchier `interfaceTk.py` est le début d'une interface graphique réalisée avec la librairie *Tkinter*.

## Projet

1. Créez un fichier `binero.py` dans lequel vous implémenterez les fonctions suivantes :

    * une fonction `transpose(g)` qui prend en paramètre une grille de jeu *g* et qui renvoie une nouvelle grille dans laquelle on a échangé les lignes et les colonnes de la grille d'origine.
    * une fonction `verifie_consecutif(liste)` qui prend en paramètre une liste et qui renvoie `True` s'il n'y a pas plus de deux *0* ou deux *1* consécutifs dans cette liste et `False` sinon.
    * une fonction `verifie_parite(liste)` qui prend en paramètre une liste et qui renvoie `True` si la liste contient autant de *0* que de *1* et `False` sinon.
    * une fonction `verifie_identique(liste)` qui prend en paramètre une liste et qui renvoie `False` si la liste contient au moins deux éléments identiques et `True` sinon.
    * une fonction `grille_complete(g)` qui prend en paramètre une grille de jeu *g* et qui renvoie `True` si la grille ne comporte que des *0* ou des *1* et `False` sinon.
    * une fonction `verifie_grille(g)` qui prend en paramètre une grille de jeu *g*. Cette fonction appelle les fonctions précédentes et renvoie `True` si la grille est gagnante (au vu des règles du jeu) et `False` sinon.

2. Votre fichier `binero.py` est une librairie. Enregistrez les fichiers `binero.py` et `interfaceTk.py` dans le même dossier.

    Au début du fichier `interfaceTk.py`, rajoutez la ligne "`from binero import *`" afin d'utiliser dans le fichier `interfaceTk.py` les fonctions définies dans la librairie `binero.py`.

3. Interface graphique : modifiez la commande du bouton "*vérifier*" afin de permettre à l'utilisateur de jouer les 3 grilles `grille_1`, `grille_2` et `grille_3` proposées dans le fichier `interfaceTk.py`.

4. **Bonus :** Améliorez l'interface graphique et les fonctionnalités du jeu : choix de la taille de la grille et du niveau (ce qui impliquera la saisie d'une bibliothèque de grilles), cases *figées* en couleur, compteur de temps.

Vous devrez également rédiger un rapport d'une page environ au format pdf expliquant votre démarche, les difficultés rencontrées et les réponses que vous y avez apportées.

## Critères

* Résultat final
* Implication en classe durant les séances de projet
* Respect des consignes
* Organisation et propreté du code informatique
* Présence de commentaires dans le code *(avec #)*
* Spécifications de fonctions (`""".....""""`)
* Sélection pertinente d'assertions pour contrôler les résultats obtenus pour chacune des fonctions
* Rapport clair avec un contenu significatif

## Remise du projet

Fichier zip contenant les programmes et le rapport **pour le 01/02/2021**.
