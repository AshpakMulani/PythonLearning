# Decorators are used for wrapping given function in some other code. Instead of directly changing
# existing code which is prone to introducing new error, we create a decorators which takes function
# as argument and run decorators own code before/after running function taken as argument.
# So if we have to make changes / enhance existing function we use decorator for that function
# with extra code which we want to patch to existing code of function. It helps us to implement
# changes to existing function by acting as a on/off switch. If we do not have to use new code
# around existing function then just remove decorator.

############  Basic decorator in action ##########
def my_decorator(func):

    def decorator_internal_func():
        print("Here goes code which we wan to run before running input function")
        func()   # running input function
        print("Here goes code which we want to run after running inout function")

    return decorator_internal_func   # Here we are taking function to run as input asn returning a function which wraps
                                     # pre and post code to input function

def func_to_decorate():
    print(f"\tthis is actual function.")


func_with_decorator = my_decorator(func_to_decorate)
func_with_decorator()  # Here we are running function returned from decorator


##########   decorator with real use  ##################
# Instead of using above approach to call decorator function, python provide easy way to apply decorator on any function.
# Please note here both functions are decorators are not accepting any arguments. If we want to apply decorator on
# function which accepts arguments then there is other script for enplaning this concept 'Decorators-withArgs.py'

@my_decorator  # this single line applies decorator to next defined function, thats it...!!!
def new_func_to_decorate():
    print(f"\tthis is actual new function.")

# now whenever we call actual function it will automatically use decorator

print("\n\ndecorator function call")

new_func_to_decorate()