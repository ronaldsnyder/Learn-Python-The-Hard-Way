from Hero import Hero
import Items

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
        self.description = """
        Welcome to the Arena our first Legion of Hell member %s.  This is this goblins 
        first fight in the Arena.
        
        %s looks weak and scared""" % (self.name, self.name)
        
        print self.description
        
    def die(self, hero):
        #each monster needs to drop item and give to hero.
        hero.add_inventory('Healing Potion')
        
        hero.add_weapon(Items.weapon['Sword'])
        hero.add_armor(Items.armor['Leather Armor']) 