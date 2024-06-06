#fichier avec les règles du sudoku
import math
#Si on prends que chaque tableau de la grille est une ligne du sudoku

#i et j sont les coordonnées de la case que on veut changer
#grid est la grille de sudoku
#x est le nombre que on souhaite placer dans la case

def limitPool(grid):
    pool=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0"]
    possPool=[]
    for loop in range (len(grid)):
        possPool+=[(pool[loop])]
    return possPool

def emptyNum(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j]=='.':
                return True
    return False

def searchLine (grid, line, num):
    hit=False
    for size in range(len(grid)): 
        if grid[line][size]==num:
            hit=True
    return hit

def searchColumn (grid, column, num):
    hit=False
    for size in range(len(grid)): 
        if grid[size][column]==num:
            hit=True
    return hit

def searchCell(grid, line, column, num):
    hit=False
    i=int(line-(line%math.sqrt(len(grid))))
    j=int(column-(column%math.sqrt(len(grid))))
    for loop1 in range (i, int(i+math.sqrt(len(grid)))):
        for loop2 in range (j, int(j+math.sqrt(len(grid)))):
                if grid[loop1][loop2]==num:
                    hit=True
    return hit

def valid(grid, line, column, num):
    hitLigne = searchLine(grid, line, num)
    hitColonne = searchColumn(grid, column, num)
    hitCell = searchCell(grid, line, column, num)
    if hitLigne==False and hitColonne==False and hitCell==False:
        return True
    return False


"""#grid est la grille de sudoku
#x est le nombre que on souhaite placer dans la case

def searchLine (grid, ligne, x):
    tailleTab=int(math.sqrt(len(grid)))
    hit=False
    y=(ligne-1)//tailleTab
    for i in range(y*tailleTab, (y+1)*tailleTab):
        for j in range(((ligne-1)%tailleTab)*tailleTab, ((ligne-1)%tailleTab+1)*tailleTab):
            if grid[i][j]==x:
                hit=True
    return hit

def searchColumn (grid, colonne, x):
    tailleTab=int(math.sqrt(len(grid)))
    hit=False
    y=(colonne-1)//tailleTab
    z=(colonne-1)%tailleTab
    for i in range(0+y, ((tailleTab-1)*tailleTab)+(y+1), tailleTab):
        for j in range(0+z, ((tailleTab-1)*tailleTab)+(z+1), tailleTab):
            if grid[i][j]==x:
                hit=True
    return hit

def searchCell(grid, ind, x):
    hit=False
    for val in grid[ind]:
        if val==x:
            hit=True
    return hit

def findLine(grid, cell, i):
    # valeurs de cell et i sont celles en informatique, avec comme 1ère valeur 0
    tailleTab=int(math.sqrt(len(grid)))
    line = ((i//tailleTab)+1)+(cell//tailleTab)*tailleTab
    return line

def findColumn(grid, cell, i):
    # valeurs de cell et i sont celles en informatique, avec comme 1ère valeur 0
    tailleTab=int(math.sqrt(len(grid)))
    column = ((i%tailleTab)+1)+(cell%tailleTab)*tailleTab
    return column"""