import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs (RGB)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

# Définition de la taille de la fenêtre du jeu
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Mode infini")

# Position initiale du personnage
x_personnage = 0
y_personnage = 0

# Taille du personnage
largeur_personnage = 50
hauteur_personnage = 50

# Vitesse initiale du personnage
vitesse_verticale = 0

# Constantes de saut
GRAVITE = 0.5
FORCE_DU_SAUT = 10

# Points de vie du personnage
points_de_vie = 10

# Plateformes
plateformes = []

# Marées
marees = []

# Génération de niveau aléatoire
def generer_niveau():
    global plateformes, marees, x_personnage, y_personnage, points_de_vie

    # Génération de plateformes aléatoires
    plateformes.clear()
    for i in range(10):
        x = random.randint(0, largeur_fenetre - 100)
        y = random.randint(0, hauteur_fenetre - 30)
        largeur = random.randint(50, 200)
        hauteur = random.randint(10, 30)
        plateforme = pygame.Rect(x, y, largeur, hauteur)
        plateformes.append(plateforme)

    # Génération d'une plateforme pour le personnage
    x_personnage = random.randint(0, largeur_fenetre - largeur_personnage)
    y_personnage = random.randint(0, hauteur_fenetre - hauteur_personnage)
    plateforme_personnage = pygame.Rect(x_personnage, y_personnage, largeur_personnage, hauteur_personnage)
    plateformes.append(plateforme_personnage)

    # Réinitialisation des points de vie
    points_de_vie = 10

    # Génération de marées aléatoires
    marees.clear()
    for i in range(5):
        x = random.randint(0, largeur_fenetre - 100)
        largeur = random.randint(50, 200)
        maree = pygame.Rect(x, hauteur_fenetre - 10, largeur, 10)
        marees.append(maree)

# Boucle principale du jeu
en_cours = True
clock = pygame.time.Clock()

while en_cours and points_de_vie > 0:
    # Limitation de la boucle principale à 60 images par seconde
    clock.tick(120)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        # Génération d'un nouveau niveau en appuyant sur la touche "Espace"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            generer_niveau()

    # Détection des touches enfoncées
    touches = pygame.key.get_pressed()
    if touches[pygame.K_z]:
        y_personnage -= 5
    if touches[pygame.K_q]:
        x_personnage -= 5
    if touches[pygame.K_s]:
        y_personnage += 5
    if touches[pygame.K_d]:
        x_personnage += 5

    # Gestion du saut du personnage avec la touche "Espace"
    if touches[pygame.K_SPACE] and vitesse_verticale == 0:
        vitesse_verticale = -FORCE_DU_SAUT

    # Mise à jour de la position verticale du personnage avec la gravité
    y_personnage += vitesse_verticale
    vitesse_verticale += GRAVITE

    # Limiter la position verticale du personnage au sol
    if y_personnage >= hauteur_fenetre - hauteur_personnage:
        y_personnage = hauteur_fenetre - hauteur_personnage
        vitesse_verticale = 0

    # Vérifier les collisions avec les plateformes
    for plateforme in plateformes:
        if plateforme != plateformes[-1] and plateforme.colliderect(pygame.Rect(x_personnage, y_personnage, largeur_personnage, hauteur_personnage)) and vitesse_verticale > 0:
            y_personnage = plateforme.top - hauteur_personnage
            vitesse_verticale = 0

    # Vérifier les collisions avec les marées
    for maree in marees:
        if maree.colliderect(pygame.Rect(x_personnage, y_personnage, largeur_personnage, hauteur_personnage)):
            # La marée fait des dégâts au personnage
            points_de_vie -= 3
            print("Le personnage a été touché par la marée ! Points de vie restants :", points_de_vie)
            pygame.time.delay(1000)  # Pause de 1 seconde après avoir été touché

    # Limiter les points de vie entre 0 et 10
    if points_de_vie < 0:
        points_de_vie = 0
    elif points_de_vie > 10:
        points_de_vie = 10

    # Affichage du fond d'écran
    fenetre.fill(BLANC)

    # Affichage des plateformes
    for plateforme in plateformes[:-1]:
        pygame.draw.rect(fenetre, NOIR, plateforme)

    # Affichage des marées
    for maree in marees:
        pygame.draw.rect(fenetre, BLEU, maree)

    # Calcul de la largeur de la barre de vie
    largeur_barre_vie = (points_de_vie / 10) * largeur_personnage

    # Affichage de la barre de vie
    pygame.draw.rect(fenetre, VERT, (x_personnage, y_personnage - 10, largeur_barre_vie, 5))
    pygame.draw.rect(fenetre, ROUGE, (x_personnage + largeur_barre_vie, y_personnage - 10, largeur_personnage - largeur_barre_vie, 5))

    # Affichage du personnage
    pygame.draw.rect(fenetre, ROUGE, (x_personnage, y_personnage, largeur_personnage, hauteur_personnage))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Vérifier si le personnage est mort
    if points_de_vie == 0:
        pygame.time.delay(1000)  # Pause de 1 seconde avant de respawn
        generer_niveau()

# Fermeture de Pygame
pygame.quit()
sys.exit()
