import pygame

#Inialize the game
pygame.init()

#Create the screen(width,height)
screen = pygame.display.set_mode((800,600))

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
enemyX = 370
enemyy = 480
enemyX_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

#Game Loop
running = True
while running:
    #Setting the color of the screen
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Movement with arrows
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX,playery)
    pygame.display.update()