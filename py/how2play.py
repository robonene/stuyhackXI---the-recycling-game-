# setup stuff
import pygame, sys, random
from pygame.locals import *
from py.game import game

def h2p():
  pygame.init()

  # colors
  SKY_BLUE = (125, 175, 255)
  WHITE = (255, 255, 255)
  LIGHT_GREY = (175, 175, 175)
  DARK_GREY = (100, 100, 100)
  
  # variables and constants before the game starts
  running = True
  SCREEN_DIMENSIONS = [580, 450]
  screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
  height = screen.get_height()
  width = screen.get_width()
  back_light = pygame.image.load("assets/buttons/back_light.png")
  back_light = pygame.transform.scale(back_light,[140,40])
  back_dark = pygame.image.load("assets/buttons/back_dark.png")
  back_dark = pygame.transform.scale(back_dark,[140,40])
  pygame.display.set_caption("Recycle It!")
  icon = pygame.image.load("assets/other/icon.png")
  pygame.display.set_icon(icon)
  font = pygame.font.SysFont("Corbel", 35)
  bigFont = pygame.font.SysFont("Corbel", 30)
  quitButton = font.render("Menu", True, WHITE)
  font = pygame.font.SysFont("Corbel", 27)
  recycle = font.render("Recyclables:", True, WHITE)
  recycleSize = recycle.get_width()
  trash = font.render("Trash:", True, WHITE)
  trashSize = trash.get_width()
  h2p = font.render("Use the mouse and click", True, WHITE)
  h2p2 = font.render("or press SPACE to pick up items.", True, WHITE)
  h2p3 = font.render("Drag the items to the correct bins", True, WHITE)
  h2p4 = font.render("to drop them in.", True, WHITE)
  bg = pygame.image.load("assets/other/backdrop.png")
  bg = pygame.transform.scale(bg, SCREEN_DIMENSIONS)

  # items
  sprite1 = pygame.transform.scale(pygame.image.load("assets/items/can.png"), [70, 70])
  sprite2 = pygame.transform.scale(pygame.image.load("assets/items/bottle.png"), [70, 70])
  sprite3 = pygame.transform.scale(pygame.image.load("assets/items/paper.png"), [70, 70])

  sprite4 = pygame.transform.scale(pygame.image.load("assets/items/bulb.png"), [70, 70])
  sprite5 = pygame.transform.scale(pygame.image.load("assets/items/tire.png"), [60, 60])
  sprite6 = pygame.transform.scale(pygame.image.load("assets/items/bag.png"), [70, 70])

  # game loop
  while running:
    screen.blit(bg, (0, 0))

    # tuple with mouse coords, mouse[0] for x and mouse[1] for y
    mouse = pygame.mouse.get_pos()

    # go back button
    if 20 <= mouse[0] <= 120 and 20 <= mouse[1] <= 60: 
      screen.blit(back_light,[20,20])     
    else: 
      screen.blit(back_dark,[20,20]) 
    
    pygame.draw.rect(screen, DARK_GREY, [67.5, 210, 150, 200])
    pygame.draw.rect(screen, (75, 100, 200), [362.5, 210, 150, 200])
    screen.blit(recycle, (437.5-recycleSize/2, 220))
    screen.blit(trash, (142.5-trashSize/2, 220))

    pygame.draw.rect(screen, (150,150,150), [100, 85, 365, 100])
    screen.blit(h2p, [170,95])
    screen.blit(h2p2, [145,115])
    screen.blit(h2p3, [140,135])
    screen.blit(h2p4, [210,155])
    
    screen.blit(sprite1, [375,250])
    screen.blit(sprite2, [440,270])
    screen.blit(sprite3, [380,330])

    screen.blit(sprite4, [75,240])
    screen.blit(sprite5, [140,280])
    screen.blit(sprite6, [75,325])

    # event listener
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          running = False
      elif event.type == pygame.MOUSEBUTTONDOWN: 
        if 0 <= mouse[0] <= 120 and 20 <= mouse[1] <= 60: 
          running = False
      elif event.type == pygame.QUIT:
        running = False

    pygame.display.update() # refreshes screen