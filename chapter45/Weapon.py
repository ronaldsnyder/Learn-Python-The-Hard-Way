class Weapon(object):

    def __init__(self, weapon):
        self.name = weapon[0]
        self.attack = weapon[1]
        self.cost = weapon[2]
        self.description = [3]
        
    def description(self):
        print self.description
        
    
    