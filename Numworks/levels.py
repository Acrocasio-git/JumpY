from ion import *
from kandinsky import *

fill_rect(0,0,396,206,"white")

draw_string("niveaux",160,15)

while True :
  fill_rect(30,35,25,20,"black")
  fill_rect(28,37,23,23,"blue")
  draw_string("1",33,39)
  if keydown(KEY_ONE) :
    import level1
  
  fill_rect(80,35,25,20,"black")
  fill_rect(78,37,23,23,"blue")
  draw_string("2",83,39)
  if keydown(KEY_TWO) :
    import level2
    
  fill_rect(130,35,25,20,"black")
  fill_rect(128,37,23,23,"blue")
  draw_string("3",133,39)
  if keydown(KEY_THREE) :
    import level2
  if keydown(KEY_ALPHA) :
    fill_rect(0,0,396,206,"white")
    import game jl