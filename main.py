import pygame
import random

#Inialize the game
pygame.init()

#Create the screen(width,height)
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load("background.png")

#Title and Icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("player.png")
playerX = 370
playery = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0,800)
enemyy = random.randint(50,150)
enemyY_change = 40
enemyX_change = 4

#Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bullety = 480
bulletX_change = 0
bullety_change = 10
bullet_state = "ready"

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletImg,(x+16,y+10))

#Game Loop
running = True
while running:
    #Setting the color of the screen
    screen.fill((0, 0, 0))
    #Background Image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Movement with arrows
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        if event.key == pygame.K_SPACE:
            fire_bullet(playerX,bullety)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    #Checking for boundaries of spaceship
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 4
        enemyy += enemyY_change
    elif enemyX >= 736:
        enemyy += enemyY_change
        enemyX_change = -4

    #Bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX,bullety)
        bullety -= bullety_change

    enemy(enemyX,enemyy)
    player(playerX,playery)
    pygame.display.update()