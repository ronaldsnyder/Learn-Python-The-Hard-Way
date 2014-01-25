#Hero Class for Miz's adventure

import Items
from Weapon import Weapon
import Armor

class Hero(object):
    def __init__(self):
        #self stats
        self.name = 'Miz'
        self.hp = 200
        self.health = self.hp
        self.attack = 10
        self.weapon = 0
        self.armor = 0
        
        #intangibles 
        self.inventory = ["Healing Potion"]
        self.wallet = 0
        
        
    def attack(self, weapon):
        pass
    
    def add_inventory(self, item):
        #thinking of a dictionary holding a list
        pass
    
    def add_weapon(self, myWeapon):
        #probably need to check if weapon exists
        #delete the amount of attack it has from attack
        self.weapon = Weapon(myWeapon)
        self.attack = self.attack + self.weapon.attack
        
    def add_armor(self, myArmor):
        #probably need to check if armor exists
        #delete the amount of armor the old armor adds
        #delete the amount of hp the old armor adds
        self.armor = Armor(myArmor)
        self.armor = self.armor + self.armor.defense
        self.hp = self.hp + self.armor.bonusHP
    
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
        
    
#tests
 
myHero = Hero()

#mw = Items.weapon["Rusty Sword"]

#print mw[0]

print myHero.attack

myHero.add_weapon(Items.weapon["Rusty Sword"])

print myHero.attack


   
    