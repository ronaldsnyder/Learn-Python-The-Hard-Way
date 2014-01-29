from Hero import Hero
import Items
import textwrap
import random 

class Monster(Hero):
    """Base Monster Class"""
    def __init__(self):
        super(Monster,self).__init__()
        self.name = 'Monster'
        
    def die(self, hero):
        #each monster needs to drop item and give to hero.
        hero.add_inventory('Healing Potion')
 
 
class Goblin(Hero):
    """The first fight in the arena"""
    def __init__(self):
        super(Goblin,self).__init__()
        self.name = 'Garbanzo'
        self.availhp = 150
        self.description = """
        Welcome to the Arena our first Legion of Hell member, %s.  This is this goblins 
        first fight in the Arena.
        
        %s looks weak and scared\n""" % (self.name, self.name)
        
        print textwrap.dedent(self.description)
        
    def die(self, hero):
        #each monster needs to drop item and give to hero.
        hero.add_inventory('Healing Potion')
        
        hero.add_weapon(Items.weapon['Sword'])
        hero.add_armor(Items.armor['Leather Armor'])
    
    def talk_smack(self):
        sayings = ["Yooo loook delishous!",
                   "Me thinks yous will look in a stew!",
                   "Me got easy fight for first in arena!",
                   "Me family is gonna feast on yous at sunrise!",
                   "Carrots, Onions and YOOOUS, mmmmmm",
                   "Me sword is gonna dance on yous head",
                   "Me only have to kill yous to pay me debt for stealin' little uns",
                   "Yous sword is brittle as yous bones!",
                   "Me only wanted to eat",
                   "Me not sorry, me HUNGRY!"]
        say = random.randint(0,10)
        print "%s says:" % self.name
        print '%s \n ' % sayings[say]

class Warrior(Hero):
    """The first fight in the arena"""
    def __init__(self):
        super(Warrior,self).__init__()
        self.name = 'Bull'
        self.availhp = 150
        self.description = """
        The second fight is a veteran of the Arena named %s.
        
        %s looks like a formidable opponent who has the scars to prove his experience""" % (self.name, self.name)
        
        print self.description
        
    def die(self, hero):
        #each monster needs to drop item and give to hero.
        hero.add_inventory('Healing Potion')
        
        hero.add_weapon(Items.weapon['Battle Axe'])
        hero.add_armor(Items.armor['Chain Armor'])
        
    def talk_smack(self):
        sayings = ["I will crush your face with my fist!",
                   "I have fought 100 battles against better men than you!",
                   "Take a knee and I promise to not let you suffer!",
                   "I can smell your fear of me",
                   "There is more blood dried on my weapon than in your body",
                   "That sword looks like it tickles.",
                   "FREEEEEEEEEEEDOOOOOOOOOOOOOOOOM",
                   "Maximus was a sisssy",
                   "Rebels only win in Star Wars",
                   "Rebel,  I am your father....HAHAHA, not really."]
        say = random.randint(0,10)
        print "%s says:" % self.name
        print '%s \n ' % sayings[say]  