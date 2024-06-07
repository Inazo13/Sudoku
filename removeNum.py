from Ruleset import *
from solveGrid import *
import random
import copy

def removeNum(grid, diff=1):
    originalGrid = copy.deepcopy(grid)
    if diff==1: squares=int(len(grid)**2//(10/4))
    elif diff==2: squares=int(len(grid)**2//(10/5))
    elif diff==3: squares=int(len(grid)**2//(10/6))
    elif diff==4: squares=int(len(grid)**2//(10/7))
    elif diff==5: squares=int(len(grid)**2//(4/3))
    #
    order = [i for i in range(len(grid)**2)]
    random.shuffle(order)
    #
    while squares>0 and order!=[]:
        square = order.pop(0)
        line = square//len(grid)
        column = square%len(grid)
        #
        removeSquare = grid[line][column]
        grid[line][column] = "."
        squares -= 1
        #
        copyGrid = copy.deepcopy(grid)
        solveGrid(copyGrid)
        if copyGrid != originalGrid:
            squares += 1
            grid[line][column] = removeSquare       

if __name__ == "__main__":

    grid = [['1', '3', '4', '6', '8', '9', '5', '2', '7'],
['2', '5', '6', '3', '7', '1', '9', '4', '8'],
['8', '7', '9', '5', '2', '4', '6', '3', '1'],
['3', '4', '5', '8', '6', '2', '7', '1', '9'],
['9', '6', '2', '1', '4', '7', '8', '5', '3'],
['7', '8', '1', '9', '5', '3', '4', '6', '2'],
['5', '1', '3', '7', '9', '6', '2', '8', '4'],
['6', '2', '7', '4', '1', '8', '3', '9', '5'],
['4', '9', '8', '2', '3', '5', '1', '7', '6']]

    removeNum(grid)

    for line in grid:
        print(line)