from ion import *
from kandinsky import *
from time import *

x_joueur = 205 
y_joueur = 140

vitesse_ver=0

gravite = 0.5
force_saut = 10

largeur_joueur = 10
hauteur_joueur = 10

while get_keys()!={"sqrt"}:
  
  fill_rect(0,0,396,220,color(255,255,255))
  #life
  fill_rect(5,5,55,5,"red")
  
  #plateformes
  fill_rect(200,150,55,5,"black")
  fill_rect(100,130,55,5,"black")
  fill_rect(300,100,55,5,"black")
  
  #joueur
  fill_rect(x_joueur,y_joueur,largeur_joueur,hauteur_joueur,"red")
  
  if keydown(KEY_SHIFT) and y_joueur >= 0:
    vitesse_ver =- force_saut
  y_joueur += vitesse_ver
  
  if y_joueur >= 240 - hauteur_joueur:
    y_joueur = 240 - hauteur_joueur
    vitesse_ver = 0
  if keydown(KEY_LEFT) and x_joueur > 0:
    x_joueur -= 1
  if keydown(KEY_RIGHT) and x_joueur < 396 - largeur_joueur:
    x_joueur += 1
  if keydown(KEY_UP) and y_joueur > 0:
    y_joueur -= 1  
  if keydown(KEY_DOWN) and y_joueur < 240 - hauteur_joueur:
    y_joueur += 1
    
  #marree
  fill_rect(0,200,396,10,"blue") > d