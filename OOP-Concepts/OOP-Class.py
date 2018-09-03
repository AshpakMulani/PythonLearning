
#####Define a class##########

class MyClass():   # for class definition it is best practice to use camel casing (use of small and upper case letters)
    pass   # dont do anything

obj_myclass=MyClass()  # create object of calls

print(type(obj_myclass)) # this will tell object is of type MyClass


############### Class with constructor (init method)###################

class MyCar():
    '''
     below (__init__) is class constructor which run every time when we create a new object
     self keyword links init method to respective class's object.
     init method can also define arguments accepted by class during object creation
    '''
    def __init__(self, model, makeyear):   # model is arguments accepted by class. These arguments needs to be passed
                                 # while creating class object
        self.model = model       # we need to assign accepted arguments which is passed while creating object
                                 # to class attribute / class's own veriable with self.attribute_name

# lets create object of class

firstcar = MyCar(model='BMW',makeyear=1987)         # initiating class object with required parameter
print(firstcar.model)           # now we can access class attributes using class object



######################### Class with methods ##################

class MyCar():
    # Class level attributes. These are attributes which does not associated with individual object of class
    # and remain same for every object

    number_of_wheels = 4  # here we are not using self keyword because we do not have to associate
                          # these attrobutes to any individual instance and need to keep it default
                          # for all instance. By default these are public attributes and can be accessed by objects
    def __init__(self, model, make=2018):
        self.model=model
        self.make=make

    def returnlist(self):           # self is mandatory in every method which links method to its class's respective object
        return list(self.model)


myfirstcar = MyCar(model='rolls royce') # if we do not pass make parameter then it will take default value = 2010
                                        # as defined in init. If init does not have default values assignemnt
                                        # then it is mandatory to pass its value
print(myfirstcar.returnlist())  # we are accessing method from class for newly created object myfirstcar
print(myfirstcar.number_of_wheels)  # accessing class default attribute



############# Class with methods having own arguments #################


class MyCar():
    number_of_wheel =4

    def __init__(self,model):
        self.model=model

    def calculate_price(self, make):
        # notice this method is accepting its own argument. This argument has no relation with constructor.
        # While creating class object we do not need to pass it,but while calling method we will need to pass it.
        # also notice since this parameter is not associated with class object we are not using self.<name> while
        # accessing it. Just using its name, because it is normal parameter to method and not class object attribute.

        if self.model.lower() == 'bmw':
            if make in range(2010, 2018):
                return 10000
            if make < 2010:
                return 5000
        if self.model.lower() == 'rolls royce':
            if make in range(2010, 2018):
                return 20000
            if make < 2010:
                return 10000


objcar = MyCar('BMW')

print(objcar.calculate_price(2017))  # we are just passing make as method parameter. This object will now access
                                     # model as its attribute and when object is calling method it will take
                                     # make as method parameter and not class instance attribute.

objcar = MyCar('Rolls Royce')
print(objcar.calculate_price(2017))  # this will print price for rolls royce

