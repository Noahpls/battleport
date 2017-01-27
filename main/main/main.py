""" PROJECT 2 : TEAM 1"""
#Imports

import pygame
import math

#####################################################################

class bootje2():
    def __init__ (self,x,y,player,length,hp):
        self.X = x
        self.Y = y
        self.player = player
        self.length = length
        self.mode = "attacking"
        self.hp = hp
        self.active = False
        self.pos= (self.X,self.Y) 
        self.zetten = 0
        self.movementbonus = 0
        self.rangebonus = 0

    def move(self):
        if self.active == True:
            move_menu(self)

    def hp_menu(self):
        if self.active == True:
            hp_menu_(self)

    def moving_left(self):
        if self.X <= 389:
            return False
        else:
            self.X = self.X - 25
            self.draw(boot2geel_)
            self.zetten = self.zetten + 1
            new_screen()
    def moving_right(self):
        if self.X >= 864:
            return False
        else:
            self.X = self.X + 25
            self.draw(boot2geel_)
            self.zetten = self.zetten + 1
            new_screen()
    def moving_up(self):
        if self.Y <= 100:
            return False
        else:
            self.Y = self.Y - 25
            self.draw(boot2geel_)
            self.zetten = self.zetten + 1
            new_screen()
    def moving_down(self):
        if self.Y >= 600 - (self.length*25):
            return False
        else:
            self.Y = self.Y + 25
            self.draw(boot2geel_)
            self.zetten = self.zetten + 1
            new_screen()

    def draw(self,plaatjeboot):
        screen.blit(plaatjeboot,[self.X,self.Y])
    def range(self):
        self.range = range
        if self.mode == "defensive" :
            #alleen verticaal schieten
            self.range = self.length + 1
        else:
            self.range = self.length
    def movement(self):
        if self.mode == "defensive" :
            #alleen verticaal schieten
            self.movement = 0
        else:
            self.movement = 5 - self.length 
            
#####################################################################

class Tile:
    def __init__(self, x, y, pos, size):
        self.X = x
        self.Y = y
        self.Pos = pos
        self.Size = size
        self.Color = (0,0,0)
          
    def Clear(self):
        self.Color = (0,0,0)
        
    def Draw(self):
        pygame.draw.rect(screen, self.Color, (self.X, self.Y, self.Size, self.Size))
        pygame.draw.lines(screen, (100,100,100), True, [(self.X,self.Y), (self.X+self.Size,self.Y), (self.X+self.Size,self.Y+self.Size), (self.X,self.Y+self.Size)],2)

#####################################################################        

class Grid:
    def __init__(self,x,y,size,tilesize):
        self.Tile_size = tilesize
        self.Size = size
        self.X = x
        self.Y = y

        
        self.Tile_x = self.X
        self.Tile_y = self.Y
        self.Tiles = [''] * self.Size
        for x in range(0, self.Size):
            self.Tiles[x] = [''] * self.Size
            for y in range(0, self.Size):
                self.Tiles[x][y] = Tile(self.Tile_x, self.Tile_y, [x,y], self.Tile_size)
                self.Tile_y = self.Tile_y + self.Tile_size
            self.Tile_x = self.Tile_x + self.Tile_size
            self.Tile_y = self.Y

    def Change_color(self, tile_x, tile_y, color):
        self.Tiles[tile_x][tile_y].Color = color

    def Clear(self):
        for y in range(0, self.Size):
            for x in range(0, self.Size):
                self.Tiles[x][y].Clear()

    def Draw(self):
        for y in range(0, self.Size):
            for x in range(0, self.Size):
                self.Tiles[x][y].Draw()

##################################################################### 

width = 1280
height = 720
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.init()

pygame.mixer.music.load("Achtergrond.mp3")
pygame.mixer.music.play(loops=200, start=0.0)

mouse =pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

