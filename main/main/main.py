""" PROJECT 2 : TEAM 1"""
#Imports
import pygame
import math

#golbal image files
background_startscherm = pygame.image.load('boten achtergrond.jpg')

black=(0,0,0)
white=(255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)

#quit functie
def quitgame():
    pygame.quit()
    quit ()

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

def button (screen,msg,x,y,w,h,ic,ac, action = None):
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

#Main Program Logic
def play_screen():
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
        
        #Flip the screen
        pygame.display.flip()

def instructions_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.blit(background_startscherm,[0,0])
        
        #TESTBUTTON
        button (screen,"Back",640-150,576-50,300,100,red,bright_red, program)

        #Flip the screen
        pygame.display.flip()

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
        screen.blit(background_startscherm,[0,0])

        #button
        button (screen,"Start!",640-150,160-50,300,100,green,bright_green, play_screen)
        button (screen,"Instructions",640-150,360-50,300,100,blue,bright_blue, instructions_screen)
        button (screen,"Quit",640-150,576-50,300,100,red,bright_red, quitgame)

        #Flip the screen
        pygame.display.flip()

# Start the program
program()