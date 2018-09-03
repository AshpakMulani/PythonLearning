# These are also called as Magic method or Dunder method
# These methods allow use to use built in methods like print, len etc
# with our own objects
# special method syntax __<method name>__

class sample():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I am sample class and my name is {self.name}"
    #Since we have defined str method in class as special method. Whenever any operation which needs str representtion
    # of object then this special method will execute.

    def __len__(self):
        return

    #def __describe__(self):   This thing will not work, because special methods can be defined only for python built-in
        #print('describe')     # methods like print, len etc


instance = sample('rocky')
print(instance)  #without __str__ implimentation in class this will give only object
                 #  locaiton in memory without __str__ method in class

print(len(instance))  # this will print 1000








