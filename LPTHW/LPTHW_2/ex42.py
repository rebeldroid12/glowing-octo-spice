## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## make class Dog that is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## name is-a attribute 
        self.name = name

## make class Cat that is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## from self find name attribute & assign it name
        self.name = name

## make class called Person that is-a object
class Person(object):

    def __init__(self, name):
        ## from self find person attribute name/assign it
        self.name = name

        ## Person has-a pet of some kind
        ## pet attribute
        self.pet = None

        ##
    def shower(self):
        self.clean = True

    def fit(self):
        self.fitness = True

    def fit2(self):
        self.fitness2 = False

## make class Employee that is-a person object
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        ##Get the super-implementation of Employee -- which is a Person object
        ## passing itself as an argument. Afterward, call the __init__ function
        ## of the super implementation using the Employee name argument
        ## basically it gets that name attribute in employee so you dont have to rewrite: self.name = name
        super(Employee, self).__init__(name)

        ##Employee has-a salary attribute and assign it the salary
        ## attribute salary
        self.salary = salary

        super(Employee,self).fit2()

## make class Fish that is-a object
class Fish(object):
    pass

## make class Salmon that is-a Fish
class Salmon(Fish):
    pass

## make class Halibut that is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary is-a person that has-a cat attribute named satan
mary.pet = satan

## frank is-a person that is-a employee that has-a salary attribute 120000
frank = Employee("Frank", 120000)

## frank has-a dog attribute named rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

##frank has-a shower attribute
frank.shower()
print "Is %s clean? %s" % (frank.name, frank.clean)

frank.fit()
frank.fit2()
print "Is %s fit? %s" % (frank.name, frank.fitness)
print "Is %s fit? %s" % (frank.name, frank.fitness2)

mary.fit2()
print "Is %s fit? %s" % (mary.name, mary.fitness2)