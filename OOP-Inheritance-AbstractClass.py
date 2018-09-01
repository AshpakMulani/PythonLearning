###########################################################################################
# This is continuation  of script OOP-Inheritance.
# Abstract class can not be instantiated, but can can be subclassed.
# Subclasses does not need to implement __init__ method if inheriting from abstract class
# Abstract class is defined normally but it only contains constructor and method definitions (mainly)
# if we want we can also define and implement in abstract class itself.
# with logic to raise exception if any method is getting called using class object
# Abstract class is only designed to serve as a base class/ template. Inherited class finally
# is free to implement any abstract class method or any new method the way it wants.
###########################################################################################

class Animal():
    species = 'Mammal'
    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        raise NotImplementedError("This abstract method can not be instantiated")
        # raising exception if any class object trying to invoke it, since this is abstract class.

    def speak(self, volume):
        raise NotImplementedError("This abstract method can not be instantiated")

    def eat(self):
        print("I am eating..!!!")  # we can implement few methods in base class as well.

class Dog(Animal):
    # here we are not implementing separate __init__ for this class because we want to treat this class
    # as extension to base class instead if having own identity.
    # It is not mandatory for inherited class to implement all methods from base class.

    def who_am_i(self): # this inherited class is now implementing methods from base class.
        print(f"I am {self.species} dog...My name is {self.name}!!!")
        # here self. is treating Dog and Animal as same class.

class Cat(Animal):

    def who_am_i(self):
        print(f"I am {self.species} cat...My name is {self.name}!!!")

    def speak(self, volume):  # while implementing function from base class it should exactly match
                              # definition from base class otherwise this method will be treated
                              # as separate method inside inherited class.
        print(f"Meow....Meow..!!! I am {volume}")


mydog = Dog("Mikky")  # eben though there is no constructor in Dog class, it is using constructor
                        # of base class and asking name as parameter.
mydog.who_am_i()
mydog.eat()
# mydog.speak() If we try to invlike thi methot it will give NotImplimented error. since there is no
# implimentation of this method in inherited class

mycat = Cat("Sheru")
mycat.who_am_i()
mycat.speak('loud')
mycat.eat()