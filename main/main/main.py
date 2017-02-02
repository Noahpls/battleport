""" PROJECT 2 : TEAM 1"""
#Imports

import pygame
import math
import sqlite3
import random
#####################################################################

class bootje2():
    def __init__ (self,x,y,player,length,hp):
        self.X = x
        self.Y = y
        self.player = player
        self.length = length
        self.range = self.length
        self.mode = "attacking"
        self.hp = hp
        self.active = False
        self.pos= (self.X,self.Y)
        self.aanvallen = 0 
        self.zetten = -40
        self.movementbonus = 0
        self.rangebonus = 0
        self.vierkantje = pygame.Rect(self.X,self.Y,25, 25*self.length)

    def turn(self):
        if self.X + 25*(self.length-1) < 889:
            if self.mode == "attacking":
                self.mode = "defensive"
                self.vierkantje = pygame.Rect(self.X,self.Y, 25*self.length, 25)
            else:
                self.mode = "attacking"
                self.vierkantje = pygame.Rect(self.X,self.Y, 25, 25*self.length)
            self.zetten = self.zetten+1
            new_screen()
        else:
            return False

    def attack(self):
        self.aanvallen = self.aanvallen + 1

    def damage(self):
        self.hp = self.hp - 1

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
            self.draw(boot2geel_,boot2geel_k)
            self.zetten = self.zetten + 1
            new_screen()
    def moving_right(self):
        if self.X >= 864:
            return False
        else:
            self.X = self.X + 25
            self.draw(boot2geel_,boot2geel_k)
            self.zetten = self.zetten + 1
            new_screen()
    def moving_up(self):
        if self.Y <= 100:
            return False
        else:
            self.Y = self.Y - 25
            self.draw(boot2geel_,boot2geel_k)
            self.zetten = self.zetten + 1
            new_screen()
    def moving_down(self):
        if self.Y >= 600 - (self.length*25):
            return False
        else:
            self.Y = self.Y + 25
            self.draw(boot2geel_,boot2geel_k)
            self.zetten = self.zetten + 1
            new_screen()

    def draw(self,plaatjeboot,plaatjebootkapot):
        if self.hp > 0:
            screen.blit(plaatjeboot,[self.X,self.Y])
        else:
            screen.blit(plaatjebootkapot,[self.X,self.Y])
            self.active = False
        

    def draw2(self,plaatjeboot,plaatjebootkapot):
        if self.hp > 0:
            screen.blit(plaatjeboot,[self.X,self.Y + self.length*25 - 25])
        else:
            screen.blit(plaatjebootkapot,[self.X,self.Y+ self.length*25 - 25])
    def range(self):
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
class cardholder:
    def __init__ (self, name, id, desc,amount,simg,bimg):
        self.Name = name
        self.id = id
        self.Desc = desc
        self.amount= amount
        self.simg = simg
        self.bimg = bimg

class Card:
    def __init__(self, x, y, width, height, name, desc, function, i, deck):
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height
        self.Name = name
        self.Desc = desc
        self.Function = function
        self.Active = True
        self.Deck = deck
        self.ID = i

        self.Pressed = False
        self.Pressing = False
    
    def Hover(self):
        if self.X < pygame.mouse.get_pos()[0] < self.X + self.Width:
            if self.Y < pygame.mouse.get_pos()[1] < self.Y + self.Height: 
                return True
            return False
        
        
    
    def Click(self): 
        return pygame.mouse.get_pressed()[0]

    def Draw(self):
        if self.Active:
            if self.Hover():
                # pygame.blit(game.Display, pygame.image.load("images\\cards\\" + self.name + "hover.png"), [self.X, self.Y])
                screen.blit(fmj_big, [540, 210])
                screen.blit(fmj_small, [self.X, self.Y])   
                self.Pressing = self.Click()
 
                

                if self.Pressing:
                    self.Pressed = True
                    self.Pressing = False
                else:
                    if self.Pressed:
                        #self.Function()
                        self.Deck.Remove_card(self.ID)
                        self.Pressed = False
            else:
                screen.blit(fmj_small, [self.X, self.Y])  
                       

        else:
            pygame.draw.rect(screen, (255,0,0), (self.X, self.Y, self.Width, self.Height))

class Deck:
    def __init__(self, x, y, player, limit):
        self.X = x
        self.Y = y
        self.Player = player
        self.Limit = limit

        self.Cards = [""] * self.Limit
    
    def Add_card(self, name, desc, function):
        i = 0
        x = self.X
        y = self.Y
        w = 50
        h = 100
        for card in self.Cards:
            if card == "":
                self.Cards[i] = Card(x, y, w, h, name, desc, function, i, self)
                break
            x = x + w + 25
            i += 1



    def Remove_card(self, element):
        del self.Cards[element]
        for i in range(element, self.Limit - 1):
            if self.Cards[i] != "":
                self.Cards[i].ID -= 1
                self.Cards[i].X -= self.Cards[i].Width + 25
        self.Cards.append("")
        new_screen()
    def Activate(self):
        for card in self.Cards:
            if card == "": break
            else:
                if card.Active: card.Active = False
                else: card.Active = True

    def Draw(self):
        for card in self.Cards:
            if card == "": break
            else: 
                card.Draw()
                
        
        
class Hand:
    def __init__(self, x, y, player):
        self.X = x
        self.Y = y
        self.Player = player

        self.Decks = [Deck(self.X, self.Y, self.Player, 6), Deck(self.X, self.Y, self.Player, 7), Deck(self.X, self.Y, self.Player, 8)]
        self.Normal = self.Decks[0]
        self.Traps = self.Decks[1]
        self.Special = self.Decks[2]
    
    def Activate(self):
        for deck in self.Decks:
            deck.Activate()


    def Draw(self):
        for deck in self.Decks:
            deck.Draw()


#####################################################################
width = 1280
height = 720
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.init()


