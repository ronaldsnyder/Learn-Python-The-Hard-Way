class Armor(object):
    """Some Armor"""
    
    def __init__(self, armor):
        
        self.name = armor[0]
        self.defense = armor[1]
        self.cost = armor[2]
        self.bonusHP = armor[3]
        self.description = armor[4]
        
        
    def description(self):
        print self.description