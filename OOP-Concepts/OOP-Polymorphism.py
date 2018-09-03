##################################################################################################
# Polymorphism is way of making a base class method behave differently for different derived
# class by mutating/ overriding base class method in inherited class
# polymorphism use class inheritance.
##################################################################################################

class Animal():
    def __init__(self):
        pass

    def who_am_i(self):
        return "I am Animal"


class dog(Animal):   # deriving Dog from Animal
    def __init__(self, name, colour):
        super().__init__()   # here we are invoking constructor of base class, since we are deriving from it.
                                # we can also use Animal.__init__ instead of super, but if we use Animal then
                                # we will have to pass self object as well while calling Animal constructor.
                                # but if we use super which points to base class we do not have to pass
                                # self, because by default super points to base class.
        self.name = name
        self.colour = colour

    def who_am_i(self):
        print(super().who_am_i() + f" My name is {self.name} and I am  {self.colour}")


class cat(Animal):
    def __init__(self, food):
        super().__init__()
        self.food = food

    def who_am_i(self):
        print(super().who_am_i() + f" I love {self.food}")

mydog = dog('Mikky','White')
mycat = cat('catfood')


# in this example we are mutating who_am_i method of base class in subclasses and making it behave
# differently for diffent object types. This is polymorphism.

for pet in [mycat, mydog]:
    pet.who_am_i()   # so here same method is behaving differently for different objects


# common method os using polymorphism is usgin funciton which takes class object as paremater
# and call same method which behaves differently in differnt class

def introduce(pet):
    pet.who_am_i()

introduce(mydog)
introduce(mycat)