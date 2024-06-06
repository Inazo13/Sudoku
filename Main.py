import pygame
import copy

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
running = True

#grid setup
size=3
grilleEnCours=False

#partie def et grille
x=y=50

#test text surface
pygame.font.init() 
text_font = pygame.font.SysFont('microsofthimalaya', 40)

#test de grille
if size==3:
    grid=[[7, ".", 5, 2, ".", 3, 4, ".", 6], [1, ".", 9, 4, 5, 6, ".", 8, 3],[4, 6, ".", 9, 7, ".", 2, 5, "."],[2, 1, ".", 3, 6, 9, 5, ".", 4],[5, 9, ".", 7, 2, ".", 6, ".", 8],[".", ".", ".", 5, ".", 4, ".", 1, "."],[6, ".", ".", ".", 9, 5, ".", 4, "."],[".", 5, ".", ".", 4, ".", ".", 2, 9],[9, ".", 7, ".", ".", 2, ".", 6, 5]]
elif size==4:
    grid=[[1, 3, 'f', 'e', 'c', 5, 9, 'g', 6, 4, 8, 'a', 'b', 7, 2, 'd'],[5, 4, 'g', 'b', 1, 8, 6, 'a', 9, 2, 7, 'd', 3, 'f', 'c', 'e'],[9, 'c', 2, 7, 'd', 3, 'f', 'b', 5, 'e', 1, 'g', 6, 4, 8, 'a'],['d', 6, 8, 'a', 2, 'e', 4, 7, 3, 'b', 'c', 'f', 'g', 1, 5, 9],[3, 9, 'a', 1, 'g', 7, 'c', 'd', 8, 5, 4, 2, 'e', 'b', 6, 'f'],['g', 'e', 4, 'f', 'b', 1, 'a', 2, 7, 'd', 9, 6, 8, 'c', 3, 5],[2, 7, 'd', 'c', 'f', 6, 5, 8, 'e', 'g', 3, 'b', 9, 'a', 1, 4],[8, 'b', 6, 5, 4, 9, 3, 'e', 1, 'f', 'a', 'c', 'd', 2, 'g', 7],[7, 5, 9, 3, 6, 'a', 'e', 'f', 4, 1, 'b', 8, 2, 'g', 'd', 'c'],['a', 'f', 'b', 2, 8, 'd', 1, 4, 'c', 3, 'g', 9, 5, 'e', 7, 6],['c', 8, 1, 'g', 9, 2, 7, 5, 'f', 6, 'd', 'e', 'a', 3, 4, 'b'],[6, 'd', 'e', 4, 3, 'b', 'g', 'c', 'a', 7, 2, 5, 'f', 8, 9, 1],['e', 1, 'c', 6, 'a', 4, 'b', 9, 2, 8, 5, 3, 7, 'd', 'f', 'g'],[4, 2, 3, 9, 5, 'f', 'd', 1, 'g', 'a', 'e', 7, 'c', 6, 'b', 8],['b', 'g', 7, 8, 'e', 'c', 2, 6, 'd', 9, 'f', 1, 4, 5, 'a', 3],['f', 'a', 5, 'd', 7, 'g', 8, 3, 'b', 'c', 6, 4, 1, 9, 'e', 2]]
