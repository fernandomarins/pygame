
# coding: utf-8

# In[ ]:

import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))

def checkCollision(x, y, treasureX, treasureY):
    global textWin, screen
    collisionState = False
    if y >= treasureY and y <= treasureY + 40:
        if x >= treasureX and x <= treasureX + 35:
            y = 650
            x = 450 - 35/2
            collisionState = True
        elif x + 40 >= treasureX and x + 35 <= treasureX + 35:
            y = 650
            x = 450 - 35/2
            collisionState = True
    elif y + 40 >= treasureY and y + 40 <= treasureY + 40:
        if x + 40 >= treasureX and x + 40 <= treasureX + 35:
            y = 650
            x = 450 - 35/2
            collisionState = True
        elif x + 40 >= treasureX and x + 35 <= treasureX + 35:
            y = 650
            x = 450 - 35/2   
            collisionState = True
    
    return (x, y, collisionState)

# if the game is finished or not
finished = False
# x and y coordenates
x = 450 - 35/2
y = 650

# adding image
playerImage = pygame.image.load('player.png')
playerImage = pygame.transform.scale(playerImage, (35, 40))
# make sure image is transparent so the background is displayed
playerImage = playerImage.convert_alpha()

# background
backgroundImage = pygame.image.load('background.png')
backgroundImage = pygame.transform.scale(backgroundImage, (900, 700))
screen.blit(backgroundImage, (0, 0))

# teasure
treasureImage = pygame.image.load('treasure.png')
treasureImage = pygame.transform.scale(treasureImage, (35, 40))
treasureImage = treasureImage.convert_alpha()
treasureX, treasureY = 450 - 35/2, 50
screen.blit(treasureImage, (treasureX, treasureY))

collisionTreasure = False

#enemy
enemyImage = pygame.image.load('enemy.png')
enemyImage = pygame.transform.scale(enemyImage, (35, 40))
enenyImage = enemyImage.convert_alpha()
enemyX = 100
enemyY = 580-10
movingRight = True
collisionEenemy = False

enemies = [(enemyX, enemyY, movingRight)]
enemyNames = {0: "Max", 1: "Jill", 2: "Greg", 3: "Diane"}

#adding font
font = pygame.font.SysFont("comicsans", 60)

# level
level = 1

# the frame
frame = pygame.time.Clock()

while finished == False:
    for event in pygame.event.get():
        # to detect if the game should end
        if event.type == pygame.QUIT:
            finised = True
    
    enemyIndex = 0
    # check if enemy is next to the screen border
    for enemyX, enemyY, movingRight in enemies:
        if enemyX >= 800 - 35:
            movingRight = False
        elif enemyX <= 100:
            movingRight = True
            
        if movingRight == True:
            enemyX += 5 * level
        else:
            enemyX -= 5 * level
    
        enemies[enemyIndex] = (enemyX, enemyY, movingRight)
        enemyIndex += 1
    # array containing all the keys pressed by the user
    pressedKeys = pygame.key.get_pressed()
    # K_SPACE means the space key
    if pressedKeys[pygame.K_RIGHT] == 1:
        # if the space key is pressed, add 5 to x (move the object)
        x += 5
    
    if pressedKeys[pygame.K_DOWN] == 1:
        # if the space key is pressed, add 5 to x (move the object)
        y += 5
        
    if pressedKeys[pygame.K_LEFT] == 1:
        # if the space key is pressed, add 5 to x (move the object)
        x -= 5
        
    if pressedKeys[pygame.K_UP] == 1:
        # if the space key is pressed, add 5 to x (move the object)
        y -= 5
        
    #if pressedKeys[pygame.K_q] == 1:
       # pygame.event.post(pygame.QUIT())

    white = (255, 255, 255)
    screen.blit(backgroundImage, (0, 0))
    screen.blit(treasureImage, (treasureX, treasureY))
    
    enemyIndex = 0
    for enemyX, enemyY, movingRight in enemies:
        screen.blit(enemyImage, (enemyX, enemyY))
        x, y, collisionEnemy = checkCollision(x, y, enemyX, enemyY)
        if collisionEnemy == True:
            name = enemyNames[enemyIndex]
            textLose = font.render("You were killed by " + name, True, (255, 0, 0))
            screen.blit(textLose, (450 - textLose.get_width()/2, 350 - textLose.get_height()/2))
            pygame.display.flip()
            frame.tick(1)
        frame.tick(30)
        enemyIndex += 1            

    screen.blit(playerImage, (x, y))
    
    x, y, collisionTreasure = checkCollision(x, y, treasureX, treasureY)
    
    
    if collisionTreasure == True:
        level += 1
        textWin = font.render("You've reached level " + str(level), True, (0, 0, 0))
        enemies.append((enemyX - 50 * level, enemyY - 50 * level, False))
        screen.blit(textWin, (450 - textWin.get_width()/2, 350 - textWin.get_height()/2))
        pygame.display.flip()
        frame.tick(1)
    
    pygame.display.flip()
    frame.tick(30)


# In[ ]:



