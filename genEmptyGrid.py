from Parameters import inputSize
#https://www.delftstack.com/fr/howto/python/how-to-initiate-2-d-array-in-python/
def generateEmptyGrid(size):
    column, row = size**2, size**2
    grid = [["." for _ in range(row)] for _ in range(column)]
    #print(len(grid))
    return grid

#generateEmptyGrid()
