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
        first fight in the Arena.  The goblin was caught stealing from the Kings market
        and has been training under the watchful eye of the Kingdom for the last six
        months.
        
        %s looks weak and scared.\n""" % (self.name, self.name)
        
        print textwrap.dedent(self.description)
        
    def die(self, hero):
        #each monster needs to drop item and give to hero.
        print '%s falls and says "Meees only wanted to feed mees family \n' % (self.name)
        print '%s has died' % (self.name)
               
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
        say = random.randint(0,9)
        print "%s says:" % self.name
        print '%s \n ' % sayings[say]

class Warrior(Hero):
    """The first fight in the arena"""
    def __init__(self):
        super(Warrior,self).__init__()
        self.name = 'Bull'
        self.availhp = 150
        self.description = """ 
        The second fight is a veteran of the Arena named %s.  He is a perfect 27-0 in 
        the Arena.  He lost his arm in the last battle and WON! That isn't keeping Bull
        from fighting another match.
        
        %s looks like a once formidable opponent, he would probably do better with another 
        arm.
        """ % (self.name, self.name)
        
        print textwrap.dedent(self.description)
        
    def die(self, hero):
        #each monster needs to drop item and give to hero.
        hero.add_inventory('Healing Potion')
        
        hero.add_weapon(Items.weapon['Battle Axe'])
        hero.add_armor(Items.armor['Chain Armor'])
        
    def talk_smack(self):
        sayings = ["I will crush your face with my stub arm!",
                   "I have fought 27 battles against better men than you!",
                   "Take a knee and I promise to not let you suffer!",
                   "I could beat you with one arm tied behind my back, AHAHAHHAHA",
                   "Want to touch my stub?",
                   "You are my last fight, I need your ARM!",
                   "I don't need two arms to kill a traitor.",
                   "The kingdom promised my release after I kill you.",
                   "I am going to take your arm when this fight is over, HAHAHAHAHA",
                   "Your children will be disappointed to hear you were killed by a one armed man."]
        say = random.randint(0,9)
        print "%s says:" % self.name
        print '%s \n ' % sayings[say]  