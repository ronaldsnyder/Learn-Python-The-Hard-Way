import random
from sys import exit

class Hero(object):
    def __init__(self):
        self.health = 200
        self.hp = 200
        self.mp = 20
        self.strength = 15
        self.wisdom = 15        
        self.weapon = 'baseball bat'
    
    def weapon_attack(self):
        damage = random.randint(0,10)
        if damage < 1:
            damage = 0
            print "%s miss with the %s" % (self.name, self.weapon)
        elif damage == 10:
            damage = self.strength * random.randint(4,8) + random.randint(0,10)
            print "%s critically hit with the %s for %s" % (self.name, self.weapon, damage)
        else:
            damage = self.strength * random.randint(1,2) + damage
            print "%s hit with the %s for %s" % (self.name, self.weapon, damage)
        return damage;
    
    def spell(self):
        damage = random.randint(0,10)
        if damage < 1:
            damage = 0
            print "%s misses with a spell" % self.name
        elif damage == 10:
            damage = self.wisdom * random.randint(4,8) + random.randint(0,10)
            print "%s spell critically hits for %s" % (self.name, damage)
        else:
            damage = self.wisdom * random.randint(1,2) + damage
            print "%s hit with the spell for %s" % (self.name, damage)
        return damage;
    
    def hurt(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.die()
        else:
            print "%s has taken %s damage and has %s health remaining" % (self.name, damage, self.hp)
            
    def heal(self, amount):
        if self.health + amount < self.hp:
            self.hp = self.hp + amount
        else:
            self.hp = self.health
            
    def level_up(self, health, strength, wisdom):
        self.health = self.health + health
        self.strength = self.strength + strength
        self.wisdom = self.wisdom + wisdom
        
    def die(self):
        print "%s has died, good job" %self.name
        exit(1)

class Mage(Hero):
    def __init__(self):
        self.name = "Marlin"
        self.weapon = 'staff'       
        self.strength = 5
        self.wisdom = 25

        
class Fighter(Hero):
    def __init__(self):
        self.name = "Miz"
        self.weapon = 'Sword'
        self.strength = 25
        self.wisdom = 5
        self.armor = 25
            
maz = Mage();
miz = Fighter()

while True:
    miz.hurt(maz.spell())
    maz.hurt(miz.weapon_attack())
    
        
        
        

        