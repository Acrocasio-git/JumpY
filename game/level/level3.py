import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs (RGB)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

# Définition de la taille de la fenêtre du jeu
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu 2D simple")

# Position initiale du personnage
x_personnage = 800
y_personnage = 300

# Vitesse initiale du personnage
vitesse_verticale = 0

# Constantes de saut
GRAVITE = 0.5
FORCE_DU_SAUT = 10

# Plateformes
plateformes = [
    pygame.Rect(500, 500, 400, 20),
    pygame.Rect(10, 300, 100, 20),
    pygame.Rect(100, 400, 100, 20),
    pygame.Rect(500, 370, 200, 10)
]

# Piques
piques = [
    pygame.Rect(0, hauteur_fenetre - 10, largeur_fenetre, 10)
]

# Points de vie du personnage
points_de_vie = 10

# Boucle principale du jeu
en_cours = True
clock = pygame.time.Clock()

while en_cours:
    # Limitation de la boucle principale à 120 images par seconde
    clock.tick(120)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        # Gestion de l'appui sur la touche "espace" pour le saut
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            vitesse_verticale = -FORCE_DU_SAUT

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

    # Mise à jour de la position verticale du personnage avec la gravité
    y_personnage += vitesse_verticale
    vitesse_verticale += GRAVITE

    # Limiter la position verticale du personnage au sol
    if y_personnage >= hauteur_fenetre - 50:
        y_personnage = hauteur_fenetre - 50
        vitesse_verticale = 0

    # Vérifier les collisions avec les plateformes
    for plateforme in plateformes:
        if plateforme.colliderect(pygame.Rect(x_personnage, y_personnage, 50, 50)) and vitesse_verticale > 0:
            y_personnage = plateforme.top - 50
            vitesse_verticale = 0

    # Vérifier les collisions avec les piques
    for pique in piques:
        if pique.colliderect(pygame.Rect(x_personnage, y_personnage, 50, 50)):
            points_de_vie -= 3
            if points_de_vie <= 0:
                # Le personnage est mort, réinitialisation de la position
                x_personnage = plateformes[1].left
                y_personnage = plateformes[1].top
                points_de_vie = 10
            else:
                pygame.time.delay(1000)  # Pause d'une seconde

    # Limiter la position du personnage à l'écran
    if x_personnage < 0:
        x_personnage = 0
    if x_personnage > largeur_fenetre - 50:
        x_personnage = largeur_fenetre - 50
    if y_personnage < 0:
        y_personnage = 0
    if y_personnage > hauteur_fenetre - 50:
        y_personnage = hauteur_fenetre - 50

    # Affichage du fond d'écran
    fenetre.fill(BLANC)

    # Affichage des plateformes
    for plateforme in plateformes:
        pygame.draw.rect(fenetre, NOIR, plateforme)

    # Affichage des piques
    for pique in piques:
        pygame.draw.rect(fenetre, BLEU, pique)

    # Affichage du personnage
    pygame.draw.rect(fenetre, ROUGE, (x_personnage, y_personnage, 50, 50))

    # Affichage de la barre de vie
    barre_de_vie_largeur = 200
    barre_de_vie_hauteur = 20
    barre_de_vie_x = 10
    barre_de_vie_y = hauteur_fenetre - 600

    pygame.draw.rect(fenetre, NOIR, (barre_de_vie_x, barre_de_vie_y, barre_de_vie_largeur, barre_de_vie_hauteur))
    pygame.draw.rect(fenetre, ROUGE, (barre_de_vie_x, barre_de_vie_y, (points_de_vie / 10) * barre_de_vie_largeur, barre_de_vie_hauteur))

    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture de Pygame