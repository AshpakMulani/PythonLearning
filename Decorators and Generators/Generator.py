#######################################################################################################
# Generator generates numbers one at a time.  when we call generator it does not generate all values at once.
# It generates only one  value and wait on request for next value. This way we can write memory efficient
# program which does not generate all numbers at once but generate next number when requested.
#######################################################################################################

# with out generate if we need to generate list of numbers then we will normally use list like below example
# disadvantage og this is complete list will stay in memory at any single point in time, which wont be
# efficient if we are using very large lists, or collections.

def cubes(n):
    cubes = []

    for i in range(n):
        cubes.append(i*i*i)
    return cubes   # here we are returning complete list of cubes for given range. which will eat more memory
                    # when given range is high

print(cubes(10))  # get list of cubes from 0 to 9


# With generators we can save memory without generating all values at once.
# python has Yield method which

def squares(n):

    for i in range(n):
        yield i*i   # here yield states that return i*i when 'next' is requested on function call and increment i by 1
                    # each time.

squares1= squares(10)
print(next(squares1))  # return square of zero
print(next(squares1))  # return square of one
print(next(squares1))  # return square of two

# once value of generator has been reached to end we can not loop same generator without initializing it again.

for i in squares1:   # now this will start from 3 because same generator has been used for zero , one , two above
    print(i)

print("-----------------------------")

for j in squares1:   # this for loop will not execute because generator has already reached to its end on above for loop
    print(j)

# generators work only in one direction and only once. If we need to again loop it then re-define it
print("-----------------------------")

squares2 = squares(20)
print(next(squares2))
for j in squares2:   # Now this will again start from zero
    print(j)



##############################   Iter ##########################3
#Iter function help us to conver iterable into generators

mystring = 'hello!!'

# next(mystring)  # this will fail because mystring is not generator

mystring = iter(mystring)  # this has not converted mystring to generator

print(next(mystring))