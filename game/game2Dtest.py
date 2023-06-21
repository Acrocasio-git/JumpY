import pygame
import sys

# Définition de la classe Button
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()

# Initialisation de Pygame
pygame.init()

# Définition des couleurs (RGB)
BLANC = (255, 255, 255)

# Définition de la taille de la fenêtre du jeu
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu 2D simple")

# États du jeu
ETAT_MENU = 0
ETAT_PARAMETRES = 1

# État initial du jeu
etat_jeu = ETAT_MENU

# Variables de paramètres
resolution = (largeur_fenetre, hauteur_fenetre)
fps = 60

# Fonction pour passer à l'état du jeu
def jouer():
    global etat_jeu
    etat_jeu = ETAT_JEU

# Fonction pour passer à l'état des paramètres
def parametres():
    global etat_jeu
    etat_jeu = ETAT_PARAMETRES

# Fonction pour mettre à jour les paramètres du jeu
def mettre_a_jour_parametres():
    global resolution, fps
    # Mettre à jour la résolution et les FPS en fonction des valeurs entrées dans la fenêtre de paramètres
    resolution = (int(input_resolution_text), int(input_resolution_text))
    fps = int(input_fps_text)

# Création des boutons
bouton_jouer = Button(200, 200, 200, 50, "Jouer", jouer)
bouton_parametres = Button(200, 300, 200, 50, "Paramètres", parametres)

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

        # Gestion des événements des boutons
        bouton_jouer.handle_event(event)
        bouton_parametres.handle_event(event)

    # Affichage du fond d'écran
    fenetre.fill(BLANC)

    if etat_jeu == ETAT_MENU:
        # Affichage des boutons
        bouton_jouer.draw(fenetre)
        bouton_parametres.draw(fenetre)

    elif etat_jeu == ETAT_PARAMETRES:
        # Affichage de la fenêtre de paramètres
        fenetre_parametres = pygame.display.set_mode((400, 200))
        pygame.display.set_caption("Paramètres")

        # Éléments de la fenêtre de paramètres
        font = pygame.font.SysFont(None, 30)
        text_resolution = font.render("Résolution (largeur x hauteur):", True, (0, 0, 0))
        text_fps = font.render("FPS (images par seconde):", True, (0, 0, 0))
        input_resolution = pygame.Rect(220, 50, 100, 30)
        input_fps = pygame.Rect(220, 100, 100, 30)
        input_resolution_text = str(resolution[0]) + " x " + str(resolution[1])
        input_fps_text = str(fps)
        bouton_valider = Button(170, 150, 100, 30, "Valider", mettre_a_jour_parametres)

        # Gestion des événements de la fenêtre de paramètres
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mettre_a_jour_parametres()
                elif event.key == pygame.K_ESCAPE:
                    etat_jeu = ETAT_MENU
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if input_resolution.collidepoint(event.pos):
                    # Activer l'édition de la résolution
                    editing_resolution = True
                    editing_fps = False
                elif input_fps.collidepoint(event.pos):
                    # Activer l'édition des FPS
                    editing_resolution = False
                    editing_fps = True
                else:
                    editing_resolution = False
                    editing_fps = False

        # Affichage des éléments de la fenêtre de paramètres
        fenetre_parametres.fill((255, 255, 255))
        fenetre_parametres.blit(text_resolution, (20, 55))
        fenetre_parametres.blit(text_fps, (20, 105))
        pygame.draw.rect(fenetre_parametres, (0, 0, 0), input_resolution, 2)
        pygame.draw.rect(fenetre_parametres, (0, 0, 0), input_fps, 2)
        fenetre_parametres.blit(input_resolution_text, (225, 55))
        fenetre_parametres.blit(input_fps_text, (225, 105))
        bouton_valider.draw(fenetre_parametres)

    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
sys.exit()