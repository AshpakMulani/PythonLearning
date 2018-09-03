# Function documentation string.

def my_function():
    '''
     DOCSTRING: this is a documentation string for information on function
                when we use help(my_function) then all this information from comment
                gets displayed.
    :Input: No input.
    :return: prints hello world
    '''
    print("hello world")

help(my_function)   # when we call help for function we get commented info from from top of function.


# we can take arguments as well

def dog_check(inputstring):
    return 'dog' in inputstring   # we have returned trou/false in single line itself instead of writting
                                    # if/else, because 'in' itself return true or false.
                                    # this is how experiance person should write a code.
print(dog_check('my cat ran away'))



# use function to check if value is prime number
# Prime number = a number should be devisible by itself or only by 1. (except fraction numbers)
# we can go on checking from 2 to number-1 to check if given number is divisible by any number
# but efficient method is exclude even numbers from process as they are divisible by atleast 2
# and process division login till only squer root of given number.
'''
Let's say m = sqrt(n) then m × m = n. Now if n is not a prime then n can be written
as n = a × b, so m × m = a × b. Notice that m is a real number whereas n, a and b are natural numbers.
Now there can be 3 cases:

a > m ⇒ b < m
a = m ⇒ b = m
a < m ⇒ b > m
In all 3 cases, min(a, b) ≤ m. Hence if we search till m, we are bound to find at least one factor
of n, which is enough to show that n is not prime.

'''

# lets create a function now  :)
import math
def check_prime(number):
    if number% 2 == 0 or number < 2:
        return False
    for x in range(3, int(math.sqrt(number))+1, 2): # checking divisibility by odd numbers starting from 3 toll squer root of number
        if number % x == 0:
            return False

    return True   # if not divisible by anything means it is prime.

if check_prime(9):
    print("Prime number!!")
else:
    print("Not Prime number!!")




##############################
#  *args    : arguments
#  *kwargs  : key word arguments
##############################

# If we need to make function to access as many parameter as user wnats without defining poritional
# parameter in function definition then we user * args
# python converts all passed parameters to tupil using *args

def my_func(*args):  #naming keyword as *args is not mandatory we can use anything like *myvals, *xyz etc....
    print(args)
    for item in args:
        print(item)
    print(str(args[0]) + " - " + args[1])

my_func(1,'two',3,'four',list(range(2,7)))   # arguments can be of any type



def my_func(**kwargs):      # if *args is used then python takes arguments as tupil.
                            # if **kwargs is used python takes arguments as dictionary
    print(kwargs)
    print(kwargs['drink'])

my_func(fruit='apple', drink='juice')


# we can also take *args and **kwargs as parameter at same time

def my_func(*args, **kwargs):
    print(f"I would like to have {args[1]} {kwargs['drinkitem2']}")


my_func(1, 2, 3, 4, 5, lunchItem1='rice', lunchitem2='pizza', drinkitem1="wine", drinkitem2='wiskey')


#####################################
## nested functions : we can write function inside function
## variable scope is calculated as "LEGB" rule
#L:Local veriable (first inner function will check veriable inside.
#E:Enclosing function local (then veriable in parent functions will be used.
#G:Global veriable (then global veriable will be used)
#B : built in (then variable name will be eveluated to builtin functions like range, open, def etc....)
#####################################

x = {'lower':'hello', 'upper':'HELLO'}  # this x will not be used inside function, since it has its own x

def my_func(name):
    x = {}
    def makelower():
        x['lower']=name.lower()  # this wont affect anything to global variable

    def makeupper():
         x['upper']=name.upper()

    makelower()
    makeupper()
    return x

response=my_func('Ashpak Mulani')
print(f"lower version of input = {response['lower']} . \nUpper version on input = {response['upper']}")
print(f"original global lower value = {x['lower']} . \nUpper value = {x['upper']}")




#######################################################################################################

####   Lambda, map, filter

#######################################################################################################

##### Map function : Runs specified function for given collection of objects

def make_squer(x):
    return x**2

my_list=[1,2,3,4,5]
print(list(map(make_squer,my_list)))


###### filter function :  returns objects from collection with use of function which returns true or false

def check_even_length(x):
    return len(x)%2==0

my_list=['Hello','world','my','name','is','ashpak']

print(' '.join(filter(check_even_length,my_list)))  #item from collection is returned only when function returns true.


######## Lambda function : these are un-nammed one liner short functions
'''
def sample(x):
    return x**2

response=sample(5)
    
Above mentioned is normal style of coding. Since this is small function we can make it lambda functiion

response = lambda sample x: x**2
response(5)
'''


response = lambda x: x**2  # lambda <input_parameter>: <Code>
print(response(5))


# we can use lambda with use of map and filter easily.
my_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda x: x**2, my_list)))  # here we specified function logic inline with help of lambda.


