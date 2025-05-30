import pygame
import random


SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72


pygame.init()


background_image = pygame.transforms.scale(pygame.image.load("download.jpeg"), 
                                           (SCREEN_WIDTH, SCREEN_HEIGHT))


font = pygame.font.SysFont('Times New Roman', FONT_SIZE)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
      super().__init__()
      self.image = pygame.Surface([width, height])
      self.image.fill(
      pygame.Color("dogerblue"))
      self.rect = self.image.get_rect()


    def move(self, x_change, y_change):
        self.rect.x = max(
       min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(
         min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Level Up Game")
all_sprites = pygame.sprite.Group()


sprite1 = Sprite(pygame.Color("black"), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, SCREEN_WIDTH - sprite1.rect.width), random.randint(
0, SCREEN_HEIGHT - sprite1.rect.width), random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)


sprite2 = Sprite(pygame.Color("red"), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(
0, SCREEN_WIDTH - sprite2.rect.width), random.randint(
0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)


running, won = True, False
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    x_change, y_change = 0, 0
    if keys[pygame.K_LEFT]:
        x_change = -MOVEMENT_SPEED
    if keys[pygame.K_RIGHT]:
        x_change = MOVEMENT_SPEED
    if keys[pygame.K_UP]:
        y_change = -MOVEMENT_SPEED
    if keys[pygame.K_DOWN]:
        y_change = MOVEMENT_SPEED

    sprite1.move(x_change, y_change)

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if pygame.sprite.collide_rect(sprite1, sprite2):
        won = True

    if won:
        win_text = font.render("You Win!", True, pygame.Color("green"))
        screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2,
                               SCREEN_HEIGHT // 2 - win_text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
# End of the game loop