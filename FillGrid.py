from genEmptyGrid import generateEmptyGrid
from Ruleset import *
import random
import copy
import math

def fillGrid(grid, possPool):
    """Rempli la grille de Sudoku de manière récursive à l'aide d'un tableau
    des valeurs possibles mélangés aléatoirement.
    Renvoie des booléens afin de sortir de la récursivité.
    """
    for i in range(len(grid)*len(grid)):
        line = i//len(grid)
        column = i%len(grid)
        if grid[line][column]=='.':
            #création d'une copie du tab des valeurs possibles
            copyPool = copy.deepcopy(possPool)
            #mélange du tableau
            random.shuffle(copyPool)
            for num in copyPool:
                if valid(grid, line, column, num): #vérifie la validité de la valeur num
                    grid[line][column]=num
                    if not emptyNum(grid): #vérifie si la grille est pleine
                        return True
                    else:
                        if fillGrid(grid, possPool):
                            return True
            break
    grid[line][column]='.'
    return False

def generateGrid(size):
    """Fonction qui va générer une grille vide puis qui va la remplir"""
    grid=generateEmptyGrid(size)
    possPool = limitPool(grid)
    fillGrid(grid, possPool)
    return grid

def fillCell(grid, pool, cell, size):
    """Fonction qui va remplir une cellule à l'aide d'un tableau de caractères aléatoires"""
    for line in range((cell//size)*size, ((cell//size)+1)*size):
        for column in range((cell%size)*size, ((cell%size)+1)*size):
            grid[line][column]=pool.pop(0)

def generateGrid2(size):
    """Fonction qui génère une grille vide puis la remplie à l'aide d'un tableau
    de caractères aléatoires qui sera arangé pour que la grille soit valide"""
    grid=generateEmptyGrid(size)
    pool = limitPool(grid)
    random.shuffle(pool)
    for cell in range(size*size):
        fillCell(grid, copy.deepcopy(pool), cell, size)
        #On décale les valeurs d'une ligne sur la cellule
        pool = pool[size:]+pool[:size] 
        if (cell+1)%5==0:
            # On décale les valeurs d'une ligne + 1 quand on commence une nouvelle ligne de celulles 
            pool = pool[size+1:]+pool[:size+1]
    return grid

"""if __name__ == "__main__":
    grid = generateGrid2(5)
    for line in grid:
        print(line)
"""


# Anciens codes

"""def findPossNum(possPool, grid, indCell, i):
    possNum = []
    for j in possPool:
        line = findLine(grid, indCell, i)
        column = findColumn(grid, indCell, i)
        hitLigne = searchLine(grid, line, j)
        hitColonne = searchColumn(grid, column, j)
        hitCell = searchCell(grid, indCell, j)
        if hitLigne==False and hitColonne==False and hitCell==False:
            possNum.append(j)
    return possNum"""

"""def fillCell(possPool, grid, indCell):
    tailleTab=int(math.sqrt(len(grid)))
    for i in range(len(grid[indCell])):
        possNum=findPossNum(possPool, grid, indCell, i)
        if possNum==[]:
            grid[indCell][i] = grid[indCell][i-tailleTab]
            grid[indCell][i-tailleTab] = '.'
            possNum=findPossNum(possPool, grid, indCell, i-tailleTab)
            grid[indCell][i-tailleTab] = possNum[0]
        else:
            grid[indCell][i] = random.choice(possNum)"""


"""def fillDiag(possPool, grid):
    tailleGrid = int(math.sqrt(len(grid)))
    x = 0 #indice des diagionales
    while x<len(grid):
        copyPool = copy.deepcopy(possPool)
        for i in range(len(grid)):
            num = random.choice(copyPool)
            grid[x][i] = num
            copyPool.remove(num)
        x += tailleGrid+1 """