pygame.mixer.music.load("Achtergrond.mp3")
pygame.mixer.music.play(200,5.0)


mouse =pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

#global image files
#set a resolution
radar = pygame.image.load('radar.jpg')
background_startscherm = pygame.image.load('radar background.jpg')
boten = pygame.image.load('boten achtergrond.jpg')
zee = pygame.image.load('Bord2.jpg')
eindscherm = pygame.image.load('eindscherm.jpg')
boot2rood_ = pygame.image.load('boot2rood.png')
boot2rood_d = pygame.image.load('boot2rood_d.png')
boot2rood_k = pygame.image.load('boot2rood_dood.png')
boot2rood_dk = pygame.image.load('boot2rood_dood_d.png')

boot3rood1_ = pygame.image.load('boot3rood.png')
boot3rood1_d = pygame.image.load('boot3rood_d.png')
boot3rood1_k = pygame.image.load('boot3rood_dood.png')
boot3rood1_dk = pygame.image.load('boot3rood_dood_d.png')

boot3rood2_ = pygame.image.load('boot3rood.png')
boot3rood2_d = pygame.image.load('boot3rood_d.png')
boot3rood2_k = pygame.image.load('boot3rood_dood.png')
boot3rood2_dk = pygame.image.load('boot3rood_dood_d.png')

boot4rood_ = pygame.image.load('boot4rood.png')
boot4rood_d = pygame.image.load('boot4rood_d.png')
boot4rood_k = pygame.image.load('boot4rood_dood.png')
boot4rood_dk = pygame.image.load('boot4rood_dood_d.png')

boot2geel_ = pygame.image.load('boot2geel.png')
boot2geel_d = pygame.image.load('boot2geel_d.png')
boot2geel_k = pygame.image.load('boot2geel_dood.png')
boot2geel_dk = pygame.image.load('boot2geel_dood_d.png')

boot3geel1_ = pygame.image.load('boot3geel.png')
boot3geel1_d = pygame.image.load('boot3geel_d.png')
boot3geel1_k = pygame.image.load('boot3geel_dood.png')
boot3geel1_dk = pygame.image.load('boot3geel_dood_d.png')

boot3geel2_ = pygame.image.load('boot3geel.png')
boot3geel2_d = pygame.image.load('boot3geel_d.png')
boot3geel2_k = pygame.image.load('boot3geel_dood.png')
boot3geel2_dk = pygame.image.load('boot3geel_dood_d.png')

boot4geel_ = pygame.image.load('boot4geel.png')
boot4geel_d = pygame.image.load('boot4geel_d.png')
boot4geel_k = pygame.image.load('boot4geel_dood.png')
boot4geel_dk = pygame.image.load('boot4geel_dood_d.png')

label1=pygame.image.load('button groen 1.png')
label3=pygame.image.load('button groen 3.png')

boatinfo = pygame.image.load('Spelregels 2.png')

spelregels1=pygame.image.load('Spelregels NL 1.png')
spelregels2=pygame.image.load('Spelregels NL 2.png')
spelregels3=pygame.image.load('Spelregels NL 3.png')
spelregels4=pygame.image.load('Spelregels NL 4.png')
spelregels5=pygame.image.load('Spelregels NL 5.png')
settings=pygame.image.load('Settings.png')
card1 = pygame.image.load("Kaart tekst.png")
card1groot = pygame.image.load("Kaart groot tekst.png")
p1wins = 0
p1games = 0
p2wins = 0
p2games = 0
p1won_percentage = 0
p2won_percentage = 0
#Cards
fmj_small                   = pygame.image.load('Kaart FMJ.png')
fmj_big                     = pygame.image.load('Kaart FMJ groot.png')
rifling_small               = pygame.image.load('Kaart rifling.png')    
rifling_big                 = pygame.image.load('Kaart rifling groot.png')
advanced_rifling_small      = pygame.image.load('Kaart adv rifling.png')
advanced_rifling_big        = pygame.image.load('Kaart adv rifling groot.png')
emp_upgrade_small           = pygame.image.load('Kaart EMP.png')
emp_upgrade_big             = pygame.image.load('Kaart EMP groot.png')
reinforced_hull_small       = pygame.image.load('Kaart reinf hull.png')
reinforced_hull_big         = pygame.image.load('Kaart reinf hull groot.png')
sonar_small                 = pygame.image.load('Kaart sonar.png')
sonar_big                   = pygame.image.load('Kaart sonar groot.png')
smokescreen_small           = pygame.image.load('Kaart smoke.png')
smokescreen_big             = pygame.image.load('Kaart smoke groot.png')
sabotage_small              = pygame.image.load('Kaart sabotage.png')
sabotage_big                = pygame.image.load('Kaart sabotage groot.png')
backup_small                = pygame.image.load('Kaart backup.png')
backup_big                  = pygame.image.load('Kaart backup groot.png')
extra_fuel_small            = pygame.image.load('Kaart fuel.png')
extra_fuel_big              = pygame.image.load('Kaart fuel groot.png')
extra_fuel2_small           = pygame.image.load('Kaart fuel 2.png')
extra_fuel2_big             = pygame.image.load('Kaart fuel 2 groot.png')
rally_small                 = pygame.image.load('Kaart rally.png')
rally_big                   = pygame.image.load('Kaart rally groot.png')
nuclear_small               = pygame.image.load('Kaart nuclear.png')
nuclear_big                 = pygame.image.load('Kaart nuclear groot.png')
repair_small                = pygame.image.load('Kaart repair.png')
repair_big                  = pygame.image.load('Kaart repair groot.png')
far_sight_small             = pygame.image.load('Kaart far sight.png')
far_sight_big               = pygame.image.load('Kaart far sight groot.png')
aluminium_hull_small        = pygame.image.load('Kaart aluminium.png')
aluminium_hull_big          = pygame.image.load('Kaart aluminium groot.png')

