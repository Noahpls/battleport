import random

#Class

class card:
    def __init__ (self, name, id, desc,amount):
        self.name = name
        self.id = id
        self.desc = desc
        self.amount= amount

#Create card instance

#Offensive
fmj_upgrade = card("FMJ Upgrade",1,"When this card is used, your next shot does +1 damage.",2)
rifling = card("Rifling",2,"When this card is used, your next shot has +1 range.",2)
advanced_rifling = card("Advanced Rifling",3,"When this card is used, your next shot has +2 range.",2)
naval_mine = card("Naval Mine",4,"Activates the mine with coordinate X,Y.",6)
emp_upgrade = card("EMP Upgrade", 5, "When this card is used, your mine or shot will disable the movement and attack of the ship(s) that got hit for 1 turn.",4)

#defensive
reinforced_hull = card("Reinforced Hull",6,"Adds one HP to a friendly ship of your choice when this card is played.",2)
sonar = card("Sonar",7,"Choose a potential mine location to spot and deactivate that mine and place it in the discarded deck.",4)
smokescreen = card("Smokescreen",8,"When a friendly ship gets attacked, you may activate this card to make the attack miss.",2)
sabotage = card("Sabotage",9,"When activated, your opponent's attack deals damage to its own ship.",2)

#Utility
backup = card("Backup",10,"Draw two cards.",2)
extra_fuel = card("Extra Fuel",11,"Select a friendly ship to make it move +1 step.",6)
extra_fuel2 = card("Extra Fuel II",12,"Select a friendly ship to make it move +1 step.",4)
rally = card("Rally",13,"All friendly ships van move +1 step.",1)
adrenaline_rush = card("Adrenaline Rush",14,"Select a friendly ship to make its moveset x2.",4)

#Special cards
repair = card("Repair", 15, "Select a friendly ship to fully heal this ship (Base HP).",2)
flak_armor = card("Flak Armor", 16, "Ship becomes immune to mines.", 2)
hack_intel = card("Hack Intel", 17, "Reveal the three cards in the special deck.",1)
far_sight = card ("Far Sight", 18, "The used ship now has +2 range.",1)
aluminium_hull = card("Aluminium Hull",19,"The used ship now has its moveset x2.",1)
jack_sparrow = card("Jack Sparrow",20,"Reveal opponent's hand, choose 1 of his cards and discard another 1.",1) 



def carddraw():
    r = random.randint(1,20)
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
        
            if naval_mine.amount == 0:
                foundcard = 0
            else:
                naval_mine.amount = naval_mine.amount - 1
                foundcard = 1
                activecard = naval_mine
                return activecard

        elif r == 5:
        
            if emp_upgrade.amount == 0:
                foundcard = 0
            else:
                emp_upgrade.amount = emp_upgrade.amount - 1
                foundcard = 1
                activecard = emp_upgrade
                return activecard

        elif r == 6:
        
            if reinforced_hull.amount == 0:
                foundcard = 0
            else:
                reinforced_hull.amount = reinforced_hull.amount - 1
                foundcard = 1
                activecard = reinforced_hull
                return activecard

        elif r == 7:
        
            if sonar.amount == 0:
                foundcard = 0
            else:
                sonar.amount = sonar.amount - 1
                foundcard = 1
                activecard = sonar
                return activecard
       
        elif r == 8:
        
            if smokescreen.amount == 0:
                foundcard = 0
            else:
                smokescreen.amount = smokescreen.amount - 1
                foundcard = 1
                activecard = smokescreen
                return activecard

        elif r == 9:
        
            if sabotage.amount == 0:
                foundcard = 0
            else:
                sabotage.amount = sabotage.amount - 1
                foundcard = 1
                activecard = sabotage
                return activecard

        elif r == 10:
        
            if backup.amount == 0:
                foundcard = 0
            else:
                backup.amount = backup.amount - 1
                foundcard = 1
                activecard = backup
                return activecard

        elif r == 11:
        
            if extra_fuel.amount == 0:
                foundcard = 0
            else:
                extra_fuel.amount = extra_fuel.amount - 1
                foundcard = 1
                activecard = extra_fuel
                return activecard

        elif r == 12:
        
            if extra_fuel2.amount == 0:
                foundcard = 0
            else:
                extra_fuel2.amount = extra_fuel2.amount - 1
                foundcard = 1
                activecard = extra_fuel2
                return activecard

        elif r == 13:
        
            if rally.amount == 0:
                foundcard = 0
            else:
                rally.amount = rally.amount - 1
                foundcard = 1
                activecard = rally
                return activecard

        elif r == 14:
        
            if adrenaline_rush.amount == 0:
                foundcard = 0
            else:
                adrenaline_rush.amount = adrenaline_rush.amount - 1
                foundcard = 1
                activecard = adrenaline_rush
                return activecard

        elif r == 15:
        
            if repair.amount == 0:
                foundcard = 0
            else:
                repair.amount = repair.amount - 1
                foundcard = 1
                activecard = repair
                return activecard

        elif r == 16:
        
            if flak_armor.amount == 0:
                foundcard = 0
            else:
                flak_armor.amount = flak_armor.amount - 1
                foundcard = 1
                activecard = flak_armor
                return activecard

        elif r == 17:
        
            if hack_intel.amount == 0:
                foundcard = 0
            else:
                hack_intel.amount = hack_intel.amount - 1
                foundcard = 1
                activecard = hack_intel
                return activecard

        elif r == 18:
        
            if far_sight.amount == 0:
                foundcard = 0
            else:
                far_sight.amount = far_sight.amount - 1
                foundcard = 1
                activecard = far_sight
                return activecard

        elif r == 19:
        
            if aluminium_hull.amount == 0:
                foundcard = 0
            else:
                aluminium_hull.amount = aluminium_hull.amount - 1
                foundcard = 1
                activecard = aluminium_hull
                return activecard

        elif r == 20:
        
            if jack_sparrow.amount == 0:
                foundcard = 0
            else:
                jack_sparrow.amount = jack_sparrow.amount - 1
                foundcard = 1
                activecard = jack_sparrow
                return activecard
