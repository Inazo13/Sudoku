import pygame
import copy

import Ruleset
import fileManager
import FillGrid
import removeNum
import solveGrid
# pygame setup
pygame.init()
pygame.mixer.music.load("acoustic_music.mp3")
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
running = True

victory=False
lose=False
grilleEnCours=False
generate = False
defaultDiff=1
Diff=0
triche=False

#Si utilisateur souhaite résoudre la grille
solve=False

#partie def et grille
x=y=50

#test text surface
pygame.font.init()
text_font = pygame.font.SysFont('microsofthimalaya', 40)

#test image affichage
img=pygame.image.load('save.png')
small_img = pygame.transform.scale(img, (30, 30))
save_hitobx = pygame.Rect(740, 10, 25, 25) 

#affichage du bouton solve
buttonSolve=pygame.image.load("solve.png")
solve_small = pygame.transform.scale(buttonSolve, (70, 70))
save2_hitobx = pygame.Rect(770, 5, 75, 40) 

#victoire/défaite
death=pygame.image.load("YOU_DIED.png")
Victory=pygame.image.load("VICTORY_ACHIEVED.png")
Victory_resize=pygame.transform.scale(Victory, (1280, 720))


#input cell test
base_font = pygame.font.Font(None, 25) 
user_text = '' 
input_rect = pygame.Rect(740, 200, 30, 30) 
color_active = (pygame.Color('lightskyblue3') )
color_passive = (135, 195, 143) 
color = color_passive 
active = False

#deuxieme input cell
size_test=''
input_cell=pygame.Rect(740, 70, 30,30)
size_color=color_passive
size_active=False

#troisieme cellule charger fichiers
grilleACharger=''
celluleACharger=pygame.Rect(740, 750, 30,30)
load_color=color_passive
grilleChargee=False

#boutons difficulté
ez_diff = pygame.Rect(740, 150, 25, 25) 
mid_diff = pygame.Rect(770, 150, 25, 25) 
hard_diff = pygame.Rect(800, 150, 25, 25) 
hardplus_diff = pygame.Rect(830, 150, 25, 25) 
demon_diff = pygame.Rect(860, 150, 25, 25) 

#dessine une grille et affiche les cases pré-remplies
def drawEmptyGrid(size, grid):
    screen.fill((28, 110, 140))
    ecart=720/(size*size)
    for loop in range (size*size):
        i=0
        j=0
        #compteur=0
        while (i*ecart)<720:
            while (j*ecart)<720:
                if grid[loop][i]!=".":
                    pygame.draw.rect(screen,"lavender", pygame.Rect((i*ecart)+15, (loop*ecart)+15, ecart+0.2, ecart+0.2))
                else:
                    pygame.draw.rect(screen,"lightsteelblue2", pygame.Rect((i*ecart)+15, (loop*ecart)+15, ecart+0.2, ecart+0.2))
                #cast=str(compteur)
                #text_surface = my_font.render(cast, False, (0, 0, 0))
                #screen.blit(text_surface, ((i*ecart)+20,(loop*ecart)+15))
                i+=1
                j+=1
                #compteur+=1
    pygame.draw.rect(screen, (35,25,70), pygame.Rect(15, 15, 720, 720), 5)
    i = 1
    while (i*ecart) < 720:
        line_width = 2 if i % size > 0 else 4
        pygame.draw.line(screen, (35,25,70), pygame.Vector2((i*ecart) + 15, 15), pygame.Vector2((i * ecart) + 15, 730), line_width)
        pygame.draw.line(screen, (35,25,70), pygame.Vector2(15, (i * ecart) + 15), pygame.Vector2(730, (i * ecart) + 15), line_width)
        i += 1

#deuxieme def prends la case choisie par l'utilisateur
def inputUser(size):
    x,y=pygame.mouse.get_pos()
    if ((x>=15)& (x<=735)) & ((y>15)&(y<=735)):
        ligne=0
        column=0
        ecart=720/(size*size)
        #print(x)
        while(x>(((ligne+1)*ecart)+15)):
            ligne+=1
        #print y
        while(y>(((column+1)*ecart)+15)):
            column+=1
        #pygame.draw.rect(screen, "violet",pygame.Rect((ligne*ecart)+15,(column*ecart)+15, ecart,ecart))
        print("ligne: ", ligne, "colonne", column)   
        return ligne,column
    return None, None

