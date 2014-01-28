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
        self.attack = 30
        self.defense = 5
        self.weapon = 0
        self.armor = 0
        self.level = 1
        
        #intangibles 
        self.inventory = ["Healing Potion"]
        self.wallet = 0
        
        
    def strike(self, enemy):
        #hit roll
        
        hit = random.randint(0,8)

        if hit == 0:
            print "A wild attack from %s misses" % self.name
            damage = 0
            
        elif hit == 8:
            print "CRITICAL HIT FOR %s" % self.name
            damage = random.randint(10,self.attack) + self.attack - enemy.defense
            
        else:
            damage = random.randint(5,self.attack) - enemy.defense
        
        if damage < 0:
            damage = 0
            print "%s armor absorbed the hit" %enemy.name
            
        #if damage < enemy.defense:
            #damage = 0
            #print "%s armor absorbed the hit" %enemy.name
        
        
        return damage
    
    def kick(self):
        #kick has a 25 percent chance to miss
        hit = random.randint(0,4)
        
        if hit > 0:      
            damage = random.randint(0,10)
        else:
            damage = 0
            
        return damage    
    
    def add_inventory(self, item):
        self.inventory.append(item[0])
    
    def print_inventory(self):
        for item in self.inventory:
            myItem = Items.heal[item]
            print "%s: %s" % (myItem[0], myItem[3])
            
            
    
    def use_item(self):
        for item in self.inventory:
            myItem = Items.heal[item]
            print "%s: %s" % (myItem[0], myItem[3])
            
        for (counter, item) in enumerate(self.inventory):
            myItem = Items.heal[item]
            #print counter, item
            print "%s.  %s: %s" % (counter, myItem[0], myItem[3])
        
        #need to make sure choice is an int
        choice = raw_input('select item to use ')
        
        myItem = self.inventory[int(choice)]
        self.heal(Items.heal[myItem]) 
        self.inventory.remove(myItem)

            
    def add_weapon(self, myWeapon):
        #if weapon exists subtract to get back to base stats
        if self.weapon != 0:
            self.attack = self.attack - self.weapon.attack
        self.weapon = Weapon(myWeapon)
        self.attack = self.attack + self.weapon.attack
        
        print "%s equips a %s" % (self.name, self.weapon.description)
        
    def add_armor(self, myArmor):
        #if armor exits subtract to get back to base stats.
        if self.armor != 0:
            self.defense = self.defense - self.armor.defense
            self.maxhp = self.maxhp - self.armor.bonusHP           
        self.armor = Armor(myArmor)
        self.defense = self.defense + self.armor.defense
        self.maxhp = self.maxhp + self.armor.bonusHP
        
        print "%s equips some %s" % (self.name, self.armor.description)
    
    
    def heal(self, amount):
        if self.availhp >= self.maxhp + amount[1]:
            self.availhp = self.availhp + amount[1]
        else:
            print 'full heal'
            self.availhp = self.maxhp
        print "The %s healed to %s" % (self.name, self.availhp)
       
    def damage(self, amount):
        #if amount > self.availhp:
            #dead
            #self.die()
        #else:
        self.availhp = self.availhp - amount
        print "%s was hit for %s" % (self.name, amount)
        print "%s has %s hp left \n" % (self.name, self.availhp)
    def die(self):
        "MIZ DIED"

    