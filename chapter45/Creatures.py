from Hero import Hero

class Monster(Hero):
    """Base Monster Class"""
    def __init__(self):
        super(Monster,self).__init__()
        self.name = 'Monster'
        
    def die(self, hero):
        #each monster needs to drop item and give to hero.
        hero.add_inventory('Healing Potion')
    