reps = 0
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
boot4rood = bootje2(mooigrid.Tiles[0][0].X,mooigrid.Tiles[0][0].Y, "player2",4,4)

special = {"1": "!","2": "@","3": "#","4": "$","5": "%","6": "^","7": "&","8": "*","9": "(","0": ")","`": "~","-": "_","=": "+",",": "<",".": ">","/": "?",";": ":","'": chr(34),"[": "{","]": "}",chr(92): "|"}

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
dark_red=(120,13,3)
volume = 1

#Create card instance
#Offensive
fmj_upgrade = cardholder("FMJ Upgrade",0,"When this card is used, your next shot does +1 damage.",2,fmj_small,fmj_big)
rifling = cardholder("Rifling",1,"When this card is used, your next shot has +1 range.",2,rifling_small,rifling_big)
advanced_rifling = cardholder("Advanced Rifling",2,"When this card is used, your next shot has +2 range.",2,advanced_rifling_small,advanced_rifling_big)
emp_upgrade = cardholder("EMP Upgrade", 3, "When this card is used, your shot will disable the movement and attack of the ship(s) that got hit for 1 turn.",4,emp_upgrade_small,emp_upgrade_big)

#defensive
reinforced_hull = cardholder("Reinforced Hull",4,"Adds one HP to a friendly ship of your choice when this card is played.",2,reinforced_hull_small,reinforced_hull_big)
sonar = cardholder("Sonar",5,"Choose a potential mine location to spot and deactivate that mine and place it in the discarded deck.",4,sonar_small,sonar_big)
smokescreen = cardholder("Smokescreen",6,"When a friendly ship gets attacked, you may activate this card to make the attack miss.",2,smokescreen_small,smokescreen_big)
sabotage = cardholder("Sabotage",7,"When activated, your opponent's attack deals damage to its own ship.",2,sabotage_small,sabotage_big)

#Utility
backup = cardholder("Backup",8,"Draw two cards.",2,backup_small,backup_big)
extra_fuel = cardholder("Extra Fuel",9,"Select a friendly ship to make it move +1 step.",6,extra_fuel_small,extra_fuel_small)
extra_fuel2 = cardholder("Extra Fuel II",10,"Select a friendly ship to make it move +1 step.",4,extra_fuel2_small,extra_fuel2_big)
rally = cardholder("Rally",11,"All friendly ships van move +1 step.",1,rally_small,rally_big)
nuclear = cardholder("Nuclear",12,"Select a friendly ship to make its moveset x2.",4,nuclear_small,nuclear_big)

#Special cards
repair = cardholder("Repair", 13, "Select a friendly ship to fully heal this ship (Base HP).",2,repair_small,repair_big)
far_sight = cardholder("Far Sight", 14, "The used ship now has +2 range.",1,far_sight_small,far_sight_big)
aluminium_hull = cardholder("Aluminium Hull",15,"The used ship now has its moveset x2.",1,aluminium_hull_small,aluminium_hull_big)



#hand
handp1 = Hand(425,625,1)
handp2 = Hand(425,625,1)


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
        if event.type == pygame.KEYDOWN:
            if turnplayer1 == True:
                if event.key == pygame.K_1:
                    handp1.Normal.Add_card(fmj_upgrade.Name, fmj_upgrade.Desc, 1)
                if event.key == pygame.K_2:
                    handp1.Normal.Add_card(advanced_rifling.Name, advanced_rifling.Desc, 1)
                if event.key == pygame.K_3:
                    handp1.Activate()
            if turnplayer2 == True:
                if event.key == pygame.K_1:
                    handp2.Normal.Add_card(fmj_upgrade.Name, fmj_upgrade.Desc, 1)
                if event.key == pygame.K_2:
                    handp2.Normal.Add_card(advanced_rifling.Name, advanced_rifling.Desc, 1)
                if event.key == pygame.K_3:
                    handp2.Activate()

        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    return False
 
done = False
def name_input():
    global done
    class input_page:# the actual screen

	    def __init__(self):
		    self.lst = [] # list of text box's
		    self.current = 0 #currently selected string

	    def get_input(self,event,mouse_pos):
		    if event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:# move to next box in the list
				    if self.current < len(self.lst)-1:
					    self.current += 1
		    if event.type == pygame.MOUSEBUTTONDOWN:# sees if you click in the box
			    for i in range(len(self.lst)):
				    if self.lst[i].rect.collidepoint(mouse_pos):
					    self.lst[i].current = True
					    self.current = i
					    for g in range(len(self.lst)):
						    if g != i:
							    self.lst[g].current = False
				
		    for i in range(len(self.lst)):# makes all other text boxes not the current one selected
			    if i == self.current:
				    self.lst[i].current = True
				    self.lst[i].get_input(event)
				    for g in range(len(self.lst)):
						    if g != i:
							    self.lst[g].current = False
				

	    def render(self,screen):
		    for i in range(len(self.lst)): # renders the text boxes
			    self.lst[i].render(screen)

    class text_box:

	    def __init__(self,location,width,height,question = None,text_color = (255,255,255), font = None,font_size = 20):
		    self.location = location
		    self.text = ""
		    self.question = question
		    self.current = False
		    self.rect = pygame.Rect((location),(width,max(height,25)))
		    self.font_size = font_size
		    self.font = pygame.font.Font(font,font_size)
		    self.text_color = text_color
		    self.outline = (255,255,255)
		    self.rect_color = (0,0,0)

	    def render(self,screen):
		    if self.current == True:
			    temp = (self.rect[0]-3,self.rect[1]-3,self.rect[2]+6,self.rect[3]+6)# if you change the numbers, the second two need to be multiplied by 2 and postive
			    pygame.draw.rect(screen,(255,105,34),temp)
		    pygame.draw.rect(screen,self.rect_color,self.rect)
		    pygame.draw.rect(screen,self.outline,self.rect,1)
		    screen.blit(self.font.render(self.question,1,self.text_color),(self.location[0]-self.font.size(self.question)[0]-100,self.location[1]+4))
		    screen.blit(self.font.render(self.text,1,self.text_color),(self.location[0]+2,self.location[1]+4))
	    def get_input(self,event):
		    if event.type == pygame.KEYDOWN:
			    if 31<event.key<127 and event.key != 8: # making sure not backspace or error throwing key
				    if event.mod & (pygame.KMOD_SHIFT | pygame.KMOD_CAPS): # sees if caps or shift is on
					    if chr(event.key) in special.keys(): # Shifted keys
						    self.text += special[chr(event.key)]# adds to the current string
					    else:
						    self.text += chr(event.key).upper() # uppercase
				    else:
					    self.text += chr(event.key)# lowercase
			    if event.key == 8: # Backspace
				    self.text = self.text[0:-1]
			    if event.key == 127: # delete entire string, comment out if you want
				    self.text = ""
			    if self.font.size(self.text)[0] > self.rect.size[0]-5:# makes sure it isn't making text outside of the rect
				    self.text = self.text[0:-1]
    inp = input_page()# make the page class
    text = text_box((int(width/1.75),height/2-145),200,25,"Name player 1 -->")# make the text box classes
    text2 = text_box((int(width/1.75),height/2-95),200,25,"Name player 2 -->")
    inp.lst = [text,text2]# add the boxes to a list
    global text
    global text2
    while done == False:
    
        screen.blit(radar,(0,0))
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            inp.get_input(event,pos)# give the boxes input

        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)
        button (screen,"FIGHT!",1160,650,100,50,grey,bright_grey,0,0,20, new_screen, read_from_db)

        inp.render(screen)# render the boxes
        pygame.display.flip()       

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

