# setup stuff 
import pygame, sys, random
from pygame.locals import *
from py.trash import Trash as Tr
from py.recycling import Recycling as Rc
from py.game_over import game_over

def game():
  pygame.init()

  # colors
  WHITE = (255, 255, 255)
  LIGHT_GREY = (175, 175, 175)
  DARK_GREY = (100, 100, 100)
  
  # variables and constants before the game starts
  running = True
  SCREEN_DIMENSIONS = [580, 450]
  screen = pygame.display.set_mode(SCREEN_DIMENSIONS)

  bg = pygame.image.load("assets/other/backdrop.png")
  bg = pygame.transform.scale(bg, SCREEN_DIMENSIONS)
  recycle_bin = pygame.image.load("assets/other/recycling_bin.png")
  recycle_bin = pygame.transform.scale(recycle_bin, [125, 187.5])
  trash_can = pygame.image.load("assets/other/trash_bin.png")
  trash_can = pygame.transform.scale(trash_can, [125, 187.5])
  back_light = pygame.image.load("assets/buttons/back_light.png")
  back_light = pygame.transform.scale(back_light,[140,40])
  back_dark = pygame.image.load("assets/buttons/back_dark.png")
  back_dark = pygame.transform.scale(back_dark,[140,40])

  height = screen.get_height()
  width = screen.get_width()
  pygame.display.set_caption("Recycle It!")
  icon = pygame.image.load("assets/other/icon.png")
  pygame.display.set_icon(icon)
  clock = pygame.time.Clock() # for fps 
  tick = 0
  font = pygame.font.SysFont("Corbel", 35)
  lives = 3
  score = 0
  all_trash = pygame.sprite.Group() # list of trash instances
  all_recycle = pygame.sprite.Group() # list of recycle instances

  pygame.time.set_timer(USEREVENT+2, random.randrange(1500, 3000))

  # game loop
  while running:
    tick += 1
    if tick % 10 == 0:
      score += 1
    scoreText = font.render(("Score: " + str(score)), True, WHITE)
    livesText = font.render(("Lives: " + str(lives)), True, WHITE)

    screen.blit(bg, (0, 0))
    
    screen.blit(trash_can, (50, 250))
    screen.blit(recycle_bin, (405, 250))
    
    # tuple with mouse coords, mouse[0] for x and mouse[1] for y
    mouse = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed(3)

    all_trash.update() # make recycle and trash sprites update
    all_trash.draw(screen) 
    all_recycle.update()
    all_recycle.draw(screen)

    # update for next moves - all trash and recycables
    for item in all_trash: item.gravity(item.rect.y)
    for item in all_trash: item.follow(mouse[0], mouse[1])
    for item in all_trash: lives += item.missed(item.rect.x, item.rect.y)
    for item in all_trash: item.binned(item.rect.x, item.rect.y)
    for item in all_recycle: item.gravity(item.rect.y)
    for item in all_recycle: item.follow(mouse[0], mouse[1])
    for item in all_recycle: lives += item.missed(item.rect.x, item.rect.y)
    for item in all_recycle: item.binned(item.rect.x, item.rect.y)

    if mouse_pressed[0]:
      for item in all_trash:
        if item.rect.x - 10 <= mouse[0] <= item.rect.x + 40 and item.rect.y - 10 <=  mouse[1] <= item.rect.y + 40:
          item.followMouse = True 
      for item in all_recycle:
        if item.rect.x - 10 <= mouse[0] <= item.rect.x + 40 and item.rect.y - 10 <=  mouse[1] <= item.rect.y + 40:
          item.followMouse = True 

    # go back button
    if 20 <= mouse[0] <= 120 and 20 <= mouse[1] <= 60: 
      screen.blit(back_light,[20,20])     
    else: 
      screen.blit(back_dark,[20,20]) 

    # score/lives
    pygame.draw.rect(screen, DARK_GREY, [width - 180, 20, 160, 85])
    screen.blit(scoreText, (410, 30))
    screen.blit(livesText, (410, 70))

    # event listener
    for event in pygame.event.get():
      if event.type == USEREVENT+2:
        r = random.randrange(0,2)
        if r == 0:
          all_trash.add(Tr(random.randint(175, 375), 0, 580, 450, random.randint(1,3)))
        elif r == 1:
          all_recycle.add(Rc(random.randint(175, 375), 0, 580, 450, random.randint(1,3)))
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          running = False
        elif event.key == K_SPACE:
          for item in all_trash:
            if item.rect.x - 10 <= mouse[0] <= item.rect.x + 60 and item.rect.y - 10 <=  mouse[1] <= item.rect.y + 60:
              item.followMouse = True 
          for item in all_recycle:
            if item.rect.x - 10 <= mouse[0] <= item.rect.x + 60 and item.rect.y - 10 <=  mouse[1] <= item.rect.y + 60:
              item.followMouse = True 
      elif event.type == pygame.MOUSEBUTTONDOWN: 
        if 0 <= mouse[0] <= 120 and 20 <= mouse[1] <= 60: 
          running = False
      elif event.type == pygame.QUIT:
        running = False
    
    if lives <= 0:
      running = False
      game_over(scoreText)

    pygame.display.update() # refreshes screen
    clock.tick(30) # fps