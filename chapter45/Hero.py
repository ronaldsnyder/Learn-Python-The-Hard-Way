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
        self.defense = 5
        self.weapon = 0
        self.armor = 0
        self.level = 1
        
        #intangibles 
        self.inventory = ["Healing Potion"]
        self.wallet = 0
        
        
    def strike(self, enemy):
        #can miss
        #can crit hit
        
        #hit roll
        
        hit = random.randint(0,6)

        if hit == 0:
            damage = 0
            
        elif hit == 6:
            print "CRITICAL HIT FOR %s" % self.name
            damage = random.randint(5,self.attack) + self.attack - enemy.defense
            
        else:
            damage = random.randint(5,self.attack) - enemy.defense
            
        if damage < enemy.defense:
            damage = 0
            print "%s armor absorbed the hit" %enemy.name
        
        
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
        
    def damage(self, amount):
        if amount > self.availhp:
            #dead
            print "I should have died"
        else:
            self.availhp = self.availhp - amount
            print "%s was hit for %s" % (self.name, amount)
            print "%s has %s hp left" % (self.name, self.availhp)

   def show_items(self):
    