import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, sys
from py.game import game
from py.credits import credits
from py.how2play import h2p

# initializing the constructor
pygame.init()

# shorthand events
def imgload(img): return pygame.image.load(img)

# screen resolution
SCREEN_DIMENSIONS = [580, 450]
bg = imgload("assets/other/backdrop.png")
bg = pygame.transform.scale(bg, SCREEN_DIMENSIONS)
logo = imgload("assets/other/logo.png")
logo = pygame.transform.scale(logo, [390, 130])
screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
height, width = screen.get_height(), screen.get_width()
pygame.display.set_caption("Recycle It!")
icon = imgload("assets/other/icon.png")
pygame.display.set_icon(icon)

# colors
SKY_BLUE = (125, 175, 255)
WHITE = (255, 255, 255)
LIGHT_GREY = (175, 175, 175)
DARK_GREY = (100, 100, 100)
LIGHT_GREEN = (63, 196, 47)
LIGHT_RED = (240, 36, 22)
DARK_GREEN = (49, 158, 36)
DARK_RED = (199, 30, 18)
DARK_BLUE = (21, 42, 176)
LIGHT_BLUE = (44, 71, 242)
DARK_ORANGE = (186, 172, 20)
LIGHT_ORANGE = (230, 212, 25)

smallfont = pygame.font.SysFont('Corbel', 35)
smallerfont = pygame.font.SysFont('Corbel', 32)

# buttons
# imgload = pygame.image.load()
start_light = imgload("assets/buttons/start_light.png")
start_light = pygame.transform.scale(start_light,[140,40])
start_dark = imgload("assets/buttons/start_dark.png")
start_dark = pygame.transform.scale(start_dark,[140,40])

h2p_light = imgload("assets/buttons/h2p_light.png")
h2p_light = pygame.transform.scale(h2p_light,[140,40])
h2p_dark = imgload("assets/buttons/h2p_dark.png")
h2p_dark = pygame.transform.scale(h2p_dark,[140,40])

credits_light = imgload("assets/buttons/credits_light.png")
credits_light = pygame.transform.scale(credits_light,[140,40])
credits_dark = imgload("assets/buttons/credits_dark.png")
credits_dark = pygame.transform.scale(credits_dark,[140,40])

quit_light = imgload("assets/buttons/quit_light.png")
quit_light = pygame.transform.scale(quit_light,[140,40])
quit_dark = imgload("assets/buttons/quit_dark.png")
quit_dark = pygame.transform.scale(quit_dark,[140,40])

running = True
while running:
  # stores the (x,y) coordinates into
  # the variable as a tuple
  mouse = pygame.mouse.get_pos()
  screen.blit(bg, (0, 0))
  screen.blit(logo, (93, 50))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      # initiate game // see game.py
      if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20: 
        game()
      elif width/2-70 <= mouse[0] <= width/2+70 and height/2+165 <= mouse[1] <= height/2+205: 
        running = False
      elif width/2-70 <= mouse[0] <= width/2+70 and height/2+103 <= mouse[1] <= height/2+143: 
        credits()
      elif width/2-70 <= mouse[0] <= width/2+70 and height/2+41 <= mouse[1] <= height/2+71: 
        h2p()
          
  # buttons // change colors when hovering [Start, How To Play, Credits, Quit]
  if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20: screen.blit(start_light, [width/2-70,height/2-20])
  else: screen.blit(start_dark, [width/2-70,height/2-20])
  
  if width/2-70 <= mouse[0] <= width/2+70 and height/2+165 <= mouse[1] <= height/2+205: screen.blit(quit_light,[width/2-70,height/2+165])
  else: screen.blit(quit_dark,[width/2-70,height/2+165])

  if width/2-70 <= mouse[0] <= width/2+70 and height/2+103 <= mouse[1] <= height/2+143: screen.blit(credits_light,[width/2-70,height/2+103])
  else: screen.blit(credits_dark,[width/2-70,height/2+103])

  if width/2-70 <= mouse[0] <= width/2+70 and height/2+41 <= mouse[1] <= height/2+71: screen.blit(h2p_light,[width/2-70,height/2+41])
  else: screen.blit(h2p_dark,[width/2-70,height/2+41])

  # updates the frames of the game
  pygame.display.update()
  
pygame.quit()