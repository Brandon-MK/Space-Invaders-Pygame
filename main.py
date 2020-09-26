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

    player(playerX,playery)
    pygame.display.update()