# setup stuff
import pygame, sys, random
from pygame.locals import *

def credits():
  pygame.init()

  # colors
  SKY_BLUE = (34, 207, 230)
  WHITE = (255, 255, 255)
  LIGHT_GREY = (175, 175, 175)
  DARK_GREY = (100, 100, 100)
  PINK = (222, 62, 181)
  
  # variables and constants before the game starts
  running = True
  SCREEN_DIMENSIONS = [580, 450]
  screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
  height = screen.get_height()
  width = screen.get_width()
  pygame.display.set_caption("Recycle It!")
  icon = pygame.image.load("assets/other/icon.png")
  back_light = pygame.image.load("assets/buttons/back_light.png")
  back_light = pygame.transform.scale(back_light,[140,40])
  back_dark = pygame.image.load("assets/buttons/back_dark.png")
  back_dark = pygame.transform.scale(back_dark,[140,40])
  pygame.display.set_icon(icon)
  font = pygame.font.SysFont("Corbel", 35)
  bigFont = pygame.font.SysFont("Corbel", 30)
  quitButton = font.render("Menu", True, WHITE)
  codeBy = bigFont.render("Code By:", True, WHITE)
  codeSize = codeBy.get_width()
  jack = bigFont.render("Jack G.", True, WHITE)
  jackSize = jack.get_width()
  logan = bigFont.render("Logan V.", True, WHITE)
  loganSize = logan.get_width()
  alex = bigFont.render("Alvin S.", True, WHITE)
  alexSize = alex.get_width()
  artBy = bigFont.render("Art By:", True, SKY_BLUE)
  artSize = artBy.get_width()
  aditi = bigFont.render("Aditi K.", True, SKY_BLUE)
  aditiSize = aditi.get_width()
  musicBy = bigFont.render("Music By:", True, PINK)
  musicSize = musicBy.get_width()
  logan2 = bigFont.render("Logan V.", True, PINK)

  bg = pygame.image.load("assets/other/backdrop.png")
  bg = pygame.transform.scale(bg, SCREEN_DIMENSIONS)

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
    
    pygame.draw.rect(screen, DARK_GREY, [140, 100, 300, 300])
    screen.blit(codeBy, (width/2-codeSize/2, 135))
    screen.blit(jack, (width/2-jackSize/2, 160))
    screen.blit(logan, (width/2-loganSize/2, 182))
    screen.blit(alex, (width/2-alexSize/2, 206))
    screen.blit(artBy, (width/2-artSize/2, 246))
    screen.blit(aditi, (width/2-aditiSize/2, 271))
    screen.blit(musicBy, (width/2-musicSize/2, 311))
    screen.blit(logan2, (width/2-loganSize/2, 336))
    
    # event listener
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          running = False
      elif event.type == pygame.MOUSEBUTTONDOWN: 
        if 20 <= mouse[0] <= 120 and 20 <= mouse[1] <= 60: 
          running = False
      elif event.type == pygame.QUIT:
        running = False

    pygame.display.update() # refreshes screen