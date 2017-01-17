""" PROJECT 2 : TEAM 1"""
#IMPORT
import pygame
import math

# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    return False



#Main Program Logic
def program():
    width = 640
    height = 480
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

# Start the program
program()