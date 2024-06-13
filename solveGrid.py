from genEmptyGrid import generateEmptyGrid
from Ruleset import *
import random
import copy

def solve(grid, possPool):
    """Rempli la grille de Sudoku de manière récursive en regardant les valeurs 1 à 1
    Renvoie des booléens afin de sortir de la récursivité
    """
    for i in range(len(grid)*len(grid)):
        line = i//len(grid) #Determine la ligne en fonction du numéro de la case
        column = i%len(grid) #Determine la colonne en fonction du numéro de la case
        if grid[line][column]=='.':
            for num in possPool:
                if valid(grid, line, column, num): #vérifie la validité de la valeur num
                    grid[line][column]=num
                    if not emptyNum(grid): #vérifie si la grille est pleine
                        return True
                    else:
                        if solve(grid, possPool):
                            return True
            break
    grid[line][column]='.'
    return False

def solveGrid(grid):
    """Fonction qui appelle la fonction principale mais en créant elle même
    le tableau possPool, tableau des valeurs possibles de la grille"""
    possPool = limitPool(grid)
    solve(grid, possPool)
    

"""
if __name__ == "__main__":
    grid = [['.', 'b', '.', '6', 'd', 'c', '.', '.', '4', '.', '9', '.', 'f', '.', '.', '.'],
['a', '.', '3', '.', '.', 'b', '.', '.', 'd', '8', '2', 'c', '1', '9', '4', '.'],
['.', '.', '4', '8', '.', '.', '3', '.', '.', '6', '.', '.', '.', 'd', '.', '.'],
['.', '2', 'd', '1', '.', '.', '.', '9', '.', '.', '.', 'b', 'g', '3', '.', '.'],
['8', '5', '.', 'd', '.', '7', 'e', '.', 'g', '.', '3', '6', '4', '.', 'c', 'f'],
['.', '1', 'f', '3', '5', '.', 'a', '.', '.', '.', '.', '.', '.', '.', 'g', '.'],
['2', '.', 'c', '.', '9', '.', '1', 'g', '5', 'f', 'b', 'd', '.', 'a', '.', 'e'],
['.', 'a', '7', '.', '.', '.', '.', '.', '2', '.', '1', '8', '.', '5', '.', '9'],
['.', 'g', '.', '.', '.', '9', '.', '5', '.', '.', '4', 'a', '.', '2', '7', 'b'],
['9', '.', '5', '.', '.', '.', '6', 'b', '3', '2', 'e', '.', '.', 'g', '1', 'd'],
['d', '.', '.', '.', '.', '.', '4', '.', '8', 'b', 'g', '9', '.', 'c', '.', '3'],
['.', '.', '1', 'b', '2', '.', '.', '3', '6', 'd', 'c', '5', '9', '.', '.', '.'],
['1', 'c', '.', '9', 'f', '.', '.', 'a', '.', '.', '.', '.', '5', '.', '2', '.'],
['4', '7', 'a', 'f', '.', '.', 'c', 'd', '.', '.', '.', '.', '.', 'b', '.', 'g'],
['6', '.', '.', '.', '1', '.', '.', '7', 'b', '5', '.', '4', 'd', '.', '.', '.'],
['e', 'd', '.', '.', '.', '.', '.', '4', '.', '.', '6', 'f', '.', '8', '9', '.']]

    for line in grid:
        print(line)
"""