from Creatures import Monster

class Arena(object):
    def __init__(self):
        self.description = """Welcome to King Reprecht's Arena!  To punish the rebellion scums
        the Legion of Hell will fight everyone to the DEATH! """
        self.Legion = []
        self.tournament()
        
    def tournament(self):
        #instantiate monsters and put them in legion lists
        #for each monster in legion list fight
        myMonster = Monster()
        
    
    def fight(self,hero, monster):
        monsterAlive = True
        #while monster is not dead
        while monsterAlive:
            #call menu for hero's turn
            self.menu(hero, monster)
            
            #monster damage
            hit = monster.strike(hero)
            hero.damage(hit)
            
            if monster.availhp <= 0:
                monster.die()
                monsterAlive = False     
            elif hero.availhp <= 0:
                hero.die()
            
        
        
    
    def menu(self,hero ,monster):
        print """
        1. Strike with weapon
        2. Kick with your boot
        3. Use Item """
        
        answer = raw_input("Select your action")
        
        if answer == 1:
            hit = hero.strike(monster)
            monster.damage(hit)
            
        elif answer == 2:
            pass 
        
        elif answer == 3:
            for (counter, item) in enumerate(hero.inventory):
                print counter, item
                menu = {counter: item}
                
            answer = raw_input(menu)
            
            #need a way for hero to use heal items.  We are printing the name, need to get item and use it.
                
            