import pygame
import os
import time
import random

pygame.font.init()

WIDTH = 1000
HEIGHT = 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# load images
BLACK_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_black_ship.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_blue_ship.png"))
PURPLE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_purple_ship.png"))
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_red_ship.png"))


# player ship
WHITE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_white_ship.png"))

# lasers
BLACK_LASER = pygame.image.load(os.path.join("assets", "pixel_black_laser.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_blue_laser.png"))
PURPLE_LASER = pygame.image.load(os.path.join("assets", "pixel_purple_laser.png"))
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_red_laser.png"))
WHITE_LASER = pygame.image.load(os.path.join("assets", "pixel_white_laser.png"))


# background
BG = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT)
)

class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.laser = []
        self.cool_down_counter = 0 

    def draw(self,WIN):
        WIN.blit(self.ship_img, (self.x, self.y,))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()    


class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.ship_img = WHITE_SPACE_SHIP
        self.laser_img = WHITE_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health



def main():
    run = True
    FPS = 40
    level = 1
    lives = 5
    clock = pygame.time.Clock()
    player = Player(10, 30)
    player_vel = 6
    main_font = pygame.font.SysFont("comicsans", 30)

    def redraw_window():
        WIN.blit(BG, (0,1))
        lives_label = main_font.render(f"lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        player.draw(WIN)

        pygame.display.update()

    redraw_window()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.x - player_vel > 0: #left
              player.x -= player_vel
        if key[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:#right
            player.x += player_vel    
        if key[pygame.K_w] and player.x - player_vel > 0:#up
            player.y -= player_vel
        if key[pygame.K_s] and player.x + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel

main()
