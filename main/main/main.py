""" PROJECT 2 : TEAM 1"""
#Imports
import pygame
import math

#global image files
#set a resolution
radar = pygame.image.load('radar.jpg')
background_startscherm = pygame.image.load('radar background.jpg')
boten = pygame.image.load('boten achtergrond.jpg')
label1=pygame.image.load('button groen 1.png')
label3=pygame.image.load('button groen 3.png')

black=(0,0,0)
white=(255,255,255)
grey = (128,128,128)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)
bright_grey=(155,155,155)

#quit functie
def quitgame():
    pygame.quit()
    quit ()

def play_sound():
    pygame.init()
    sonar_sound = pygame.mixer.Sound('Sonar_Sound.wav')
    sonar_sound.play()
    set_volume=pygame.mixer.Sound.set_volume(sonar_sound, 0.25)
    


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

def button (screen,msg,x,y,w,h,ic,ac,ilw,alw,fs,action = None, action2 = None):
    pygame.init()
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,ac,(x,y,w,h),ilw)
        if click[0] == 1 and action2 != None:
            action2()
        if click[0] == 1 and action != None:
            action()
            
            
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h),alw)

    smallText = pygame.font.Font("freesansbold.ttf",fs)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

def load_new_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)


    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])
        screen.blit(label1,[50,25])
        screen.blit(label3,[645,25])

        button (screen,"Load Game",255,175,200,75,green,bright_green,5,1,20, load_screen,play_sound)
        button (screen,"New Game",850,175,200,75,green,bright_green,5,1,20, new_screen,play_sound)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()

#Main Program Logic
#main-start-new
def new_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)


    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])

        button (screen,"Menu",1160,20,100,50,grey,bright_grey,0,0,20)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)
        
        #Flip the screen
        pygame.display.flip()
#main-start-load
def load_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)


    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])

        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, load_new_screen)
        
        #Flip the screen
        pygame.display.flip()
#main-instructions
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
        screen.blit(radar,[0,0])
        
        #TESTBUTTON
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()
#main-highscores
def highsccores_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])
        
        #TESTBUTTON
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()
#main-options
def option_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)

    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])

        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()
#main
def program():
    width = 1280
    height = 720
    size = (width, height)
    #start PyGame

    
    screen = pygame.display.set_mode(size)
    
    while not process_events():
        # Clear Screen
        screen.blit(background_startscherm,[0,0])
            

        #button
        button (screen,"Start!",350,200,200,75,green,bright_green,5,1,30, load_new_screen, play_sound)
        button (screen,"Instructions",670,580,200,75,green,bright_green,5,1,30, instructions_screen,play_sound)
        button (screen,"Highscores",930,300,200,75,green,bright_green,5,1,30, highsccores_screen,play_sound)
        button (screen,"Options",1160,650,100,50,grey,bright_grey,0,0,20, option_screen)
        button (screen,"Quit",20,650,100,50,red,bright_red,0,0,20, quitgame)

        #Flip the screen
        pygame.display.flip()

# Start the program
program()

#end