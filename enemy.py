import pygame
import random

class Enemy:

  def __init__(self):
    self.enemy_img = pygame.image.load("images/alien.png")
    self.enemy_x = random.randint(10, 790)
    self.enemy_y = 90
    self.enemy_x_change = 0.5
    self.enemy_y_change = 32

  def draw_enemy(self, screen):
    screen.blit(self.enemy_img, (self.enemy_x, self.enemy_y))

  def set_position(self):
    self.enemy_x = random.randint(10, 790)
    self.enemy_y = random.randint(20, 400)

  def move(self):
    self.enemy_x += self.enemy_x_change
    if self.enemy_x <= 0:
      self.enemy_y = self.enemy_y + self.enemy_y_change
      self.enemy_x_change = 0.5
    elif self.enemy_x >= 768:
      self.enemy_y = self.enemy_y + self.enemy_y_change
      self.enemy_x_change = -0.5

    if self.enemy_y >= 568:
      self.enemy_y_change = -32
      if self.enemy_x <= 0:
        self.enemy_x_change = 0.5
      elif self.enemy_x >= 768:
        self.enemy_x_change = -0.5
