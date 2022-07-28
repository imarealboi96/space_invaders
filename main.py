import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyimg= pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.1
enemyY_change = 100
def enemy(x, y):
    screen.blit(enemyimg, (x, y))

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))



# Game Loop
running = True
while running:
    


    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    # Catch pygames QUIT event and exit the while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether it is a right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.3
            elif event.key == pygame.K_RIGHT:
                playerX_change += 0.3


        # if key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    player(playerX, playerY)

    enemyX += enemyX_change
    
    if enemyX <=150:
        enemyX_change = 0.1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.1
        enemyY += enemyY_change 
    enemy(enemyX, enemyY)
    # Update screen
    pygame.display.update()
