from genEmptyGrid import generateEmptyGrid
from Ruleset import *
import random
import copy
import math

def fillGrid(grid, possPool):
    for i in range(len(grid)*len(grid)):
        line = i//len(grid)
        column = i%len(grid)
        if grid[line][column]=='.':
            copyPool = copy.deepcopy(possPool)
            random.shuffle(copyPool)
            for num in copyPool:
                if valid(grid, line, column, num):
                    grid[line][column]=num
                    if not emptyNum(grid):
                        return True
                    else:
                        if fillGrid(grid, possPool):
                            return True
            break
    grid[line][column]='.'
    return False

def generateGrid(size):
    grid=generateEmptyGrid(size)
    possPool = limitPool(grid)
    fillGrid(grid, possPool)
    return grid

if __name__ == "__main__":
    grid = generateGrid()
    for line in grid:
        print(line)

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