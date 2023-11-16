
# Importation des bibliothèques nécessaires
import pygame
import sys
import random
import time
import os
import ctypes
import pkg_resources
import io

#taille console
os.system('mode con: cols=32 lines=17')

# Déplacer la fenêtre tout à gauche de l'écran (x=0, y=100)
hwnd = ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.SetWindowPos(hwnd, -1,4, 100, 50, 2, 0x0001)

#bank color
class Colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
class Color:
    BG_WHITE = '\033[47m'

#debut du chrono
temps_debut = time.time()

#variable non classée
sup = 0
supp = 0
score = 0

# Définir la taille de l'écran
largeur, hauteur = 700, 500
taille_case = 50

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("deplacement avec: zqsd et les flèches")


# Chargez les images en utilisant pkg_resources
image_zero_data = pkg_resources.resource_string(__name__, 'zero.png')
image_croix_data = pkg_resources.resource_string(__name__, 'croix.png')
image_fond_data = pkg_resources.resource_string(__name__, 'fond_ecran.jpg')
image_piece_data = pkg_resources.resource_string(__name__, 'piece.png')
# Redimensionnez les images
image_zero = pygame.transform.scale(pygame.image.load(io.BytesIO(image_zero_data)), (taille_case + supp, taille_case + supp))
image_croix = pygame.transform.scale(pygame.image.load(io.BytesIO(image_croix_data)), (taille_case + sup, taille_case + sup))
fond_ecran = pygame.transform.scale(pygame.image.load(io.BytesIO(image_fond_data)), (largeur, hauteur))
image_piece = pygame.transform.scale(pygame.image.load(io.BytesIO(image_piece_data)), (taille_case, taille_case))

#efface la fenettre
os.system('cls' if os.name == 'nt' else 'clear')

# en tete
print(Colors.RED + "_______________________________"+Colors.RESET)
print(Colors.RED +"        PRISON BREAK           ")
print(Colors.RED + "_______________________________")



#positions initiales
x_croix, y_croix = largeur // 5, hauteur // 7
x, y = largeur // 2, hauteur // 2
x_piece, y_piece = random.randint(0, largeur - taille_case), random.randint(0, hauteur - taille_case)
# Horloge pour contrôler le temps
horloge = pygame.time.Clock()

#vitesse des joueur, g=croix=gardien v=zero=voleur
vitesseg = 8
vitessev = 10


while True:
  # Gestion des événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_g:
            vitesseg = vitesseg+5  # Changer la valeur de vitesseg à 12 lorsque la touche "g" est pressée
            sup = sup+20
            image_croix = pygame.transform.scale(pygame.image.load("croix.png"), (taille_case+sup, taille_case+sup))
            vitessev = 2
        elif evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_m:
            vitessev = vitessev+5  # Changer la valeur de vitessev à 12 lorsque la touche "m" est pressée
            supp = supp-20
            image_zero = pygame.transform.scale(pygame.image.load("zero.png"), (taille_case+supp, taille_case+supp))
            vitesseg = 2 


    temps_fin = time.time()
    duree = round(temps_fin - temps_debut)

    if duree > 60:
        pygame.quit()
        temps_fin = time.time()
        duree = round(temps_fin - temps_debut)
        print(Colors.YELLOW + " le voleur s'échappe!!!")
        print(" le score du voleur est: ", score)
        print(Colors.BLUE +" ____________________________")
        print("       YOU ARE FREE!!!")
        print(" ____________________________")
        input(Colors.YELLOW +"Appuie sur entrée pour quitter")
        SystemExit

# Gestion des déplacements du "0"
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and x > vitessev:
        x -= vitessev
    if touches[pygame.K_RIGHT] and x < largeur - vitessev:
        x += vitessev
    if touches[pygame.K_UP] and y > 0:
        y -= vitessev
    if touches[pygame.K_DOWN] and y < hauteur - vitessev:
        y += vitessev

        # Vérifier la collision avec le rond
    if (x <= x_croix <= x + taille_case  and
        y<= y_croix <= y + taille_case ) :
        pygame.quit()
        temps_fin = time.time()
        duree = round(temps_fin - temps_debut)
        print(Colors.YELLOW + " Tu as perdu!!")
        print("tu as survecu:", duree, " secondes.")
        print(" ton score est: ", score)
        print(Colors.BLUE +" ____________________________")
        print(" |  |  |  |  |  |  |  |  |  |")
        print(" |  |  |  | \|/\|/\|/ |  |  |")
        print(" |  |  |  |/ |  |  |\ |  |  |")
        print(" |  |  |  |  |O |O | ||  |  |")
        print(" |  |  |  |\_|__|__|/ |  |  |")
        print(" |  |  |  |/ |  |  |\ |  |  |")
        print(" |  |  | /|  |  |  | \|  |  |")
        print(" |__|__|_\|__|__|__|/_|__|__|")
        input(Colors.YELLOW +"Appuie sur entrée pour quitter")
        SystemExit
    if (x_piece <= x <= x_piece + taille_case  and
        y_piece <= y <= y_piece + taille_case ) or \
       (x  <= x_piece <= x + taille_case  and
        y <= y_piece <= y + taille_case ) :
        score=score+1
        x_piece, y_piece = random.randint(0, largeur - taille_case), random.randint(0, hauteur - taille_case)
