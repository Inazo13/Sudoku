from datetime import datetime
import json
import os.path
import math
#emplacement pour votre emplacement de préférence pour les fichiers sans ça la fonctionnalité sauvergarde n'est pas sauvergardée
userpath = "TextFiles\\"

grid=[[7, ".", 5, 2, ".", 3, 4, ".", 6], [1, ".", 9, 4, 5, 6, ".", 8, 3],[4, 6, ".", 9, 7, ".", 2, 5, "."],[2, 1, ".", 3, 6, 9, 5, ".", 4],[5, 9, ".", 7, 2, ".", 6, ".", 8],[".", ".", ".", 5, ".", 4, ".", 1, "."],[6, ".", ".", ".", 9, 5, ".", 4, "."],[".", 5, ".", ".", 4, ".", ".", 2, 9],[9, ".", 7, ".", ".", 2, ".", 6, 5]]
fillerGrid=[[7, 8, 5, 2, 8, 3, 4, 8, 6], [1, 8, 9, 4, 5, 6, 8, 8, 3],[4, 6, 8, 9, 7, 8, 2, 5, 8],[2, 1, 8, 3, 6, 9, 5, 8, 4],[5, 9, 8, 7, 2, 8, 6, 8, 8],[8, 8, 8, 5, 8, 4, 8, 1, 8],[6, 8, 8, 8, 9, 5, 8, 4, 8],[8, 5, 8, 8, 4, 8, 8, 2, 9],[9, 8, 7, 8, 8, 2, 8, 6, 5]]

def saveGrid (grid, fillerGrid):
    num = 0
    filepath=f"TextFiles\save{num}.json"
    while os.path.exists(filepath):
        num += 1
        filepath=f"TextFiles\save{num}.json"
    with open(filepath, 'w') as f:
        json.dump(grid, f)
        json.dump("\\", f)
        json.dump(fillerGrid, f)
    #return filepath

def loadGrid (filepath):
    with open (filepath, 'r') as f:
        lines = f.read()
        f.close()
    return lines

def toGrid(lines):
    ligne=0
    newLine=''
    for i in range (len(lines)):
        #if ((lines[i]=="[") & ((i!=0))):
            #ligne+=1
        if ((lines[i]=='"') | (lines[i]==",") | (lines[i]=="[") | (lines[i]=="]") | (lines[i]==" ") | (lines[i]=="\\")):
            z=0
        else:
            newLine+=lines[i]
        ligne=int(math.sqrt(len(newLine)))
    newGrid=[[] for i in range (ligne)]
    count=0
    #print(ligne)
    #print(newLine)
    for i in range(ligne):
        for j in range(ligne):
            newGrid[i].append(newLine[count])
            count+=1
    #print(ligne)
    return newGrid, int(math.sqrt(ligne))

def getGrids(lines):
    sampleGrid=''
    i=0
    while lines[i]!="\\":
        sampleGrid+=lines[i]
        i+=1
    grid, size=toGrid(sampleGrid)
    #print (grid)
    sampleGrid=""
    for j in range(len(lines)-i):
        sampleGrid+=lines[i+j]
    #print(sampleGrid)
    fillerGrid, size=toGrid(sampleGrid)
    #print (fillerGrid)
    return grid, fillerGrid, size

    

def testExistence(userpath, filename):
    filepath=userpath+filename+".json"
    print(filepath)
    test=os.path.exists(filepath)
    return test

#saveGrid(grid, fillerGrid, userpath)
#lines=loadGrid(userpath+"05-06-2024_09-26-35.json")
#getGrids(lines)