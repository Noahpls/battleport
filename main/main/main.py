""" PROJECT 2 : TEAM 1"""
#Imports
import pygame
import math

black=(0,0,0)
white=(255,255,255)
green = (0,200,0)
red = (200,0,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    return False

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button (screen,msg,x,y,w,h,ic,ac):
    mouse =pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

#Main Program Logic
def program():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.fill((0,0,0))

        #button
        button (screen,"Start!",640-150,360-50,300,100,green,bright_green)

        #Flip the screen
        pygame.display.flip()

# Start the program
program()