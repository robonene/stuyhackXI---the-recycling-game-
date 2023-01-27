# setup stuff
import pygame
from pygame.locals import *

def game_over(scoreText):
  pygame.init()
  
  # colors
  WHITE = (255, 255, 255)
  DARK_RED = (199, 30, 18)
  
  # variables and constants before the game starts
  running = True
  SCREEN_DIMENSIONS = [580, 450]
  screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
  width = screen.get_width()
  pygame.display.set_caption("Recycle It!")
  icon = pygame.image.load("assets/other/icon.png")
  pygame.display.set_icon(icon)
  bigFont = pygame.font.SysFont("Corbel", 30)
  gameOver = bigFont.render("GAME OVER", True, WHITE)
  bg = pygame.image.load("assets/other/backdrop.png")
  bg = pygame.transform.scale(bg, SCREEN_DIMENSIONS)
  
  tick = 0
  # game loop
  while running:
    screen.blit(bg, [0, 0])

    pygame.draw.rect(screen, DARK_RED, (100, 100, 380, 100))
    screen.blit(gameOver, [width/2 - gameOver.get_width()/2, 125])
    screen.blit(scoreText, [width/2 - scoreText.get_width()/2, 150])

    tick += 1
    if tick >= 100:
      running = False

    pygame.display.update() # refreshes screen