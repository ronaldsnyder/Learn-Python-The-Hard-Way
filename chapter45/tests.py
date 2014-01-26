from Hero import Hero
from Creatures import Monster
from Weapon import Weapon
from Armor import Armor
import Items

#tests
 
myHero = Hero()

myMonster = Monster()

amount = myHero.strike(myMonster)
print amount
myMonster.damage(amount)