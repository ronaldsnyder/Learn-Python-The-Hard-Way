#Name:    my36.py
#Date:    1/15/2014
#Author:  Ron Snyder
#Purpose: Project for the first 36 chapters of LPTHW
from sys import exit
import random

def fight():
    life = random.randint(1,10)
    return life

def start():
    print """
    You enter the underground dungeon and find a room 
    to your right, left and straight ahead.  
    
    What do you do?
    
    1.  Straight
    2.  Left
    3.  Right
    4.  Go back
    """
    next = raw_input("> ")
    
    next = int(next)
    
    if next == 1:
        horse_room()
    elif next == 2:
        duck_room()
    elif next == 3:
        die("You fall into an abyss")
    elif next == 4:
        print ("You turn around to walk out the door")
        die("Savages attack you as soon as you walk out the door")
        
    else:
        die("You are too drunk to walk and passout.  The rodents eat your toes off.")
 
def die(text):
    print text
    print "You die a horrible death."
    exit(0) 
     
def horse_room():
    print """
    You enter a room with 100 duck sized horses.  These horses
    start rearing up and charging.  What do you do?
    
    1.  Turn around and run!
    2.  Fight them!
    """
    
    next = raw_input("> ") 
    
    next = int(next)
    if next == 1:
        die("You can't out run horses in short distances.......")
    elif next == 2:
        print "You ready yourself to fight the horses and win."
        result = fight()
        if result > 5:
            print """
    		You defeat all of the horses and grab the fabled golden saddle
    		and return to the starting room as there are no more doors in 
    		this room."""
            start();
        else:
            die("You are overcome by all the horses")
    
    else:
        die("The horses quickly overwhelm you because of your indecision")
 
def duck_room():
    print """
 	You enter a room with 100 horse sized ducks.  These ducks start quacking and 
 	getting in the v formation.  What do you do?
 	
 	1.  Turn around and run!
	2.  Fight them!
	3.  Hold you ground!
	"""
    
    next = raw_input("< ") 
    
    next = int(next)
    
    if next == 1:
        die("You slip on duck poop.  This isn't pretty.")
        
    elif next == 2:
        print "You ready yourself to fight the ducks."
        result = fight()
        if result > 7:
            print """
    		After a long and horrible fight you have beaten the 100 duck sized horses.
    		All you find in the room is a bunch of huge duck poop. You return to the starting
    		room and as there is nowhere else to go."""
            start()
        else:
            die("The ducks peck your eyes out and leave you lying there.")
    elif next == 3:
        print "The ducks just wander around and are completely harmless"
        start()
    else:
        die("The ducks quickly over come you because your indecision")
start()	   