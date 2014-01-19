# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# dog class extending Animal
class Dog(Animal):
    
    def __init__(self, name):
        #assign name for dog
        self.name = name
    
    def bark(self):
        print "Ruff, Ruff"
        
#cat class extending Animal
class Cat(Animal):
    #assign name for cat
    def __init__(self, name):
        self.name = name
    
    def meow(self):
        print "Meow, meow"

#Person Class
class Person(object):
    
    def __init__(self, name):
        #assign person name
        self.name = name
        
        #person has some kind of pet
        self.pet = None
        
#employee class extending Person
class Employee(Person):
    
    def __init__(self, name, salary):
        #call the person constructor
        super(Employee, self).__init__(name)
        #assign salary to new Employee
        self.salary = salary
        
# Fish Class
class Fish(object):
    
    def swim(self):
        print "I am swimming"

#Salmon class extending Fish
class Salmon(Fish):
    def swim(self):
        print "Salmon swim up river"

#Halibut class extending Fish
class Halibut(Fish):
    pass

#rover is a dog
rover = Dog("Rover")

#satan is a cat
satan = Cat("Satan")

#Mary is a person
mary = Person("Mary")

#Frank is an employee
frank = Employee('Frank', 120000)

##Frank has a Pet
frank.pet = rover

#Flipper is a fish
flipper = Fish()
flipper.swim()

#crouse is a salmon
crouse = Salmon()
crouse.swim()

#Harry is a halibut
harry = Halibut()
harry.swim()