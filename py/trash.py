# file for the trash pieces
import pygame

sprite1 = pygame.transform.scale(pygame.image.load("assets/items/bulb.png"), [50, 50])
sprite2 = pygame.transform.scale(pygame.image.load("assets/items/tire.png"), [50, 50])
sprite3 = pygame.transform.scale(pygame.image.load("assets/items/bag.png"), [50, 50])

sprites = [sprite1, sprite2, sprite3]

class Trash(pygame.sprite.Sprite):
  instancelist = [] # i need this later to run functions on every piece

  def __init__(self, x, y, width, height, sprite):
    super().__init__()

    self.image = pygame.Surface([width, height])
    self.image = sprites[sprite - 1]
    self.rect = self.image.get_rect()
    self.x, self.rect.x = x, x
    self.y, self.rect.y = y, y
    self.followMouse = False

    Trash.instancelist.append(self)

  def gravity(self, y): 
    self.rect.y += 2
  
  def binned(self, x, y):
    if x >= 0 and x <= 160 and y >= 250:
      self.kill()

  def missed(self, x, y):
    if y >= 400 or (x >= 380 and x <= 570 and y >= 250):
      self.kill()
      return -1
    else:
      return 0

  def follow(self, x, y):
    if self.followMouse:
      self.rect.x = x - 25
      self.rect.y = y - 25