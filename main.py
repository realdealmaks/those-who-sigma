import math, random, pygame, PIL, pydub, pytweening, scipy, dearpygui

# Image loading
player_image = pygame.image.load('player.png')
pygame.convert_alpha(player_image)
player_image = pygame.transform.scale(player_image, (50, 50))
enemy_image = pygame.image.load('enemy.png')
pygame.convert_alpha(enemy_image)
enemy_image = pygame.transform.scale(enemy_image, (50, 50))

# Classes and definitions
class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.health = 100
        self.damage = 10
        self.sprite = pygame.image.load('player.png')
    
    def move(self, direction):
        if direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed
        elif direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed

    def attack(self, enemy):
        enemy.health -= self.damage

        if enemy.health <= 0:
            enemy.die()

    def die(self):
        pass

class enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.health = 50
        self.damage = 5
        self.sprite = pygame.image.load('enemy.png')
    
    def move(self):
        self.x += self.speed

    def attack(self, player):
        player.health -= self.damage

        if player.health <= 0:
            player.die()

    def die(self):
        pass

# Game setup
player = player(0, 0)
enemy = enemy(100, 0)
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game')

# Main loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN: # Key registration
            if event.key == pygame.K_w:
                player.move('up')
            elif event.key == pygame.K_s:
                player.move('down')
            elif event.key == pygame.K_a:
                player.move('left') 
            elif event.key == pygame.K_d:
                player.move('right')
            elif event.key == pygame.K_SPACE:
                player.attack(enemy)

    screen.fill((0, 0, 0)) # Redraw background
    screen.blit(player.sprite, (player.x, player.y)) # Draw player
    screen.blit(enemy.sprite, (enemy.x, enemy.y)) # Draw enemy
    clock.tick(240) # Set FPS
    pygame.display.update() # Update display

pygame.quit()