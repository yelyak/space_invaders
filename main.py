import asyncio
import pygame
from player import Player
from enemy import Enemy

pygame.init()



screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

async def main():

  player = Player()
  enemy = Enemy()
  running = True

  score = 0
  font = pygame.font.Font("freesansbold.ttf", 30)
  text_x = 10
  text_y = 10

  lives = 3
  font = pygame.font.Font("freesansbold.ttf", 30)
  lives_text_x = 670
  lives_text_y = 10

  def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))

  def show_lives(x, y):
    lives_text = font.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(lives_text, (x, y))

  def check_bullet_collision(bullet_x, bullet_y, enemy_x, enemy_y):
    if enemy_x - 32 <= bullet_x <= enemy_x + 32 and bullet_y <= enemy_y + 32:
        return True
    else:
        return False


  def check_enemy_player_coll(player_x, player_y, enemy_x, enemy_y):
    if enemy_x - 32 <= player_x <= enemy_x + 32 and enemy_y - 32 <= player_y <= enemy_y + 32:
        return True
    else:
        return False

  while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      else:
        player.actions(event, screen)
    player.actions(event, screen)
    player.draw_player(screen)
    enemy.draw_enemy(screen)
    show_score(text_x, text_y)
    show_lives(lives_text_x, lives_text_y)
    pygame.display.update()

    enemy.move()

    if check_bullet_collision(player.bullet_x, player.bullet_y, enemy.enemy_x, enemy.enemy_y):
      score = score + 1
      enemy.set_position()

    if check_enemy_player_coll(player.player_x, player.player_y, enemy.enemy_x, enemy.enemy_y):
      lives = lives - 1
      print("You lost a life!")
      player.set_position_player()

    if lives == 0:
      print("Your ufo crashed!")
      print("You lost.")
      lame = open("images/lame.txt", "r")
      print(lame.read())
      lame.close()
      exit()

    if score == 15:
      print("Congrats, you have beat the aliens.")
      print("Here's your trophy.")
      trophy = open("images/trophy.txt", "r")
      print(trophy.read())
      trophy.close()
      exit()

    clock.tick(180)
    await asyncio.sleep(0)

asyncio.run(main())


