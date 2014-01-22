import random
from sys import exit

class Hero(object):
    def __init__(self):
        self.hp = 12.5
        self.mp = 20
        self.strength = 15
        self.wisdom = 15        
        self.weapon = 'baseball bat'
    
    def weapon_attack(self):
        #damage = random.randint(0,10)
        damage = 5
        if damage < 1:
            damage = 0
            print "%s miss with the %s" % self.weapon
        elif damage == 10:
            damage = self.strength * random.randint(4,8) + random.randint(0,10)
            print "%s critically hit with the %s for %s" % (self.name, self.weapon, damage)
        else:
            damage = self.strength * random.randint(1,2) + damage
            print "%s hit with the %s for %s" % (self.name, self.weapon, damage)
        return damage;
    
    def hurt(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.die()
        else:
            print "%s has taken %s damage and has %s health remaining" % (self.name, damage, self.hp)
    
    def die(self):
        print "%s has died, good job" %self.name
        exit(1)

class Mage(Hero):
    def __init__(self):
        self.name = "Marlin"
        self.weapon = 'staff'
        
        self.hp = 100
        self.mp = 200
        self.strength = 5
        self.wisdom = 25
        
class Fighter(Hero):
    def __init__(self):
        self.name = "Miz"
        self.weapon = 'Sword'
        
        self.hp = 200
        self.mp = 100
        self.strength = 25
        self.wisdom = 5
            
maz = Mage();
miz = Fighter()

while True:
    miz.hurt(maz.weapon_attack())
    maz.hurt(miz.weapon_attack())    
        
        

        