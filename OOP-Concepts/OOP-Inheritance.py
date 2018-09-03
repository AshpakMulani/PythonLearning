###########################################################################################
#Inherintance : Way to form new classes (derived class) with the help of already defined base class
# we use inheritance if we do not want to again impliment same methods defined in base class
# or when we want to avoid implementing redundant methods in different classes.
###########################################################################################

class Animal():

    species = 'Mammal'

    def __init__(self):
        print("Animal Created.")

    def who_am_i(self):
        print("I am animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):  # we are deriving new class from Animal class. This class can use/re-imliment resources from base class.

    def __init__(self, name):
        Animal.__init__(self) # initiating Animal class. This is mandatory because once instance of this class created it should
                          # automatically create instance of base class.
        self.name = name

    def speak(self):
        print("woof...Woof..!!!")

    def eat(self):   # here we are redefining / overwritting method from base class.
                     # for object of this class eat method will use this definition
                     # instead of using definition from base class.
                     # method overwtirring is one of the type of Polymorphism.
        print(f"My Name is {self.name} and i am eating..")

class Cat(Animal): # one more derived class from Animal

    def __init__(self,name):
        Animal.__init__(self)
        self.name=name

    def speak(self):
        print("Meow....Meow..!!")


mydog = Dog("Mikky")
mydog.who_am_i()  # since this is object of derived class it can access methods and variables from base class Animal.
mydog.speak()
mydog.eat()  # this will use overwritten method in dog class instead of using from base class.


mycat = Cat("Sheru")
mycat.who_am_i()  # accessing method from base class
mycat.speak() # accessing method from derived class
mycat.eat() # unlike dog object above this will call method from base class
            # since derived class does not overwrite this method of base class