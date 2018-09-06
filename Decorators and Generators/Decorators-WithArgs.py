#def accept_dec_param(param1):  # In case if we wan to take argument for decorator
def decorator_bypass_args(func_to_decorate):
    def real_decorator(*args, **kwargs):  # *args, **kwargs in mandatory which makes python understand that there
                                          # can be zero or more arguments
        print("Here goes code which we wan to run before running input function.")
        decorated_func =  func_to_decorate(*args, **kwargs)
        print("Here goes code which we wan to run after running input function")
        return decorated_func  # returning input function but changed signature of zero or more arguments.
    return real_decorator  # returning decorated function

'''
here we are using two step nested functions. First step takes function ass input and second steps decorates and returns 
function with modified signature. 
This way we have decoupled function signature with decorator.
'''

@decorator_bypass_args
def my_func(name, name1):
    print(f"\tThis is main func with argument {name} , {name1}")


my_func('ashpak', 'mulani')  # calling only function which will automatically execute with decorator.

'''
Now after Decoupling, if we want some arguments for decorator function to process them then we need to add one more
layer around our decorator. which will accept parameters for decorator . Above method 'accept_dec_param()' does the same

@accept_dec_param('test')
def my_func(name, name1):
    print(f"This is mail func with argument {name} , {name1}")


'''