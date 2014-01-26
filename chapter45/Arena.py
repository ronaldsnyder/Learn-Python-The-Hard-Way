class Arena(object):
    def __init__(self):
        self.description = """Welcome to King Reprecht's Arena!  To punish the rebellion scums
        the Legion of Hell will fight everyone to the DEATH! """
        
        
    
    def fight(self,hero, monster):
        #hero strikes first.
        pass
        #monsters each have unique fight style.
        
        
    
    def menu(self,hero ,monster):
        print """
        1. Strike with weapon
        2. Cast Spell
        3. Use Item """
        
        answer = raw_input("Select your action")
        
        if answer == 1:
            hero.strike(monster)
            
        elif answer == 2:
            pass 
        
        elif answer == 3:
            for (counter, item) in enumerate(hero.inventory):
                print counter, item
                menu = {counter: item}
                
            answer = raw_input(menu)
            
            #need a way for her to use heal items.  We are printing the name, need to get item and use it.
                
            