###########################################################################################
# This is continuation  of script OOP-Inheritance.
# Abstract class can not be instantiated, but can can be subclassed.
# Subclasses does not need to implement __init__ method if inheriting from abstract class
# Abstract class is defined normally but it only contains constructor and method definitions (mainly)
# if we want we can also define and implement in abstract class itself.
# with logic to raise exception if any method is getting called using class object
# Abstract class is only designed to serve as a base class/ template.  It is a blueprint for new inherited
# classes to implement methods from abstract class.
###########################################################################################
from abc import ABC, abstractmethod

#abc (abstract base class) library in python help us to define abstract methods.

class Animal(ABC):
    species = 'Mammal'

    @abstractmethod    # here we are using abc library to make jump method in class as abstract.
    def jump(self):
        pass

    def who_am_i(self):  # this is other type of making method abstract by explicitly raising exceptions.
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
    def __init__(self, name):
        self.name = name

    def who_am_i(self): # this inherited class is now implementing methods from base class.
        print(f"I am {self.species} dog...My name is {self.name}!!!")
        # here self. is treating Dog and Animal as same class.

    def jump(self):
        print("I am jumping DOG")

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print(f"I am {self.species} cat...My name is {self.name}!!!")

    def speak(self, volume):  # while implementing function from base class it should exactly match
                              # definition from base class otherwise this method will be treated
                              # as separate method inside inherited class.
        print(f"Meow....Meow..!!! I am {volume}")

    def jump(self):
        print("I am jumping CAT")

mydog = Dog("Mikky")  # even though there is no constructor in Dog class, it is using constructor
                        # of base class and asking name as parameter.
mydog.who_am_i()
mydog.eat()
# mydog.speak() If we try to invlike thi methot it will give NotImplimented error. since there is no
# implimentation of this method in inherited class

mycat = Cat("Sheru")
mycat.who_am_i()
mycat.speak('loud')
mycat.eat()
mycat.jump()


# Summary : We can make methods abstract using two types
# 1. manually raising exception if code tries to call it using class object -- raise NotImplementedError
#    This approach is kind of making method abstract by ourselves and not using any other library. It
#    is just a normal method with exception to avoid direct call that's it, which forces us to implement it in other class
#    if we have to use it. Please note IT IS NOT MANDATORY for other child class to implement these abstract methods.
#    Its up to developer if they want to implement it on derived class.
# 2. Using abs (abstract base class) library. Import abc library abs shown above and use ABC class from it. 'abstractmethod' is
#    a decorator in library which helps us to mark our method as abstract using @abstract on top of method definition.
#    if we use this style of making method abstract then IT IS MANDATORY for inherited class to implement this
#    abstract method, otherwise we get error. THIS IS good way of implementing abstract class.