# Gestion des déplacements du "X"
    touches = pygame.key.get_pressed()
    if touches[pygame.K_q] and x_croix > vitesseg:
        x_croix -= vitesseg
    if touches[pygame.K_d] and x_croix < largeur - vitesseg:
        x_croix += vitesseg
    if touches[pygame.K_z] and y_croix > 0:
        y_croix -= vitesseg
    if touches[pygame.K_s] and y_croix < hauteur - vitesseg:
        y_croix += vitesseg

# Vérifier la collision avec le croix
    if (x_croix <= x <= x_croix + taille_case + sup -1  and
        y_croix <= y <= y_croix + taille_case + sup -1) :
        pygame.quit()
        temps_fin = time.time()
        duree = round(temps_fin - temps_debut)
        print(Colors.YELLOW + " Tu as perdu!!")
        print("tu as survecu:", duree, " secondes.")
        print(" ton score est: ", score)
        print(Colors.BLUE+" ____________________________")
        print(" |  |  |  |  |  |  |  |  |  |")
        print(" |  |  |  | _|__|__|  |  |  |")
        print(" |  |  |  |/ |  |  |\ |  |  |")
        print(" |  |  |  |  |O |O | ||  |  |")
        print(" |  |  |  |\_|_-|__|/ |  |  |")
        print(" |  |  |  |/ |  |  |\ |  |  |")
        print(" |  |  | /|  |  |  | \|  |  |")
        print(" |__|__|_\|__|__|__|/_|__|__|")
        input(Colors.YELLOW +" Appuie sur entrée pour quitter")
        SystemExit
    if (x_piece <= x <= x_piece + taille_case  and
        y_piece <= y <= y_piece + taille_case ) or \
       (x  <= x_piece <= x + taille_case  and
        y <= y_piece <= y + taille_case ) :
        score=score+1
        x_piece, y_piece = random.randint(0, largeur - taille_case), random.randint(0, hauteur - taille_case)
# Effacer l'écran
    ecran.fill((255, 255, 255))


   # Vérifier la collision avec le croix
    if (x_croix <= x <= x_croix + taille_case + sup -1 and
        y_croix <= y <= y_croix + taille_case + sup -1) :
        pygame.quit()
        temps_fin = time.time()
        duree = round(temps_fin - temps_debut)
        print(Colors.YELLOW + " Tu as perdu!!")
        print(" tu as survecu:", duree, "secondes")
        print(" ton score est: ", score)
        print(Colors.BLUE+" ____________________________")
        print(" |  |  |  |  |  |  |  |  |  |")
        print(" |  |  |  | _|__|__|  |  |  |")
        print(" |  |  |  |/O|  |O |\ |  |  |")
        print(" |  |  |  |  |--|  | ||  |  |")
        print(" |  |  |  |\_|__|__|/ |  |  |")
        print(" |  |  |  |/ |  |  |\ |  |  |")
        print(" |  |  | /|  |  |  | \|  |  |")
        print(" |__|__|_\|__|__|__|/_|__|__|")
        input(Colors.YELLOW +"Appuie sur entrée pour quitter.")
        SystemExit
    if (x_piece <= x <= x_piece + taille_case  and
        y_piece <= y <= y_piece + taille_case ) or \
       (x  <= x_piece <= x + taille_case  and
        y <= y_piece <= y + taille_case ) :
        score=score+1
        x_piece, y_piece = random.randint(0, largeur - taille_case), random.randint(0, hauteur - taille_case)
# Dessiner le fond d'écran à l'arrière-plan
    ecran.blit(fond_ecran, (0, 0))

    # Dessiner le "0" à la position actuelle
    ecran.blit(image_zero, (x, y))

    # Dessiner les "x" à leurs positions actuelles
    ecran.blit(image_croix, (x_croix, y_croix))

    # Dessiner les "piecce" à leurs positions actuelles 
    ecran.blit(image_piece, (x_piece, y_piece))

    # Mettre à jour l'écran
    pygame.display.flip()


# Vérifier la collision avec le croix
    if (x_croix <= x <= x_croix + taille_case + sup -1 and
        y_croix <= y <= y_croix + taille_case + sup-1) :
        pygame.quit()
        temps_fin = time.time()
        duree = round(temps_fin - temps_debut)
        print(Colors.YELLOW + "Tu as perdu!!")
        print("tu as survecu:", duree, "secondes")
        print(" ton score est: ", score)
        print(Colors.BLUE+"____________________________")
        print("|  |  |  |  |  |  |  |  |  |")
        print("|  |  |  | _|__|__|  |  |  |")
        print("|  |  |  |/ |  |  |\ |  |  |")
        print("|  |  |  |  |X |X | ||  |  |")
        print("|  |  |  |\_|__|__|/ |  |  |")
        print("|  |  |  |/ |  |  |\ |  |  |")
        print("|  |  | /|  |  |  | \|  |  |")
        print("|__|__|_\|__|__|__|/_|__|__|")
        input(Colors.YELLOW +"Appuie sur entrée pour quitter -->")
        SystemExit
    if (x_piece <= x <= x_piece + taille_case  and
        y_piece <= y <= y_piece + taille_case ) or \
       (x  <= x_piece <= x + taille_case  and
        y <= y_piece <= y + taille_case ) :
        score=score+1
        x_piece, y_piece = random.randint(0, largeur - taille_case), random.randint(0, hauteur - taille_case)
            
    # Limiter le nombre d'images par seconde
    horloge.tick(30)