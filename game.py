from ion import *
from kandinsky import *
from os import *
import logo
exit = False
while exit != True:
  #bouton play
  fill_rect(135,105,130,30,"blue")
  fill_rect(137,107,126,26,"white")
  draw_string("play",180,110)
  
  #bouton exit
  fill_rect(135,145,130,30,"blue")
  fill_rect(137,147,126,26,"white")
  draw_string("exit",180,150)
  
  if keydown(KEY_UP) :
    while keydown(KEY_UP):
      fill_rect(137,107,126,26,"red")
      if keydown(KEY_SHIFT) or keydown(KEY_EXE) :
        import levels
  
  if keydown(KEY_DOWN) :
    while keydown(KEY_DOWN) :
      fill_rect(137,147,126,26,"red")
      if keydown(KEY_SHIFT) or keydown(KEY_EXE) :
        exit = True 