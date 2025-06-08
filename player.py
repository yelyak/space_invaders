import pygame
import random


class Player:

    def set_position_player(self):
        self.player_x = random.randint(10, 790)
        self.player_y = random.randint(20, 580)

    def __init__(self):
        self.player_img = pygame.image.load("images/ufo.png")
        self.player_x = random.randint(10, 790)
        self.player_y = 450
        self.player_x_change = 0
        self.player_y_change = 0

        self.bullet_img = pygame.image.load("images/bullet.png")
        self.bullet_x = 0
        self.bullet_y = 480
        self.bullet_ready = True
        self.bullet_y_change = 5

    def fire_bullet(self):
        self.bullet_ready = False

    def draw_player(self, screen):
        screen.blit(self.player_img, (self.player_x, self.player_y))

    def actions(self, event, screen):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player_x_change = -1
            elif event.key == pygame.K_RIGHT:
                self.player_x_change = 1
            elif event.key == pygame.K_UP:
                self.player_y_change = -1
            elif event.key == pygame.K_DOWN:
                self.player_y_change = 1
            elif event.key == pygame.K_SPACE:

                if self.bullet_ready:

                    self.fire_bullet()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.player_x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player_y_change = 0
        if self.player_x <= 0:
            self.player_x = 0
        elif self.player_x >= 768:
            self.player_x = 768
        if self.player_y <= 0:
            self.player_y = 0
        elif self.player_y >= 568:
            self.player_y = 568
        self.player_x = self.player_x + self.player_x_change
        self.player_y = self.player_y + self.player_y_change

        if not self.bullet_ready:
            self.bullet_x = self.player_x
            screen.blit(self.bullet_img, (self.bullet_x, self.bullet_y))
            self.bullet_y -= self.bullet_y_change

        if self.bullet_y <= 0:
            self.bullet_y = self.player_y
            self.bullet_x = self.player_x
            self.bullet_ready = True