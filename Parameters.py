size=0
diff=["easy", "medium", "hard", "diabolic"]
def inputSize():
    desiredSize=int(input("saisissez un nombre entre 2 et 6 pour la taille de grille: "))
    while (desiredSize>6 or desiredSize<2):
        desiredSize=int(input("saisissez un nombre entre 2 et 6 pour la taille de grille: "))
    size=desiredSize
    return size

def chooseDiff(diff):
    desiredDiff=int(input("choix difficulté entre 0 et 3: "))
    while (desiredDiff>3 or desiredDiff<0):
        desiredDiff=int(input("choix de la difficulté entre 0 et 3: "))
    return diff[desiredDiff]