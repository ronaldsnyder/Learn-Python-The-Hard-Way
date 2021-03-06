#Hero Class for Miz's adventure

import Items
import random
from Weapon import Weapon
from Armor import Armor
import textwrap

import os
clear = lambda: os.system('clear')

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
        self.super = True
        
        self.description ="""
        Today's challenger is from the rebellion.  He was caught trying to free 
        the slaves from the cities dungeon.  %s is the worst kind of rebel as he
        is also a traitor.  He was born, trained and one of the Kingdoms most 
        loyal soldiers up until he deserted at the Battle of Big Littlehorn.
        
        """ % self.name
        
        #intangibles 
        self.inventory = ["Healing Potion"]
        
        
        
        
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
        
        return damage
    
    def super_strike(self, enemy):
        if self.super:
            print "POWER ATTACK!  \n%s strikes with determination and anger.\n" % self.name
            
            i = random.randint(0,4)
            say = ['By the power of Greyskull, I HAVE THE POWER',
                   "Say hello to my little friend",
                   "Hello, my name is Inigo Montoya. You killed my father. Prepare to die.",
                   "I have come here to chew bubblegum and kick ass, and I'm all out of bubblegum",
                   "You've gotta ask yourself a question: do I feel lucky? ...well, do ya, punk?!?"]
            print '%s says "%s"\n' % (self.name, say[i])
            
            damage = random.randint(10,self.attack) + self.attack
            self.super = False
            return damage
        else:
            self.strike(enemy)
        
        
        
    
    def kick(self):
        #kick has a 25 percent chance to miss
        hit = random.randint(0,4)
        
        if hit > 0:      
            damage = random.randint(0,10)
        else:
            damage = 0
            
        return damage    
    
    def add_inventory(self, item):
        self.inventory.append(item)
    
    def print_inventory(self):
        for item in self.inventory:
            myItem = Items.heal[item]
            print "%s: %s" % (myItem[0], myItem[3])
            
            
    
    def use_item(self):
        #for item in self.inventory:
            #myItem = Items.heal[item]
            #print "%s: %s" % (myItem[0], myItem[3])
        print '\t*********ITEM LIST**********'    
        for (counter, item) in enumerate(self.inventory):
            myItem = Items.heal[item]
            #print counter, item
            print "\t%s.  %s: %s" % (counter + 1, myItem[0], myItem[3])
        
        #need to make sure choice is an int
        choice = raw_input('\nSelect item to use: ')
        
        try:
            choice = int(choice) - 1
            valid = True
        except:
            clear()
            valid = False
            print 'Please enter a number, try again: '
            self.use_item()
            
        #make sure the choice is an index in the item list
        if (choice >= len(self.inventory)  or choice < 0):
            valid = False    
            
        if valid:
            myItem = self.inventory[choice]
            self.heal(Items.heal[myItem]) 
            self.inventory.remove(myItem)
        else:
            clear()
            print 'Invalid Choice, try again'
            self.use_item()

            
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
        if self.maxhp <= self.availhp + amount[1]:
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

    def introduction(self):
        print textwrap.dedent(self.description)