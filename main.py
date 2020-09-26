import pygame
import random
import math
from pygame import mixer

# Inialize the game
pygame.init()

# Create the screen(width,height)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playery = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyy = []
enemyY_change = []
enemyX_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyY_change.append(40)
    enemyX_change.append(4)

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bullety = 480
bulletX_change = 0
bullety_change = 10
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bullety):
    distance = math.sqrt((math.pow(bulletX - enemyX, 2)) + (math.pow(bullety - enemyY, 2)))
    if distance < 27:
        return True
    else:
        return False


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    game_over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (200, 250))


# Game Loop
running = True
while running:
    # Setting the color of the screen
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement with arrows

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        # Shooting of the bullet
        if event.key == pygame.K_SPACE:
            if bullet_state is "ready":
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()
                bulletX = playerX
                fire_bullet(bulletX, bullety)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # Checking for boundaries of spaceship
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemies):
        # Game over
        if enemyy[1] > 440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyy[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyy[i] += enemyY_change[i]
            enemyX_change[i] = -4

        collision = isCollision(enemyX[i], enemyy[i], bulletX, bullety)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyy[i], i)

    # Bullet movement
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bullety)
        bullety -= bullety_change

    show_score(textX, textY)
    player(playerX, playery)
    pygame.display.update()