def Text_draw(text, size, x, y, textcolor=(255,255,255)):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, textcolor)
    screen.blit(screen_text, [x,y])


def carddraw():
    r = random.randint(0,15)
    foundcard = 0
    while foundcard == 0:
        if r == 1:
        
            if fmj_upgrade.amount == 0:
                foundcard = 0
            else:
                fmj_upgrade.amount = fmj_upgrade.amount - 1
                foundcard = 1
                activecard = fmj_upgrade
                return activecard

        elif r == 2:
        
            if rifling.amount == 0:
                foundcard = 0
            else:
                rifling.amount = rifling.amount - 1
                foundcard = 1
                activecard = rifling
                return activecard
        elif r == 3:
        
            if advanced_rifling.amount == 0:
                foundcard = 0
            else:
                advanced_rifling.amount = advanced_rifling.amount - 1
                foundcard = 1
                activecard = advanced_rifling
                return activecard


        elif r == 4:
        
            if emp_upgrade.amount == 0:
                foundcard = 0
            else:
                emp_upgrade.amount = emp_upgrade.amount - 1
                foundcard = 1
                activecard = emp_upgrade
                return activecard

        elif r == 5:
        
            if reinforced_hull.amount == 0:
                foundcard = 0
            else:
                reinforced_hull.amount = reinforced_hull.amount - 1
                foundcard = 1
                activecard = reinforced_hull
                return activecard

       
        elif r == 6:
        
            if smokescreen.amount == 0:
                foundcard = 0
            else:
                smokescreen.amount = smokescreen.amount - 1
                foundcard = 1
                activecard = smokescreen
                return activecard

        elif r == 7:
        
            if sabotage.amount == 0:
                foundcard = 0
            else:
                sabotage.amount = sabotage.amount - 1
                foundcard = 1
                activecard = sabotage
                return activecard

        elif r == 8:
        
            if backup.amount == 0:
                foundcard = 0
            else:
                backup.amount = backup.amount - 1
                foundcard = 1
                activecard = backup
                return activecard

        elif r == 9:
        
            if extra_fuel.amount == 0:
                foundcard = 0
            else:
                extra_fuel.amount = extra_fuel.amount - 1
                foundcard = 1
                activecard = extra_fuel
                return activecard

        elif r == 10:
        
            if extra_fuel2.amount == 0:
                foundcard = 0
            else:
                extra_fuel2.amount = extra_fuel2.amount - 1
                foundcard = 1
                activecard = extra_fuel2
                return activecard

        elif r == 11:
        
            if rally.amount == 0:
                foundcard = 0
            else:
                rally.amount = rally.amount - 1
                foundcard = 1
                activecard = rally
                return activecard

        elif r == 12:##
        
            if nuclear.amount == 0:
                foundcard = 0
            else:
                nuclear.amount = nuclear.amount - 1
                foundcard = 1
                activecard = nuclear
                return activecard

        elif r == 13:
        
            if repair.amount == 0:
                foundcard = 0
            else:
                repair.amount = repair.amount - 1
                foundcard = 1
                activecard = repair
                return activecard


        elif r == 14:
        
            if far_sight.amount == 0:
                foundcard = 0
            else:
                far_sight.amount = far_sight.amount - 1
                foundcard = 1
                activecard = far_sight
                return activecard

        elif r == 15:
        
            if aluminium_hull.amount == 0:
                foundcard = 0
            else:
                aluminium_hull.amount = aluminium_hull.amount - 1
                foundcard = 1
                activecard = aluminium_hull
                return activecard


