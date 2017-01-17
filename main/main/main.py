""" PROJECT 2 : TEAM 1"""
#Imports
import pygame
import math

white=(255,255,255)

# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    return False

class Button:
    def __init__(self,x,y,z,q):
        self.x=x
        self.y=y
        self.z=z
        self.q=q
    def draw(self,screen):
        pygame.draw.rect(screen,white,((int(self.x-(int(self.z)/2))),(int(self.y-(int(self.q)/2))),int(self.z),int(self.q)))

#Main Program Logic
def program():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    #Button aanmaken
    button1 = Button((width * 0.5),(height * 0.5),300,100)
    button2 = Button((width * 0.5),(height * 0.7),300,100)

    while not process_events():
        # Clear Screen
        screen.fill((0,0,0))

        #button
        button1.draw(screen)
        button2.draw(screen)

        #Flip the screen
        pygame.display.flip()

# Start the program
program()