#global image files
#set a resolution
radar = pygame.image.load('radar.jpg')
background_startscherm = pygame.image.load('radar background.jpg')
boten = pygame.image.load('boten achtergrond.jpg')
zee = pygame.image.load('Bord.jpg')
boot2rood_ = pygame.image.load('boot2rood.png')
boot3rood1_ = pygame.image.load('boot3rood.png')
boot3rood2_ = pygame.image.load('boot3rood.png')
boot4rood_ = pygame.image.load('boot4rood.png')
boot2geel_ = pygame.image.load('boot2geel.png')
boot3geel1_ = pygame.image.load('boot3geel.png')
boot3geel2_ = pygame.image.load('boot3geel.png')
boot4geel_ = pygame.image.load('boot4geel.png')
label1=pygame.image.load('button groen 1.png')
label3=pygame.image.load('button groen 3.png')
spelregels1=pygame.image.load('Spelregels NL 1.png')
spelregels2=pygame.image.load('Spelregels NL 2.png')
spelregels3=pygame.image.load('Spelregels NL 3.png')
spelregels4=pygame.image.load('Spelregels NL 4.png')
spelregels5=pygame.image.load('Spelregels NL 5.png')
settings=pygame.image.load('Settings.png')

turnplayer1 = True
turnplayer2 = False

mooigrid = Grid(389,100,20,25)

boot2geel = bootje2(mooigrid.Tiles[19][18].X,mooigrid.Tiles[19][18].Y,"player1",2,2)
boot3geel1 = bootje2(mooigrid.Tiles[10][17].X,mooigrid.Tiles[10][17].Y,"player1",3,3)
boot3geel2 = bootje2(mooigrid.Tiles[5][17].X,mooigrid.Tiles[5][17].Y,"player1",3,3)
boot4geel = bootje2(mooigrid.Tiles[0][16].X,mooigrid.Tiles[0][16].Y,"player1",4,4)

boot2rood = bootje2(mooigrid.Tiles[19][0].X,mooigrid.Tiles[19][0].Y,"player2",2,2)
boot3rood1 = bootje2(mooigrid.Tiles[10][0].X,mooigrid.Tiles[10][0].Y,"player2",3,3)
boot3rood2 = bootje2(mooigrid.Tiles[5][0].X,mooigrid.Tiles[5][0].Y,"player2",3,3)
boot4rood = bootje2(mooigrid.Tiles[0][0].X,mooigrid.Tiles[0][0].Y,"player2",4,4)


black=(0,0,0)
white=(255,255,255)
grey = (128,128,128)
red = (200,0,0)
green = (0,200,0)
blue = (0,51,150)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,51,205)
bright_grey=(155,155,155)
volume = 1

def quitgame():
    pygame.quit()
    quit ()

def play_sound():
    pygame.init()
    sonar_sound = pygame.mixer.Sound('Sonar_Sound.wav')
    sonar_sound.play()
    pygame.mixer.Sound.set_volume(sonar_sound, volume)
  
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    return False

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button (screen,msg,x,y,w,h,ic,ac,alw,ilw,fs,action = None, action2 = None):
    pygame.init()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,ac,(x,y,w,h),alw)
        if click[0] == 1 and action2 != None:
            action2()
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h),ilw)

    smallText = pygame.font.Font("freesansbold.ttf",fs)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