def plaatje(x,y,w,h,boot,action = None,ic=None,ac=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if boot2geel.mode == "attacking":
        boot2geel.draw(boot2geel_,boot2geel_k)
    else:
        boot2geel.draw(boot2geel_d,boot2geel_dk)

    if boot3geel1.mode == "attacking":
        boot3geel1.draw(boot3geel1_,boot3geel1_k)
    else:
        boot3geel1.draw(boot3geel1_d,boot3geel1_dk)
    
    if boot3geel2.mode == "attacking":
        boot3geel2.draw(boot3geel2_,boot3geel2_k)
    else:
        boot3geel2.draw(boot3geel2_d,boot3geel2_dk)

    if boot4geel.mode == "attacking":
        boot4geel.draw(boot4geel_,boot4geel_k)
    else:
        boot4geel.draw(boot4geel_d,boot4geel_dk)


    if boot2rood.mode == "attacking":
        boot2rood.draw(boot2rood_,boot2rood_k)
    else:
        boot2rood.draw2(boot2rood_d,boot2rood_dk)

    if boot3rood1.mode == "attacking":
        boot3rood1.draw(boot3rood1_,boot3rood1_k)
    else:
        boot3rood1.draw2(boot3rood1_d,boot3rood1_dk)

    if boot3rood2.mode == "attacking":
        boot3rood2.draw(boot3rood2_,boot3rood2_k)
    else:
        boot3rood2.draw2(boot3rood2_d,boot3rood2_dk)

    if boot4rood.mode == "attacking":
        boot4rood.draw(boot4rood_,boot4rood_k)
    else:
        boot4rood.draw2(boot4rood_d,boot4rood_dk)
        
    if boot.player == "player1" and (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
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
            if turnplayer1 == True:
                print(boot.player, boot.X, boot.Y, boot.length, boot.mode)
                print(boot2rood.player, boot2rood.X, boot2rood.Y, boot2rood.length,boot2rood.mode)
                print(boot3rood1.player, boot3rood1.X, boot3rood1.Y, boot3rood1.length,boot3rood1.mode)
                print(boot3rood2.player, boot3rood2.X, boot3rood2.Y, boot3rood2.length,boot3rood2.mode)
                print(boot4rood.player, boot4rood.X, boot4rood.Y, boot4rood.length,boot4rood.mode)
                #for bootje in [boot2rood, boot3rood1, boot3rood2, boot4rood]:
                    #for i in[1-(boot.length+boot.range),boot.range]:
                        #if bootje.X == boot.X and (boot.Y - i *25 <= (bootje.Y + (bootje.length - 1 )*25) and  boot.Y - i *25 >=  bootje.Y ):

            action()

    elif (boot.player == "player2" and boot.mode == "defensive" and x+w > mouse[0] > x and y+25*boot.length > mouse[1] > y+25*boot.length-25):
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
            if turnplayer2 == True:
                print(boot.player, boot.X, boot.Y, boot.length, boot.mode)
                print(boot2geel.player, boot2geel.X, boot2geel.Y, boot2geel.length,boot2geel.mode)
                print(boot3geel1.player, boot3geel1.X, boot3geel1.Y, boot3geel1.length,boot3geel1.mode)
                print(boot3geel2.player, boot3geel2.X, boot3geel2.Y, boot3geel2.length,boot3geel2.mode)
                print(boot4geel.player, boot4geel.X, boot4geel.Y, boot4geel.length,boot4geel.mode)
            action()
    elif (boot.player == "player2" and boot.mode == "attacking") and (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
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
            if turnplayer2 == True:
                print(boot.player, boot.X, boot.Y, boot.length, boot.mode)
                print(boot2geel.player, boot2geel.X, boot2geel.Y, boot2geel.length,boot2geel.mode)
                print(boot3geel1.player, boot3geel1.X, boot3geel1.Y, boot3geel1.length,boot3geel1.mode)
                print(boot3geel2.player, boot3geel2.X, boot3geel2.Y, boot3geel2.length,boot3geel2.mode)
                print(boot4geel.player, boot4geel.X, boot4geel.Y, boot4geel.length,boot4geel.mode)
                for bootje in [boot2geel, boot3geel1, boot3geel2, boot4geel]:
                    for i in[1-(boot.length+boot.range),boot.range]:
                        if bootje.X == boot.X and (boot.Y - i *25 <= (bootje.Y + (bootje.length - 1 )*25) and  boot.Y - i *25 >=  bootje.Y ):
                            print("in range")
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
        if boot.zetten != 5-boot.length + boot.movementbonus and boot.hp > 0:
            if boot.mode == "attacking":
                button (screen,"^",1095,275,60,60,grey,bright_grey,0,0,20, boot.moving_up)
                button (screen,">",1160,340,60,60,grey,bright_grey,0,0,20, boot.moving_right)
                button (screen,"<",1030,340,60,60,grey,bright_grey,0,0,20, boot.moving_left)
                button (screen,"v",1095,405,60,60,grey,bright_grey,0,0,20, boot.moving_down)
                keys = pygame.key.get_pressed()
                if keys [pygame.K_LEFT]:
                    boot.moving_left()
                if keys [pygame.K_RIGHT]:
                    boot.moving_right()
                if keys [pygame.K_UP]:
                    boot.moving_up()
                if keys [pygame.K_DOWN]:
                    boot.moving_down()
            button (screen, "TURN", 1160, 275, 60, 60, grey, bright_grey, 0, 0 ,15, boot.turn)
        button (screen,"X",1095,340,60,60,grey,bright_grey,0,0,20, new_screen)
        
        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
                new_screen()
        pygame.display.flip()
        button (screen,"HP:" + str(boot.hp),1075,170,100,40,grey,grey,0,0,20)
        if boot.hp > 0:
            button (screen, "Moves:" + str(5-(boot.length+boot.zetten)), 1075,210,100,40,grey,grey,0,0,20)
        pygame.display.update()

def hp_menu_(boot):
    while not process_events():
        button (screen,"X",1095,340,60,60,grey,bright_grey,0,0,20, new_screen)
        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
                new_screen()
        pygame.display.flip()
        button (screen,"HP:" + str(boot.hp),1075,170,100,40,grey,grey,0,0,20)
        #boot is degene waarop geklikt is die wordt aangevallen, bootje is de aanvaller
        if turnplayer1 == True:
            for bootje in [boot2geel, boot3geel1, boot3geel2, boot4geel]:
                if boot.hp > 0:
                    if bootje.hp > 0:
                        if bootje.mode ==  "attacking" and boot.mode == "attacking":
                            for o in [-bootje.vierkantje.height, bootje.vierkantje.height]:
                                if (bootje.Y + o - 25 >= boot.Y >= bootje.Y or bootje.Y + o - 25 >= boot.Y + boot.vierkantje.height - 25 >= bootje.Y) and (bootje.X + o >= boot.X >= bootje.X - o):
                                    if bootje.aanvallen < 1:
                                        button (screen,"Attack!",1045,240,160,40,grey,bright_grey,0,0,20,boot.damage,bootje.attack)
                                    else:
                                        button (screen,"Je hebt al aangevallen",1045,240,160,40,grey,grey,0,0,15)
                        #vGOEDv
                            for i in[1-(bootje.length+bootje.range),bootje.range]:
                                if boot.hp > 0:
                                        if bootje.hp > 0:
                                            if boot.X == bootje.X and (bootje.Y - i *25 <= (boot.Y + (boot.length - 1 )*25) and  bootje.Y - i *25 >=  boot.Y ):
                                
                                                if bootje.aanvallen < 1:
                                                    button (screen,"Attack!",1045,240,160,40,grey,bright_grey,0,0,20,boot.damage,bootje.attack)
                                                else:
                                                    button (screen,"Je hebt al aangevallen",1045,240,160,40,grey,grey,0,0,15)
                    elif bootje.mode == "attacking" and boot.mode == "defensive":
                        return False
                    elif bootje.mode == "defensive" and boot.mode == "attacking":
                        return False
                    elif bootje.mode == "defensive" and boot.mode == "defensive":
                        return False
         

        else:
            for bootje in [boot2rood, boot3rood1, boot3rood2, boot4rood]:
                if boot.hp >0:
                    if bootje.hp > 0:
                        if bootje.mode ==  "attacking" and boot.mode == "attacking":
                            for o in [-bootje.vierkantje.height, bootje.vierkantje.height]:
                                if (bootje.Y + o - 25 >= boot.Y >= bootje.Y or bootje.Y + o - 25 >= boot.Y + boot.vierkantje.height - 25 >= bootje.Y) and (bootje.X + o >= boot.X >= bootje.X - o):
                                    if bootje.aanvallen < 1:
                                        button (screen,"Attack!",1045,240,160,40,grey,bright_grey,0,0,20,boot.damage,bootje.attack)
                                    else:
                                        button (screen,"Je hebt al aangevallen",1045,240,160,40,grey,grey,0,0,15)
                        #vGOEDv
                            for i in[1-(bootje.length+bootje.range),bootje.range]:
                                if boot.hp > 0:
                                        if bootje.hp > 0:
                                            if boot.X == bootje.X and (bootje.Y - i *25 <= (boot.Y + (boot.length - 1 )*25) and  bootje.Y - i *25 >=  boot.Y ):
                                                if bootje.aanvallen < 1:
                                                    button (screen,"Attack!",1045,240,160,40,grey,bright_grey,0,0,20,boot.damage,bootje.attack)
                                                else:
                                                    button (screen,"Je hebt al aangevallen",1045,240,160,40,grey,grey,0,0,15)
                    elif bootje.mode == "attacking" and boot.mode == "defensive":
                        return False
                    elif bootje.mode == "defensive" and boot.mode == "attacking":
                        return False
                    elif bootje.mode == "defensive" and boot.mode == "defensive":
                        return False
                                        
        pygame.display.update()
        
def circle (screen,x,y,r,w,h,ic,ac,ilw,alw,action = None):
    pygame.init()
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x1 = x-r
    y1= y-r

    if x1+w > mouse[0] > x1 and y1+h > mouse[1] > y1:
        pygame.draw.circle(screen,ac,(x,y),r,ilw)
        if click[0] == 1 and action != None:
            action()
            
    else:
        pygame.draw.circle(screen,ic,(x,y),r,alw)

#def handplayer1():
#     handp1.Normal.Add_card(activecard.Name, activecard.Desc, 1)   

#def handplayer2():
#     handp2.Normal.Add_card(activecard.Name, activecard.Desc, 1) 
    
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
        button (screen,"New Game",850,175,200,75,green,bright_green,5,1,20, name_input,play_sound)
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
    boot2rood.zetten = -40
    boot3rood1.zetten = -40
    boot3rood2.zetten = -40
    boot4rood.zetten = -40

    boot2rood.aanvallen = 0
    boot3rood1.aanvallen = 0
    boot3rood2.aanvallen = 0
    boot4rood.aanvallen = 0


    boot2geel.zetten = -40
    boot3geel1.zetten = -40
    boot3geel2.zetten = -40
    boot4geel.zetten = -40

    boot2geel.aanvallen = 0
    boot3geel1.aanvallen = 0
    boot3geel2.aanvallen = 0
    boot4geel.aanvallen = 0

    while not process_events():
        keys = pygame.key.get_pressed()
        if turnplayer1 == True:
            button (screen, text2.text + " ready?",500,500,300,50,green,bright_green,0,0,20,player2true)
            if keys [pygame.K_RETURN]:
                    player2true()
        else:
            button (screen,text.text + " ready?",500,500,300,50,green,bright_green,0,0,20,player1true)
            if keys [pygame.K_RETURN]:
                    player1true()
            
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
    global p1wins
    global p1games
    screen.blit(zee, [0,0])
    print ("p1: " + str(p1wins) + " " + str(p1games))
    print ("p2 wins: " + str(p2wins) + ", total games: " + str(p2games))
    while not process_events():
        # Clear Screen
        
        mooigrid.Draw()
        
        if turnplayer1 == True:
            plaatje(boot2geel.X,boot2geel.Y,boot2geel.vierkantje.width,boot2geel.vierkantje.height,boot2geel,boot2geel.move)
            plaatje(boot3geel1.X,boot3geel1.Y,boot3geel1.vierkantje.width,boot3geel1.vierkantje.height,boot3geel1,boot3geel1.move)
            plaatje(boot3geel2.X,boot3geel2.Y,boot3geel2.vierkantje.width,boot3geel2.vierkantje.height,boot3geel2,boot3geel2.move)
            plaatje(boot4geel.X,boot4geel.Y,boot4geel.vierkantje.width, boot4geel.vierkantje.height,boot4geel,boot4geel.move)

            plaatje(boot2rood.X,boot2rood.Y,boot2rood.vierkantje.width,boot2rood.vierkantje.height,boot2rood,boot2rood.hp_menu)
            plaatje(boot3rood1.X,boot3rood1.Y,boot3rood1.vierkantje.width,boot3rood1.vierkantje.height,boot3rood1,boot3rood1.hp_menu)
            plaatje(boot3rood2.X,boot3rood2.Y,boot3rood2.vierkantje.width,boot3rood2.vierkantje.height,boot3rood2,boot3rood2.hp_menu)
            plaatje(boot4rood.X,boot4rood.Y,boot4rood.vierkantje.width,boot4rood.vierkantje.height,boot4rood,boot4rood.hp_menu)

            handp1.Draw()
            #button (screen,"Draw a card",150,615,100,50,green,bright_green,0,0,20,handplayer1)

        if turnplayer2 == True:
            plaatje(boot2geel.X,boot2geel.Y,boot2geel.vierkantje.width,boot2geel.vierkantje.height,boot2geel,boot2geel.hp_menu)
            plaatje(boot3geel1.X,boot3geel1.Y,boot3geel1.vierkantje.width,boot3geel1.vierkantje.height,boot3geel1,boot3geel1.hp_menu)
            plaatje(boot3geel2.X,boot3geel2.Y,boot3geel2.vierkantje.width,boot3geel2.vierkantje.height,boot3geel2,boot3geel2.hp_menu)
            plaatje(boot4geel.X,boot4geel.Y,boot4geel.vierkantje.width, boot4geel.vierkantje.height,boot4geel,boot4geel.hp_menu)

            plaatje(boot2rood.X,boot2rood.Y,boot2rood.vierkantje.width,boot2rood.vierkantje.height,boot2rood,boot2rood.move)
            plaatje(boot3rood1.X,boot3rood1.Y,boot3rood1.vierkantje.width,boot3rood1.vierkantje.height,boot3rood1,boot3rood1.move)
            plaatje(boot3rood2.X,boot3rood2.Y,boot3rood2.vierkantje.width,boot3rood2.vierkantje.height,boot3rood2,boot3rood2.move)
            plaatje(boot4rood.X,boot4rood.Y,boot4rood.vierkantje.width,boot4rood.vierkantje.height,boot4rood,boot4rood.move)

            handp2.Draw()
            #button (screen,"Draw a card",150,615,100,50,green,bright_green,0,0,20,handplayer2)

        
        button (screen,"Boat info",1160,30,100,50,green,bright_green,0,0,15,boat_info)
        button (screen,"Back", 990,30,100,50,grey,bright_grey,0,0,20, program)
        if (boot2geel.hp != 0 or boot3geel1.hp != 0 or boot3geel2.hp != 0 or boot4geel.hp != 0) and (boot2rood.hp != 0 or boot3rood1.hp != 0 or boot3rood2.hp != 0 or boot4rood.hp != 0):
            button (screen,"Pass turn",1075,515,100,50,green,bright_green,0,0,20, overgangsscherm)
        elif boot2geel.hp == 0 and boot3geel1.hp == 0 and boot3geel2.hp == 0 and boot4geel.hp == 0:
            #P2 heeft gewonnen
            button (screen,"End game",1075,515,100,50,green,bright_green,0,0,20, eindscherm2)
        elif boot2rood.hp == 0 and boot3rood1.hp == 0 and boot3rood2.hp == 0 and boot4rood.hp == 0:
            #P1 heeft gewonnen
            button (screen,"End game",1075,515,100,50,green,bright_green,0,0,20, eindscherm1)

        keys = pygame.key.get_pressed()
        if keys [pygame.K_RETURN]:
                    overgangsscherm()
        if turnplayer1 == True:
            button(screen, text.text,565,5,150,50, green,green,0,0,20)
        if turnplayer2 == True:
            button(screen, text2.text,565,5,150,50, green,green,0,0,20)
        #button (screen,"End game",1075,565,100,50,green,bright_green,0,0,20, eindscherm1)
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

def boat_info():
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
        screen.blit(boatinfo,[0,0])
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, new_screen)

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
    ##
    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])
        screen.blit(spelregels5,[0,0])

        button (screen,"Exit",1160,650,100,50,grey,bright_grey,0,0,20, program)
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, instructions4)

        #Flip the screen
        pygame.display.flip()