elif size==5:
    grid=[[2, 4, 'c', 8, 'n', 'b', 1, 'o', 'a', 'k', 5, 6, 'l', 'g', 'd', 9, 7, 'm', 'i', 'f', 'p', 'h', 3, 'e', 'j'], ['a', 3, 6, 'd', 'h', 'e', 8, 7, 'l', 9, 4, 'c', 1, 'k', 'p', 'n', 'o', 'g', 'j', 'b', 'f', 'm', 'i', 5, 2], ['b', 'g', 'f', 'i', 'k', 'm', 2, 4, 'h', 'n', 'j', 8, 'a', 'e', 3, 'd', 'p', 5, 1, 'l', 'c', 9, 6, 7, 'o'], ['m', 5, 1, 7, 9, 'g', 'c', 'p', 'd', 'j', 'f', 'o', 'i', 'h', 'n', 3, 'k', 'e', 2, 6, 8, 'l', 4, 'b', 'a'], ['j', 'l', 'p', 'o', 'e', 3, 6, 5, 'i', 'f', 9, 2, 'b', 'm', 7, 'h', 4, 'a', 'c', 8, 'k', 'n', 'g', 1, 'd'], [1, 'j', 'o', 5, 2, 'h', 'n', 'm', 'a', 'e', 'p', 4, 8, 'k', 7, 'c', 6, 9, 'b', 3, 'i', 'l', 'f', 'g', 'd'], ['f', 'p', 'm', 7, 'g', 'k', 'b', 'd', 3, 4, 5, 'h', 1, 'a', 'l', 8, 'j', 'i', 'e', 'o', 6, 9, 'n', 'c', 2], ['i', 'b', 4, 'a', 'c', 9, 6, 8, 'f', 'o', 'e', 'g', 'j', 'd', 'n', 'h', 2, 'l', 5, 1, 3, 'k', 'm', 'p', 7], [8, 3, 9, 6, 'l', 'p', 1, 'j', 5, 'c', 'o', 'f', 'm', 'i', 2, 'g', 'k', 7, 'n', 'd', 'b', 'e', 4, 'a', 'h'], ['n', 'e', 'h', 'k', 'd', 'g', 'l', 7, 'i', 2, 6, 'b', 'c', 9, 3, 'f', 'm', 'a', 'p', 4, 'o', 'j', 1, 8, 5], ['m', 'b', 'c', 'k', 3, 'i', 'p', 'o', 9, 'n', 2, 5, 'g', 4, 8, 1, 'j', 'a', 'd', 'f', 'e', 6, 'l', 7, 'h'], [7, 6, 'f', 'd', 'p', 'e', 5, 'j', 1, 8, 'l', 'a', 3, 'o', 'c', 4, 'g', 'b', 'k', 'h', 'i', 9, 'n', 2, 'm'], ['g', 1, 'a', 9, 'j', 'b', 'h', 'k', 6, 'c', 'n', 7, 'p', 'f', 'e', 'o', 'l', 'm', 2, 'i', 8, 5, 3, 'd', 4], ['h', 'n', 4, 'i', 5, 2, 'g', 'd', 7, 'l', 1, 'm', 'j', 'b', 9, 'p', 6, 3, 'e', 8, 'f', 'k', 'o', 'c', 'a'], ['e', 'l', 8, 2, 'o', 3, 4, 'f', 'a', 'm', 'd', 'k', 'i', 6, 'h', 'n', 5, 9, 7, 'c', 1, 'g', 'b', 'j', 'p'], [8, 'd', 'h', 'e', 9, 'i', 1, 2, 'a', 4, 'l', 'm', 'g', 'o', 3, 6, 'c', 'k', 5, 'p', 7, 'b', 'n', 'j', 'f'], ['k', 1, 'j', 'm', 'g', 'c', 3, 5, 'f', 8, 'a', 'd', 7, 2, 4, 'e', 'n', 'i', 'b', 'h', 9, 6, 'l', 'p', 'o'], [3, 'p', 4, 'a', 6, 'j', 'm', 'o', 'n', 7, 'f', 'c', 5, 'h', 'b', 'g', 2, 'l', 8, 9, 1, 'k', 'e', 'i', 'd'], [7, 'i', 'f', 'b', 5, 'p', 'd', 'g', 'k', 'l', 9, 'e', 6, 'j', 'n', 4, 'm', 1, 'o', 3, 'a', 'c', 2, 'h', 8], ['o', 'n', 'l', 2, 'c', 9, 'e', 'h', 6, 'b', 1, 8, 'k', 'i', 'p', 7, 'a', 'f', 'j', 'd', 'm', 3, 'g', 5, 4], ['h', 7, 'f', 'e', 'i', 'l', 8, 'o', 'k', 'm', 'a', 3, 4, 2, 'd', 1, 'c', 'p', 'j', 'g', 'n', 'b', 5, 6, 9], [2, 6, 'j', 'd', 'g', 'a', 'h', 9, 'e', 'p', 'l', 'n', 'o', 'b', 8, 'f', 7, 'k', 5, 'i', 4, 1, 3, 'm', 'c'], [1, 9, 'm', 'l', 'b', 'g', 4, 5, 2, 6, 'f', 'e', 7, 'c', 'j', 3, 'o', 'n', 8, 'a', 'd', 'i', 'p', 'k', 'h'], ['p', 'n', 'c', 5, 'k', 'd', 'f', 3, 'j', 'b', 'h', 6, 1, 'm', 'i', 'l', 9, 'e', 4, 2, 8, 7, 'o', 'g', 'a'], [8, 'o', 'a', 4, 3, 7, 'n', 'i', 'c', 1, 5, 9, 'k', 'g', 'p', 'd', 'm', 'b', 'h', 6, 'f', 2, 'e', 'j', 'l']]