def plaatje(x,y,w,h,boot,action = None,ic=None,ac=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    boot2geel.draw(boot2geel_)
    boot3geel1.draw(boot3geel1_)
    boot3geel2.draw(boot3geel2_)
    boot4geel.draw(boot4geel_)

    boot2rood.draw(boot2rood_)
    boot3rood1.draw(boot3rood1_)
    boot3rood2.draw(boot3rood2_)
    boot4rood.draw(boot4rood_)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        
        if click[0] == 1 and action != None:
            boot.active = True

            if boot != boot2geel:
                boot2geel.active = False
            if boot != boot3geel1:
                boot3geel1.active = False
            if boot != boot3geel2:
                boot3geel2.active = False
            if boot != boot4geel:
                boot4geel.active = False
            if boot != boot2rood:
                boot2rood.active = False
            if boot != boot3rood1:
                boot3rood1.active = False
            if boot != boot3rood2:
                boot3rood2.active = False
            if boot != boot4rood:
                boot4rood.active = False
            action()
    else:
        if click[0] == 1:
            boot2geel.active = False
            boot3geel1.active = False
            boot3geel2.active = False
            boot4geel.active = False
            boot2rood.active = False
            boot3rood1.active = False
            boot3rood2.active = False
            boot4rood.active = False


def move_menu(boot):
    while not process_events():
        if boot.zetten != 5-boot.length + boot.movementbonus:
            button (screen,"^",270,290,40,40,grey,bright_grey,0,0,20, boot.moving_up)
            button (screen,">",320,340,40,40,grey,bright_grey,0,0,20, boot.moving_right)
            button (screen,"<",220,340,40,40,grey,bright_grey,0,0,20, boot.moving_left)
            button (screen,"v",270,390,40,40,grey,bright_grey,0,0,20, boot.moving_down)
            keys = pygame.key.get_pressed()
            if keys [pygame.K_LEFT]:
                boot.moving_left()
            if keys [pygame.K_RIGHT]:
                boot.moving_right()
            if keys [pygame.K_UP]:
                boot.moving_up()
            if keys [pygame.K_DOWN]:
                boot.moving_down()
        button (screen,"X",270,340,40,40,grey,bright_grey,0,0,20, new_screen)
        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
                new_screen()
        pygame.display.flip()
        button (screen,"HP:" + str(boot.hp),240,170,100,40,grey,grey,0,0,20)
        button (screen, "Moves:" + str(5-(boot.length+boot.zetten)), 240,210,100,40,grey,grey,0,0,20)
        pygame.display.update()

def hp_menu_(boot):
    while not process_events():
        button (screen,"X",270,340,40,40,grey,bright_grey,0,0,20, new_screen)
        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
                new_screen()
        pygame.display.flip()
        button (screen,"HP:" + str(boot.hp),240,170,100,40,grey,grey,0,0,20)
        pygame.display.update()
        
def circle (screen,x,y,r,w,h,ic,ac,ilw,alw,newvolume):
    pygame.init()
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x1 = x-r
    y1= y-r

    if x1+w > mouse[0] > x1 and y1+h > mouse[1] > y1:
        pygame.draw.circle(screen,ac,(x,y),r,ilw)
        if click[0] == 1:
            volume = newvolume
            
    else:
        pygame.draw.circle(screen,ic,(x,y),r,alw)

    
    
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

def player2true():
    global turnplayer1
    global turnplayer2
    turnplayer2 = True
    turnplayer1 = False
    new_screen()

def player1true():
    global turnplayer1
    global turnplayer2
    turnplayer1 = True
    turnplayer2 = False
    new_screen()

def overgangsscherm():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()
    

    #set a resolution
    screen = pygame.display.set_mode(size)

    screen.blit(boten, [0,0])
    boot2rood.zetten = 0
    boot3rood1.zetten = 0
    boot3rood2.zetten = 0
    boot4rood.zetten = 0

    boot2geel.zetten = 0
    boot3geel1.zetten = 0
    boot3geel2.zetten = 0
    boot4geel.zetten = 0

    while not process_events():
        if turnplayer1 == True:
            button (screen,"Player 2 ready?",500,500,300,50,green,bright_green,0,0,20,player2true)
            
        else:
            button (screen,"Player 1 ready?",500,500,300,50,green,bright_green,0,0,20,player1true)
            
        pygame.display.flip()
        pygame.display.update()


def new_screen():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()
    

    #set a resolution
    screen = pygame.display.set_mode(size)
    
    screen.blit(zee, [0,0])
    
    while not process_events():
        # Clear Screen
        
        mooigrid.Draw()

        if turnplayer1 == True:
            plaatje(boot2geel.X,boot2geel.Y,25,50,boot2geel,boot2geel.move)
            plaatje(boot3geel1.X,boot3geel1.Y,25,75,boot3geel1,boot3geel1.move)
            plaatje(boot3geel2.X,boot3geel2.Y,25,75,boot3geel2,boot3geel2.move)
            plaatje(boot4geel.X,boot4geel.Y,25,100,boot4geel,boot4geel.move)

            plaatje(boot2rood.X,boot2rood.Y,25,50,boot2rood,boot2rood.hp_menu)
            plaatje(boot3rood1.X,boot3rood1.Y,25,75,boot3rood1,boot3rood1.hp_menu)
            plaatje(boot3rood2.X,boot3rood2.Y,25,75,boot3rood2,boot3rood2.hp_menu)
            plaatje(boot4rood.X,boot4rood.Y,25,100,boot4rood,boot4rood.hp_menu)

        if turnplayer2 == True:
            plaatje(boot2rood.X,boot2rood.Y,25,50,boot2rood,boot2rood.move)
            plaatje(boot3rood1.X,boot3rood1.Y,25,75,boot3rood1,boot3rood1.move)
            plaatje(boot3rood2.X,boot3rood2.Y,25,75,boot3rood2,boot3rood2.move)
            plaatje(boot4rood.X,boot4rood.Y,25,100,boot4rood,boot4rood.move)

            plaatje(boot2geel.X,boot2geel.Y,25,50,boot2geel,boot2geel.hp_menu)
            plaatje(boot3geel1.X,boot3geel1.Y,25,75,boot3geel1,boot3geel1.hp_menu)
            plaatje(boot3geel2.X,boot3geel2.Y,25,75,boot3geel2,boot3geel2.hp_menu)
            plaatje(boot4geel.X,boot4geel.Y,25,100,boot4geel,boot4geel.hp_menu)

        button (screen,"Menu",1090,0,100,50,green,bright_green,0,0,20)
        button (screen,"Back",73,620,100,50,grey,bright_grey,0,0,20, program)
        button (screen,"Pass turn",1090,620,100,50,green,bright_green,0,0,20, overgangsscherm)
        if turnplayer1 == True:
            button(screen, "Speler 1",73,0,100,50, green,green,0,0,20)
        if turnplayer2 == True:
            button(screen, "Speler 2",73,0,100,50, green,green,0,0,20)
        #Flip the screen
        pygame.display.flip()
        pygame.display.update()

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
        screen.blit(label3, [240,50])
        #TESTBUTTON
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)
        button (screen,"Game Rules",450,200,200,75,green,bright_green,5,1,30, instructions1, play_sound)
       

        #Flip the screen
        pygame.display.flip()