def eindscherm1():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    screen = pygame.display.set_mode(size)
    global p2wins
    global p1wins
    global p1games
    global p2games
    global p1won_percentage
    global p2won_percentage
    p2wins = int(p2wins)
    p1wins = int(p1wins) + 1
    p1games = int(p1games) + 1
    p2games = int(p2games) + 1
    p2won_percentage = (p2wins/p2games)*100
    p1won_percentage = (p1wins/p1games)*100
    data_entry()
    while not process_events():
        # Clear Screen
        screen.blit(eindscherm,[0,0])
        button (screen,text.text,395,358,124,50,bright_grey,bright_grey,1,1,26)
        button (screen,"Quit",190,561,278,50,dark_red,red,0,0,26, quitgame)
        #Flip the screen
        pygame.display.flip()

def eindscherm2():
    width = 1280
    height = 720
    size = (width, height)

    #start PyGame
    pygame.init()

    #set a resolution
    global p2wins
    global p1wins
    global p1games
    global p2games
    global p2won_percentage
    global p1won_percentage
    screen = pygame.display.set_mode(size)
    p2wins = int(p2wins) + 1
    p1wins = int(p1wins)
    p1games = int(p1games) + 1
    p2games = int(p2games) + 1
    p2won_percentage = int((p2wins/p2games)*100)
    p1won_percentage = int((p1wins/p1games)*100)
    while not process_events():
        # Clear Screen
        screen.blit(eindscherm,[0,0])
        button (screen,text2.text,395,358,124,50,bright_grey,bright_grey,1,1,26)
        button (screen,"Quit",190,561,278,50,dark_red,red,0,0,26, quitgame)

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
    read_all()
    #printing scores on screen
    '''highscore = download_scores()     
    
    player_highscores = []
    player_highscores.append(highscore[0][0] + "   "  + str(highscore[0][1]) + "   " + str(highscore[0][2]) + "   " + str(highscore[0][3]) + "\n")
    player_highscores.append(highscore[1][0] + "   "  + str(highscore[1][1]) + "   " + str(highscore[1][2]) + "   " + str(highscore[1][3]) + "\n")
    player_highscores.append(highscore[2][0] + "   "  + str(highscore[2][1]) + "   " + str(highscore[2][2]) + "   " + str(highscore[2][3]) + "\n")
    player_highscores.append(highscore[3][0] + "   "  + str(highscore[3][1]) + "   " + str(highscore[3][2]) + "   " + str(highscore[3][3]) + "\n")
    player_highscores.append(highscore[4][0] + "   "  + str(highscore[4][1]) + "   " + str(highscore[4][2]) + "   " + str(highscore[4][3]) + "\n")
    

    font = pygame.font.Font(None,70)
    score_text = font.render(player_highscores[0],1,(255,255,255))
    
    #start PyGame
    pygame.init()'''


    while not process_events():
        # Clear Screen
        screen.blit(radar,[0,0])
        
        #TESTBUTTON
        button (screen,"Back",20,650,100,50,grey,bright_grey,0,0,20, program)
        
       
        
        #Flip the screen
        pygame.display.flip()

