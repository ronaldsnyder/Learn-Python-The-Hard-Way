#Hero Class for Miz's adventure

import Items

class Hero(object):
    def __init__(self):
        #self stats
        self.name = 'Miz'
        self.hp = 200
        self.health = self.hp
        self.attack = 10
        
        #intangibles 
        self.inventory = ["Healing Potion"]
        self.wallet = 0
        
        #armor
        self.weapon = 'sw1'
        self.armor  = 'car'
        
        def attack(self, weapon):
            pass
        
        def add_inventory(self, item):
            #thinking of a dictionary holding a list
            pass
        
        def add_weapon(self, weapon):
            #thinking of a dictionary holding a list
            pass
        
        def damage(self, amount, attack_type):
            #amount of damage mitigated by armor and type of attack
            pass
        
        def heal(self, amount):
            if self.health <= self.hp + amount:
                self.health = self.health + amount
                print "Full Heal"
            else:
                self.health = self.hp
            print "The %s healed to %s" % (self.name, self.hp)
        
    
    
    