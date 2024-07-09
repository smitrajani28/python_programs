import random
import sys
import pygame
from pygame.locals import *

# Global variables
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'Pygames/gallery/assets/bluebird-upflap.png'
BACKGROUND = 'Pygames/gallery/assets/background-day.png'
PIPE = 'Pygames/gallery/assets/pipe-green.png'

def welcomeScreen():
    playerX = int(SCREENWIDTH/5)
    playerY = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messageX = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messageY = int(SCREENHEIGHT * 0.13)
    baseX = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerX,playerY))
                SCREEN.blit(GAME_SPRITES['base'],(baseX,GROUNDY))
                SCREEN.blit(GAME_SPRITES['message'],(messageX,messageY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerX = int(SCREENWIDTH/5)
    playerY = int(SCREENHEIGHT/2)
    baseX = 0

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    upperPipes = [ 
        {'x' : SCREENWIDTH+200 , 'y' : newPipe1[0]['y']},
        {'x' : SCREENWIDTH+200+(SCREENWIDTH/2) , 'y' : newPipe2[0]['y']}
    ]
    lowerPipes = [ 
        {'x' : SCREENWIDTH+200 , 'y' : newPipe1[1]['y']},
        {'x' : SCREENWIDTH+200+(SCREENWIDTH/2) , 'y' : newPipe2[1]['y']}
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1 

    playerFlapAccv = -8
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playerY > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()
        
        crashTest = iscollide(playerX,playerY,upperPipes,lowerPipes)
        if crashTest:
            return

        playerMidPos = playerX + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipMidPos <= playerMidPos < pipMidPos + 4 :
                score +=1
                print(f"your score is {score}")
                GAME_SOUNDS['point'].play()
        
        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITES['player'].get_height()
        playerY =playerY + min(playerVelY, GROUNDY - playerY - playerHeight )
    
    for upperPipe,lowerPipe in zip(upperPipes,lowerPipes):
        upperPipe['x'] += pipeVelX
        lowerPipe['x'] += pipeVelX

    if 0 < upperPipes[0]['x'] < 5 :
        newpipe = getRandomPipe()
        upperPipes.append(newpipe[0])
        lowerPipes.append(newpipe[1])

    if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
        upperPipes.pop(0)
        lowerPipes.pop(0)

    SCREEN.blit(GAME_SPRITES['background'],(0, 0))
    for upperPipe,lowerPipe in zip(upperPipes,lowerPipes):
        SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe['x'], upperPipe['y']))
        SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerPipe['x'], lowerPipe['y']))
        
    SCREEN.blit(GAME_SPRITES['base'],(baseX, GROUNDY))
    SCREEN.blit(GAME_SPRITES['player'],(playerX, playerY))

    myDigits = [int(x) for x in list(str(score))]
    width = 0

    for digit in myDigits:
        width += GAME_SPRITES['numbers'][digit].get_width()
    
    xOffset = (SCREENWIDTH - width)/2

    for digit in myDigits:
        SCREEN.blit(GAME_SPRITES['numbers'][digit], (xOffset, SCREENHEIGHT * 0.12))
        xOffset += GAME_SPRITES['numbers'][digit].get_width()
    
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def iscollide(playerX,playerY,upperPipes,lowerPipes):
    if playerY > GROUNDY - 25 or playerY < 0:
        GAME_SOUNDS['hit'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if (playerY < pipeHeight + pipe['y'] and  abs(playerX - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
    for pipe in lowerPipes:
        if (playerY + GAME_SPRITES['player'].get_height() > pipe['y'] and  abs(playerX - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
    return False






def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2= offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2*offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x' : pipeX, 'y' : -y1},
        {'x' : pipeX, 'y' : y2}
    ]
    return pipe


if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy bird game")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('Pygames/gallery/number/0.png').convert_alpha(),
        pygame.image.load('Pygames/gallery/number/1.png').convert_alpha(),
        pygame.image.load('Pygames/gallery/number/2.png').convert_alpha(),
        pygame.image.load('Pygames/gallery/number/3.png').convert_alpha(),
        pygame.image.load('Pygames/gallery/number/4.png').convert_alpha(),
        pygame.image.load('Pygames/gallery/number/5.png').convert_alpha(),
        pygame.image.load('Pygames/gallery/number/6.png').convert_alpha(),
        pygame.image.load('Pygames/gallery/number/7.png').convert_alpha(),
        pygame.image.load('Pygames/gallery/number/8.png').convert_alpha(),
        pygame.image.load('Pygames/gallery/number/9.png').convert_alpha()
    )

    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['message'] = pygame.image.load('Pygames/gallery/assets/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('Pygames/gallery/assets/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )
        
    GAME_SOUNDS['die'] = pygame.mixer.Sound('Pygames/gallery/sound/sfx_die.wav') 
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('Pygames/gallery/sound/sfx_hit.wav') 
    GAME_SOUNDS['point'] = pygame.mixer.Sound('Pygames/gallery/sound/sfx_point.wav') 
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('Pygames/gallery/sound/sfx_swooshing.wav') 
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('Pygames/gallery/sound/sfx_wing.wav') 

    while True:
        welcomeScreen()
        mainGame()