def mute():
    global volume
    volume = 0
    pygame.mixer.music.set_volume(0)
def vijfentwintig():
    global volume
    volume = 0.25
    pygame.mixer.music.set_volume(0.25)
def vijftig():
    global volume
    volume = 0.50
    pygame.mixer.music.set_volume(0.50)
def vijfenzeventig():
    global volume
    volume = 0.75
    pygame.mixer.music.set_volume(0.75)
def honderd():
    global volume
    volume = 1
    pygame.mixer.music.set_volume(1)


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
        circle (screen,445,218,10,20,20,green,bright_green,0,1, mute)
        circle (screen,540,218,10,20,20,green,bright_green,0,1, vijfentwintig)
        circle (screen,640,218,10,20,20,green,bright_green,0,1,vijftig)
        circle (screen,741,218,10,20,20,green,bright_green,0,1,vijfenzeventig)
        circle (screen,842,218,10,20,20,green,bright_green,0,1,honderd)
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


def create_table():
    conn = sqlite3.connect('battleport.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS scores(pname TEXT, games_won INT, games_played INT, won_percentage INT)')
    conn.commit()
    c.close()
    conn.close()

def read_all():
    conn = sqlite3.connect('battleport.db')
    c = conn.cursor()
    c.execute("SELECT * FROM scores ORDER BY won_percentage DESC")
    for row in c.fetchall():
        naam = str(row[0])
        wins = str(row[1])
        games = str(row[2])
        percentage = str(row[3])
        global reps
        hoogte_score = 50+(reps*50)
        reps = reps + 1
        button(screen,"Naam: "+naam+"   totaal aantal wins: "+wins+"   totaal aantal games: "+games+"   winstpercentage: "+percentage+"%",20,hoogte_score,1000,50,grey,grey,0,0,20)
        print("Naam: "+naam+"   totaal aantal wins: "+wins+"   totaal aantal games: "+games+"   winstpercentage: "+percentage+"%")

