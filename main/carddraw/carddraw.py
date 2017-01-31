import random

#Class

class card:
    def __init__ (self, name, id, desc,amount,simg,bimg):
        self.name = name
        self.id = id
        self.desc = desc
        self.amount= amount
        self.simg = simg
        self.bimg = bimg
        
#imgfiles

fmj_small                   = pygame.image.load('Kaart_FMJ.png')
fmj_big                     = pygame.image.load('Kaart_FMJ_groot.png')
rifling_small               = pygame.image.load('Kaart_rifling.png')    
rifling_big                 = pygame.image.load('Kaart_rifling_groot.png')
advanced_rifling_small      = pygame.image.load('Kaart_adv_rifling.png')
advanced_rifling_big        = pygame.image.load('Kaart_adv_rifling_groot.png')
emp_upgrade_small           = pygame.image.load('Kaart_EMP.png')
emp_upgrade_big             = pygame.image.load('Kaart_EMP_groot.png')
reinforced_hull_small       = pygame.image.load('Kaart_reinf_hull.png')
reinforced_hull_big         = pygame.image.load('Kaart_reinf_hull_groot.png')
sonar_small                 = pygame.image.load('Kaart_sonar.png')
sonar_big                   = pygame.image.load('Kaart_sonar_groot.png')
smokescreen_small           = pygame.image.load('Kaart_smoke.png')
smokescreen_big             = pygame.image.load('Kaart_smoke_groot.png')
sabotage_small              = pygame.image.load('Kaart_sabotage.png')
sabotage_big                = pygame.image.load('Kaart_sabotage_groot.png')
backup_small                = pygame.image.load('Kaart_backup.png')
backup_big                  = pygame.image.load('Kaart_backup_groot.png')
extra_fuel_small            = pygame.image.load('Kaart_fuel.png')
extra_fuel_big              = pygame.image.load('Kaart_fuel_groot.png')
extra_fuel2_small           = pygame.image.load('Kaart_fuel_2.png')
extra_fuel2_big             = pygame.image.load('Kaart_fuel_2_groot.png')
rally_small                 = pygame.image.load('Kaart_rally.png')
rally_big                   = pygame.image.load('Kaart_rally_groot.png')
nuclear_small               = pygame.image.load('Kaart_nuclear.png')
nuclear_big                 = pygame.image.load('Kaart_nuclear_groot.png')
repair_small                = pygame.image.load('Kaart_repair.png')
repair_big                  = pygame.image.load('Kaart_repair_groot.png')
far_sight_small             = pygame.image.load('Kaart_far_sight.png')
far_sight_big               = pygame.image.load('Kaart_far_sight_groot.png')
aluminium_hull_small        = pygame.image.load('Kaart_aluminium_hull.png')
aluminium_hull_big          = pygame.image.load('Kaart_aluminium_hull_groot.png')



#Create card instance

#Offensive
fmj_upgrade = card("FMJ Upgrade",0,"When this card is used, your next shot does +1 damage.",2,fmj_small,fmj_big)
rifling = card("Rifling",1,"When this card is used, your next shot has +1 range.",2,rifling_small,rifling_big)
advanced_rifling = card("Advanced Rifling",2,"When this card is used, your next shot has +2 range.",2,advanced_rifling_small,advanced_rifling_big)
emp_upgrade = card("EMP Upgrade", 3, "When this card is used, your shot will disable the movement and attack of the ship(s) that got hit for 1 turn.",4,emp_upgrade_small,emp_upgrade_big)

#defensive
reinforced_hull = card("Reinforced Hull",4,"Adds one HP to a friendly ship of your choice when this card is played.",2,reinforced_hull_small,reinforced_hull_big)
sonar = card("Sonar",5,"Choose a potential mine location to spot and deactivate that mine and place it in the discarded deck.",4,sonar_small,sonar_big)
smokescreen = card("Smokescreen",6,"When a friendly ship gets attacked, you may activate this card to make the attack miss.",2,smokescreen_small,smokescreen_big)
sabotage = card("Sabotage",7,"When activated, your opponent's attack deals damage to its own ship.",2,sabotage_small,sabotage_big)

#Utility
backup = card("Backup",8,"Draw two cards.",2,backup_small,backup_big)
extra_fuel = card("Extra Fuel",9,"Select a friendly ship to make it move +1 step.",6,extra_fuel_small,extra_fuel_small)
extra_fuel2 = card("Extra Fuel II",10,"Select a friendly ship to make it move +1 step.",4,extra_fuel2_small,extra_fuel2_big)
rally = card("Rally",11,"All friendly ships van move +1 step.",1,rally_small,rally_big)
nuclear = card("Nuclear",12,"Select a friendly ship to make its moveset x2.",4,nuclear_small,nuclear_big)

#Special cards
repair = card("Repair", 13, "Select a friendly ship to fully heal this ship (Base HP).",2,repair_small,repair_big)
far_sight = card ("Far Sight", 14, "The used ship now has +2 range.",1,far_sight_small,far_sight_big)
aluminium_hull = card("Aluminium Hull",15,"The used ship now has its moveset x2.",1,aluminium_hull_small,aluminium_hull_big)



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