else:
    grid=[]
fillerGrid=copy.deepcopy(grid)

#input cell test
base_font = pygame.font.Font(None, 25) 
user_text = '' 
input_rect = pygame.Rect(740, 120, 30, 30) 
color_active = pygame.Color('lightskyblue3') 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 
active = False

#deuxieme input cell
size_test=''
input_cell=pygame.Rect(740, 70, 30,30)
size_color=color_passive
size_active=False

def drawEmptyGrid(size, grid):
    screen.fill(pygame.Color("darkslategray3"))
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
    pygame.draw.rect(screen, pygame.Color("chartreuse3"), pygame.Rect(15, 15, 720, 720), 5)
    i = 1
    while (i*ecart) < 720:
        line_width = 2 if i % size > 0 else 4
        pygame.draw.line(screen, pygame.Color("chartreuse3"), pygame.Vector2((i*ecart) + 15, 15), pygame.Vector2((i * ecart) + 15, 730), line_width)
        pygame.draw.line(screen, pygame.Color("chartreuse3"), pygame.Vector2(15, (i * ecart) + 15), pygame.Vector2(730, (i * ecart) + 15), line_width)
        i += 1

#deuxieme def prends la case choisie par l'utilisateur
def inputUser(size):
    x,y=pygame.mouse.get_pos()
    ligne=0
    column=0
    ecart=720/(size*size)
    if ((x>=15)& (x<=735)):
        #print(x)
        while(x>(((ligne+1)*ecart)+15)):
            ligne+=1
    if ((y>15)&(y<=735)):
        #print y
        while(y>(((column+1)*ecart)+15)):
            column+=1
    if ((y<=735)& (x<=735)):
        #pygame.draw.rect(screen, "violet",pygame.Rect((ligne*ecart)+15,(column*ecart)+15, ecart,ecart))
        print("ligne: ", ligne, "colonne", column)
    return ligne,column

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
#ATTENTION NE PRENDS PAS EN COMPTE LES VALEURS POSSIBLES DONC ON PEUT METTRE DES ? EN INPUT
def testValid(ligne, column, grid, fillerGrid):
    if user_text!="":
        if grid[column][ligne]==".":
            print("valid")
            fillerGrid[column][ligne]=user_text
            print(grid)

#Code pygame
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
  
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_BACKSPACE: 
                if active==True:
                    user_text = user_text[:-1] 
                elif size_active==True:
                    size_test = size_test[:-1] 
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

    
    screen.fill((131, 166, 200)) 

    #changement de la taille de grille
    if (size_test>='2') & (size_test<='6'):
        size=int(size_test)
    elif (size_test=='') | (size_test=='0'):
        size=1


    if (size>=2) & (size<=6):
        grilleEnCours=True
        if size==3:
            my_font = pygame.font.SysFont('microsofthimalaya', 80)
        elif size==4:
            my_font = pygame.font.SysFont('microsofthimalaya', 60)
        elif size==6:
            my_font = pygame.font.SysFont('microsofthimalaya', 30)
        elif size==5:
            my_font = pygame.font.SysFont('microsofthimalaya', 40)
        else:
            my_font = pygame.font.SysFont('microsofthimalaya', 40)
        drawEmptyGrid(size, grid)
        drawGrid(fillerGrid, size)
    else:
        grilleEnCours=False

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
    
    #text zone de saisie
    text_surface = text_font.render('Zone de saisie', False, (0, 0, 0))
    screen.blit(text_surface, (760,120))
    #texte taille de la grille
    text_surface2 = text_font.render('Taille de la grille', False, (0, 0, 0))
    screen.blit(text_surface2, (760,70))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()