def read_from_db():
    conn = sqlite3.connect('battleport.db')
    c = conn.cursor()
    c.execute("SELECT * FROM scores WHERE pname = '"+ text.text + "'")
    for row in c.fetchall():
        global p1wins
        global p1games
        p1wins = row[1]
        p1games = row[2]
        conn.commit()
    c.close()
    conn.close()
    read_from_db2()

def read_from_db2():
    conn = sqlite3.connect('battleport.db')
    c = conn.cursor()
    c.execute("SELECT * FROM scores WHERE pname = '"+ text2.text + "'")
    for row in c.fetchall():
        global p2wins
        global p2games
        p2wins = row[1]
        p2games = row[2]
    conn.commit()
    c.close()
    conn.close()

def data_entry():
    conn = sqlite3.connect('battleport.db')
    c = conn.cursor()
    c.execute("DELETE FROM scores WHERE pname ='"+ text.text +"'")
    c.execute("DELETE FROM scores WHERE pname='"+text2.text+"'")
    c.execute("INSERT INTO scores (pname, games_won, games_played, won_percentage) VALUES (?, ?, ?, ?)", (text.text, p1wins, p1games, p1won_percentage))
    c.execute("INSERT INTO scores (pname, games_won, games_played, won_percentage) VALUES (?, ?, ?, ?)", (text2.text, p2wins, p2games, p2won_percentage))
    conn.commit()
    c.close()
    conn.close()

'''<<<<<<< HEAD
=======
import psycopg2

#Using Database
def interact_with_database(command):
	#connectie
	connection = psycopg2.connect("dbname=Battleport user=postgres password=h62v5th")
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
	print(results)
		
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
	return interact_with_database("SELECT sname, games_won, games_played, won_percentage FROM scores LIMIT 5")

#Downloads the top score from the database
def download_top_score():
		result = interact_with_database("SELECT * FROM scores ORDER BY scores")[0][1]
		return result

download_scores()							

# Start the program
>>>>>>> origin/master'''
program()
