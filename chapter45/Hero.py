#Hero Class for Miz's adventure

import Items
import random
from Weapon import Weapon
from Armor import Armor

class Hero(object):
    def __init__(self):
        #self stats
        self.name = 'Miz'
        self.maxhp = 200
        self.availhp = self.maxhp
        self.attack = 10
        self.defense = 10
        self.weapon = 0
        self.armor = 0
        self.level = 1
        
        #intangibles 
        self.inventory = ["Healing Potion"]
        self.wallet = 0
        
        
    def strike(self, enemy):
        #can miss
        #can crit hit
        damage = random.randint(1,self.attack)
        #we need to take into account enemy armor or avoidance
        #need to define an enemy class to complete
        
        return damage   
    
    def add_inventory(self, item):
        self.inventory.append(item[0])
    
    def print_inventory(self):
        for item in self.inventory:
            myItem = Items.heal[item]
            print "%s: %s" % (myItem[0], myItem[3])
            
    def add_weapon(self, myWeapon):
        #if weapon exists subtract to get back to base stats
        if self.weapon != 0:
            self.attack = self.attack - self.weapon.attack
        self.weapon = Weapon(myWeapon)
        self.attack = self.attack + self.weapon.attack
        
    def add_armor(self, myArmor):
        #if armor exits subtract to get back to base stats.
        if self.armor != 0:
            self.defense = self.defense - self.armor.defense
            self.maxhp = self.maxhp - self.armor.bonusHP           
        self.armor = Armor(myArmor)
        self.defense = self.defense + self.armor.defense
        self.maxhp = self.maxhp + self.armor.bonusHP
    
    
    def heal(self, amount):
        if self.availhp <= self.maxhp + amount[1]:
            self.availhp = self.availhp + amount[1]
        else:
            print 'full heal'
            self.availhp = self.maxhp
        print "The %s healed to %s" % (self.name, self.availhp)
        
    

   
    