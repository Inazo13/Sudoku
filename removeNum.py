from Ruleset import *
from solveGrid import *
import random
import copy

def removeNum(grid, diff=1, toLong=False):
    # copie de la grille original afin d'effectuer une comparaison
    originalGrid = copy.deepcopy(grid)
    # determination du nombre de cases à retirer dans notre grille
    if diff==1: squares=int(len(grid)**2//(10/4))
    elif diff==2: squares=int(len(grid)**2//(10/5))
    elif diff==3: squares=int(len(grid)**2//(10/6))
    elif diff==4: squares=int(len(grid)**2//(10/7))
    elif diff==5: squares=int(len(grid)**2//(4/3))
    #
    #définition de l'ordre dans lequel on va enlever les cases
    order = [i for i in range(len(grid)**2)]
    random.shuffle(order)
    #
    while squares>0 and order!=[]:
        square = order.pop(0) # on retire le 1er élément du tableau 
        line = square//len(grid)
        column = square%len(grid)
        #
        # on retire et on sauvegarde l'éléùent de la case
        removeSquare = grid[line][column]
        grid[line][column] = "."
        squares -= 1
        #
        # pour les petites grilles, vérification que la grille soit à solution unique
        if toLong==False:
            copyGrid = copy.deepcopy(grid)
            solveGrid(copyGrid)
            if copyGrid != originalGrid:
                squares += 1
                grid[line][column] = removeSquare

"""if __name__ == "__main__":

    grid = [['n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5'],
['l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8'],
['p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm'],
['a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6'],
['3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h'],
['k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l'],
['c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p'],
['i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a'],
['4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3'],
['2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n'],
['f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c'],
['1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i'],
['e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4'],
['9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2'],
['g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k'],
['o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1'],
['d', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e'],
['7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9'],
['j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g'],
['b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f'],
['5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd'],
['8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7'],
['m', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j'],
['6', 'a', 'i', '1', 'o', 'h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b'],
['h', '3', '4', 'e', 'd', '5', 'n', '2', '9', '7', '8', 'l', 'k', 'g', 'j', 'm', 'p', 'c', 'f', 'b', '6', 'a', 'i', '1', 'o']]

    removeNum(grid, 1, True)

    for line in grid:
        print(line)"""