def instructions1():
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
        screen.blit(spelregels1,[0,0])
        button (screen,"Next",1160,650,100,50,grey,bright_grey,0,0,20, instructions2)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()

def instructions2():
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
        screen.blit(spelregels2,[0,0])

        button (screen,"Next",1160,650,100,50,grey,bright_grey,0,0,20,instructions3)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, instructions1)

        #Flip the screen
        pygame.display.flip()

def instructions3():
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
        screen.blit(spelregels3,[0,0])

        button (screen,"Next",1160,650,100,50,grey,bright_grey,0,0,20,instructions4)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, instructions2)

        #Flip the screen
        pygame.display.flip()

def instructions4():
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
        screen.blit(spelregels4,[0,0])

        button (screen,"Next",1160,650,100,50,grey,bright_grey,0,0,20,instructions5)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, instructions3)

        #Flip the screen
        pygame.display.flip()

def instructions5():
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
        screen.blit(spelregels5,[0,0])

        button (screen,"Exit",1160,650,100,50,grey,bright_grey,0,0,20, program)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, instructions4)

        #Flip the screen
        pygame.display.flip()

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
        screen.fill(black)
        screen.blit(settings,[37,0])
        circle (screen,445,218,10,20,20,green,bright_green,0,1, 0)
        circle (screen,540,218,10,20,20,green,bright_green,0,1, 0.25)
        circle (screen,640,218,10,20,20,green,bright_green,0,1,0.50)
        circle (screen,741,218,10,20,20,green,bright_green,0,1,0.75)
        circle (screen,842,218,10,20,20,green,bright_green,0,1,1)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)

        #Flip the screen
        pygame.display.flip()

def program():
    width = 1280
    height = 720
    size = (width, height)
    #start PyGame
    pygame.init()

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

'''<<<<<<< HEAD
=======
import psycopg2

#Using Database
def interact_with_database(command):
	#connectie
	connection = psycopg2.connect("dbname=Battleport user=postgres")
	cursor = connection.cursor()
	
	#Execute
	cursor.execute(command)
	connection.commit()
	
	#Save results
	results = None
	try:
		results = cursor.fetchall()
	except psycopg2.ProgrammingError:
		#Nothing to fetchall
		pass
		
	#Close connection
	cursor.close()
	connection.close()
	
	return results
	
#Upload score into table
def upload_score(pname, games_won, games_played, won_percentage):
	interact_with_database("UPDATE scores SET scores = {} WHERE sname = '{}'"
							.format(pname, games_won, games_played, won_percentage))
							
#Downloads score from the database
def download_scores():
	return interact_with_database("SELECT * FROM scores")

#Downloads the top score from the database
def download_top_score():
		result = interact_with_database("SELECT * FROM scores ORDER BY scores")[0][1]
		return result
							

# Start the program
>>>>>>> origin/master'''
program()