#dessine la grille
def drawGrid(grid, size):
    ecart=720/(size*size)
    i=0
    j=0
    for i in range (size*size):
        for j in range (size*size):
            cast=str(grid[j][i])
            if cast!=".":
                text_surface = my_font.render(cast, False, (0, 0, 0))
                if size>=5:
                    screen.blit(text_surface, ((i*ecart)+20,(j*ecart)+15))
                else:
                    screen.blit(text_surface, ((i*ecart)+(ecart/2),(j*ecart)+(ecart/3)))

#test si la case choisie est valide et peut être remplie
#ATTENTION NE PRENDS PAS EN COMPTE LES VALEURS POSSIBLES DONC ON PEUT METTRE DES ?? EN INPUT
def testValid(ligne, column, grid, fillerGrid):
    if (user_text!="") & (ligne!=None) & (column!=None):
        if grid[column][ligne]==".":
            print("valid")
            fillerGrid[column][ligne]=user_text
            print(grid)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #test encore pour la cellule input
        if event.type == pygame.MOUSEBUTTONDOWN: 
            ligne, column= inputUser(size)
            if grilleEnCours==True:
                testValid(ligne,column, grid, fillerGrid)
            
            if input_rect.collidepoint(event.pos): 
                active = True
            else: 
                active = False

            if input_cell.collidepoint(event.pos):
                size_active=True
            else:
                size_active=False

            if celluleACharger.collidepoint(event.pos):
                grilleChargee=True
            else:
                grilleChargee=False
            
            if save_hitobx.collidepoint(event.pos):
                if ((fileManager.userpath!='\.')&(grilleEnCours==True)):
                    fileManager.saveGrid(grid, fillerGrid)
                else:
                    print("pas de grille en cours")
            
            if save2_hitobx.collidepoint(event.pos):
                solve=True
                triche=True

            if ez_diff.collidepoint(event.pos):
                Diff=1
                generate=False
            if mid_diff.collidepoint(event.pos):
                Diff=2
                generate=False
            if hard_diff.collidepoint(event.pos):
                Diff=3
                generate=False
            if hardplus_diff.collidepoint(event.pos):
                Diff=4
                generate=False
            if demon_diff.collidepoint(event.pos):
                Diff=5
                generate=False
  
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_BACKSPACE: 
                if active==True:
                    user_text = user_text[:-1] 
                elif size_active==True:
                    size_test = size_test[:-1] 
                elif grilleChargee==True:
                    grilleACharger = grilleACharger[:-1]
            else: 
                if active==True:
                    if len(user_text)>=1:
                        user_text=event.unicode
                    else:
                        user_text += event.unicode
                elif size_active==True:
                    if pygame.key.name(event.key).isdigit():
                        if len(size_test)>=1:
                            size_test=event.unicode
                            print(size_test)
                        else:
                            size_test+=event.unicode
                            generate=False
                elif grilleChargee==True:
                    grilleACharger+=event.unicode

    screen.fill((28, 110, 140)) 

    #Charger une partie antérieure (PROBLEME AVEC LES TAILLES DE GRILLE)
    #a noter que si le fichier n'est pas au bon formatage de grille il y aura des problèmes et que actuellement ça bloque le progrès antérieur
    if grilleChargee==True:
        if fileManager.testExistence(fileManager.userpath, grilleACharger)==True:
            filepath=fileManager.userpath+grilleACharger+".json"
            lines=fileManager.loadGrid(filepath)
            grid, fillerGrid, size= fileManager.getGrids(lines)

    #changement de la taille de grille
    if (size_test>='2') & (size_test<='6'):
        size=int(size_test)
    elif (size_test=='') | (size_test=='0'):
        size=1

    #génération/ mise en place de grille
    if (size>=2) & (size<=6):
        grilleEnCours=True
        if size==3:
            my_font = pygame.font.SysFont('microsofthimalaya', 80)
        elif size==2:
            my_font = pygame.font.SysFont('microsofthimalaya', 90)
        elif size==4:
            my_font = pygame.font.SysFont('microsofthimalaya', 60)
        elif size==6:
            my_font = pygame.font.SysFont('microsofthimalaya', 30)
        elif size==5:
            my_font = pygame.font.SysFont('microsofthimalaya', 40)
        else:
            my_font = pygame.font.SysFont('microsofthimalaya', 40)
        if Diff==0:
            Diff=defaultDiff
        if generate==False:
            if size==5 or size==6:
                grid = FillGrid.generateGrid2(size)
                removeNum.removeNum(grid, Diff, True)
            else:
                grid = FillGrid.generateGrid(size)
                if size==4:
                    removeNum.removeNum(grid, Diff, True)
                else:
                    removeNum.removeNum(grid, Diff)
            generate = True
            fillerGrid = copy.deepcopy(grid)
        drawEmptyGrid(size, grid)
        drawGrid(fillerGrid, size)
    else:
        grilleEnCours=False

    #Résoud la grille si demandé
    if solve==True: 
        fillerGrid=grid
        solveGrid.solveGrid(grid)
        drawEmptyGrid(size, fillerGrid)
        drawGrid(fillerGrid, size)
        solve=False
        if size=='':
            triche=False

    if grilleEnCours==True:
        if (Ruleset.emptyNum(fillerGrid)==False) & (triche==False):
            SolvedGrid=copy.deepcopy(grid)
            solveGrid.solveGrid(SolvedGrid)
            if (SolvedGrid==fillerGrid):
                victory=True
            else:
                lose=True
        else:
            victory=False
            lose=False

    #zone de saisie numéro 1
    if active: 
        color = color_active 
    else: 
        color = color_passive 
    pygame.draw.rect(screen, color, input_rect) 
    text_surface = base_font.render(user_text, True, (255, 255, 255)) 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
    input_rect.w = max(5, text_surface.get_width()+10) 

    #zone de saisie numero 2
    if size_active:
        size_color=color_active
    else:
        size_color=color_passive
    pygame.draw.rect(screen, size_color, input_cell)
    text_surface_size = base_font.render(size_test, True, (255, 255, 255))
    screen.blit(text_surface_size, (input_cell.x+5, input_cell.y+5)) 
    input_cell.w = max(5, text_surface_size.get_width()+10) 

    #zone de saisie numéro 3
    if grilleChargee:
        load_color=color_active
    else:
        load_color=color_passive
    pygame.draw.rect(screen, load_color, celluleACharger)
    text_surface_load=base_font.render(grilleACharger, True, (255, 255, 255))
    screen.blit(text_surface_load, (celluleACharger.x+5, celluleACharger.y+5))
    celluleACharger.w=max(5, text_surface_load.get_width()+10)
    
    #text zone de saisie
    text_surface = text_font.render('Zone de saisie', False, (255, 255, 255))
    screen.blit(text_surface, (760,200))
    #texte taille de la grille
    text_surface2 = text_font.render('Taille de la grille', False, (0, 0, 0))
    screen.blit(text_surface2, (760,70))
    #texte charger partie
    text_surface3 = text_font.render('Charger une partie', False, (0, 0, 0))
    screen.blit(text_surface3, (740,715))
    #texte difficulté
    text_surface4 = text_font.render('Difficulté', False, (0, 0, 0))
    screen.blit(text_surface4, (740,120))

    #test image
    screen.blit(small_img,(740,10))
    screen.blit(solve_small,(780, -8))
    if lose==True:
        screen.blit(death, (-450,-150))
    if victory==True:
        screen.blit(Victory_resize, (-100, 0))
    
    #boutons de difficulté
    pygame.draw.rect(screen, (57,211,126),ez_diff)
    pygame.draw.rect(screen, (231,239,76),mid_diff)
    pygame.draw.rect(screen, (252,176,35),hard_diff)
    pygame.draw.rect(screen, (198,36,3),hardplus_diff)
    pygame.draw.rect(screen, (0,0,1),demon_diff)

    #esthétique bouton difficulté
    if Diff==1:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(740, 150, 25, 25), 3)
    elif Diff==2:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(770, 150, 25, 25), 3)
    elif Diff==3:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(800, 150, 25, 25), 3)
    elif Diff==4:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(830, 150, 25, 25), 3)
    elif Diff==5:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(860, 150, 25, 25), 3)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()