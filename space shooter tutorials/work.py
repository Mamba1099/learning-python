import pygame
import os
import time
import random

pygame.font.init()

WIDTH = 1500
HEIGHT = 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# load images
BLACK_SPACE_SHIP = pygame.image.load(os.path.join("pygame/assets", "black_ship.png"))
WHIT_SPACE_SHIP = pygame.image.load(os.path.join("pygame/assets", "white_ship.png"))
PURPLE_SPACE_SHIP = pygame.image.load(os.path.join("pygame/assets", "purple_ship.png"))
RED_SPACE_SHIP = pygame.image.load(os.path.join("pygame/assets", "red_ship.png"))


# player ship
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("pygame/assets", "blue_ship.png"))

# lasers
BLACK_LASER = pygame.image.load(os.path.join("pygame/assets", "black_laser.png"))
BLUE_LASER = pygame.image.load(os.path.join("pygame/assets", "blue_laser.png"))
PURPLE_LASER = pygame.image.load(os.path.join("pygame/assets", "purple_laser.png"))
RED_LASER = pygame.image.load(os.path.join("pygame/assets", "red_laser.png"))
WHITE_LASER = pygame.image.load(os.path.join("pygame/assets", "white_laser.png"))


# background
BG = pygame.transform.scale(
    pygame.image.load(os.path.join("pygame/assets", "background.png")), (WIDTH, HEIGHT)
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
        self.ship_img = BLUE_SPACE_SHIP
        self.laser_img = BLUE_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
 COLOR_MAP = {
             "red":(RED_SPACE_SHIP, RED_LASER),
             "black": (BLACK_SPACE_SHIP, BLACK_LASER),
             "blue": (WHIT_SPACE_SHIP, WHITE_LASER),
             "purple": (PURPLE_SPACE_SHIP, PURPLE_LASER)
 }


 def __init__(self, x, y, color, health = 100): 
     super().__init__( x, y, health)
     self.ship_img, self.laser_img = self.COLOR_MAP[color]
     self.mask = pygame.mask.from_surface(self.ship_img)

 def move(self, vel):
    self.y += vel


 

def main():
    run = True
    FPS = 40
    level = 1
    lives = 5
    clock = pygame.time.Clock()
    player = Player(5, 25)
    player_vel = (5)
    enemies = []
    wave_length = 5
    enemy_vel = 1
    lost = False
    main_font = pygame.font.SysFont("comicsans", 10)
    lost_font = pygame.font.SysFont("comicsans", 50)

    def redraw_window():
        WIN.blit(BG, (0,0))
        lives_label = main_font.render(f"lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)
        
        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))


        pygame.display.update()

    redraw_window()

    while run:
        clock.tick(FPS)

        if lives <= 0:
            lost = True


        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["black", "blue", "purple", "red"]))
                enemies.append(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.x - player_vel > 0: #left
              player.x -= player_vel
        if key[pygame.K_d] and player.y + player_vel + player.get_width() < WIDTH:#right
            player.x += player_vel    
        if key[pygame.K_w] and player.x - player_vel > 0:#up
            player.y -= player_vel
        if key[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel

        for enemy in enemies[:]:
         enemy.move(enemy_vel)
         if enemy.y + enemy.get_height() > HEIGHT:
            lives -= 1
            enemies.remove(enemy)

        redraw_window()



main()
