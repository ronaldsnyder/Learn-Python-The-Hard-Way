from Creatures import *
from Hero import Hero
import Items
import textwrap 

import os
clear = lambda: os.system('clear')

class Arena(object):
    def __init__(self):
        header = '*' * 75
        self.description = """
        %s
        Welcome to King Ronaldo's Arena!
        
        To punish the rebellion scums the Legion of Hell will fight the recently
        captured rebel to the DEATH! 
        %s""" % (header, header)
        
        
        self.tournament()
        
    def tournament(self):
        #clear anything in the terminal.
        clear()
        
        #instantiate monsters and put them in legion lists
        print textwrap.dedent(self.description)
        
        #first fight
        myMonster = Goblin()
        myHero = Hero()
        myHero.introduction()
        myHero.add_weapon(Items.weapon['Rusty Sword'])
        myHero.add_armor(Items.armor['Cloth Armor'])
        
        self.fight(myHero, myMonster)
        
        #second fight
        self.next_round(myHero)
        
        myMonster = Warrior()
        myMonster.add_weapon(Items.weapon['Battle Axe'])
        myMonster.add_armor(Items.armor['Chain Armor'])
        
        self.fight(myHero, myMonster)
    
    def fight(self,hero, monster):
        monsterAlive = True
        #while monster is not dead
        while monsterAlive:
            #call menu for hero's turn
            self.menu(hero, monster)
            
            #monster damage
            monster.talk_smack()
            hit = monster.strike(hero)
            hero.damage(hit)
            
            if monster.availhp <= 0:
                monster.die(hero)
                monsterAlive = False     
            elif hero.availhp <= 0:
                hero.die()

        
        
    
    def menu(self,hero ,monster):
        myMenu = """
        1. Strike with weapon
        2. Kick with your boot
        3. Use Item """
        
        if hero.super:
            myMenu = myMenu + """\n\t4. Special Attack\n"""
        
        print myMenu
        answer = raw_input("Select your action: ")
        clear()
        
        if answer == "1":
            hit = hero.strike(monster)
            monster.damage(hit)
            
        elif answer == "2":
            hit = hero.kick()
            monster.damage(hit)
        
        elif answer == "3":
            if hero.inventory:
                hero.use_item()
            else:
                print "Your inventory is empty \n"
                self.menu(hero, monster)
                
        elif answer == "4":
            hit = hero.super_strike(monster)
            monster.damage(hit)
            
        else:
            clear()
            print "Invalid Choice, try again"
            self.menu(hero,monster)    
    
                
    def next_round(self, hero):
        
        print '*' * 75
        print '\nThe arena medic heals all of %s injuries' % hero.name
        hero.availhp = hero.maxhp
        hero.super = True