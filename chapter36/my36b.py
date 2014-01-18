#simple dice rolling game
import random

def dice():
    """Dice, numbers 1 through 6"""
    roll = random.randint(1,6)
    return roll

def roll(numRolls):
    """Returns dice roll in a list"""
    myRolls = []
    for i in range(0,numRolls):
        x = dice()
        myRolls.append(x)
    return myRolls

def getPointTotal(rolls):
    myCount = []
    score = 0
    for i in range(0,7):
        x = rolls.count(i)
        myCount.append(x)
        if x == 3:
            print "3 of a kind!"
            if i == 1:
                i = 3
            score = score + (i * 100)
        elif x == 4:
            print "4 of a kind!"
            score = score + (i * 200)
        elif x == 5:
            print "5 of a kind"
            score = score + (i * 300)  
        elif x == 6:
            print "6 of a kind"
            score = score + (i * 400)                        
    if myCount.count(2) == 3:
        print "Nice Roll, 3 pair!"
        score = score + 1500
    elif myCount.count(4)  == 1 and myCount.count(2) == 1:
        print "scored four of a kind and 2 of a kind"
        score = score + 1500
    
    if myCount[1] < 3 and myCount[1] > 0 and score != 1500:
        print "Scored on 1's"
        score = score + (myCount[1] * 100)
    if myCount[5] < 3 and myCount[5] > 0 and score != 1500:
        print "Scored on 5's"
        score = score + (myCount[5] * 50)
    if myCount[1] == 1 and myCount[2] == 1 and myCount[3] == 1 and myCount[4] == 1 and myCount[5] == 1 and myCount[6] == 1:
        print "You got a straight!"
        score = score + 1500
    elif score == 0:
        print "You failed to score"
    
    return score

def printRoll(rolls):
    x = 0
    for i in rolls:
        x += 1
        print "On roll %s you rolled a %s" % (x, i)              
    

    
myRoll = roll(6)
printRoll(myRoll)
score = getPointTotal(myRoll)
print myRoll

print score

    
