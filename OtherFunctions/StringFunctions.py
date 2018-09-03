################## Escape character \n : new line \t:new tab ###################
print("\thello \n world")

#len : length of string
print(len("hello \n world"))

############ String indexing and slicing #####################
my_string='Hello World'

print(my_string[0])  # here string is treated like zero indexed array.
print(my_string[-1]) # select from right use negative index (reverse indexing)
print(my_string[-11]) # select from right use negative index (reverse indexing)

# slicing syntax [start_char_index:end_char_index:step_size]
print(my_string[2:]) #slicing is like substring. Get characters starting from index 2
print(my_string[:4]) # get characters upto index 4 from start zero(but exclude index 4)
print(my_string[2:7]) # starting from index to upto index 7 (exclude 7)
print(my_string[::2]) #get all string with step size 2. Means skip alternate chars
print(my_string[1:11:3]) #get characters strting from index 1 upto index 11 with step size of 3 (exclude two chars in between)
print(my_string[-10:-1:2]) #we can even use negative indexing but evern negative indexing slicing works from left to right, since step size in positive.
print(my_string[::-1]) #if we mention step size as negative then it return from right to left. This example will reverse string.
# String are immutable. Means we can not change a single character in string directly by indexing
# Ex. my_string[2]='A' is nto allowed. But little Jugaad can be done using concatenation
my_string = my_string[:2] + 'A' + my_string[3:]
print(my_string)

################  common string function ###########

my_string = 'hello world'
print(my_string.upper())
print(my_string.lower())
print(my_string.split()) # Return list by splitting string with white space.
print(my_string.split('rl')) # Return list by splitting string with characters mentioned

#Formatting string with .format() function.
# .format inserts giver values in string at places mentioned by {}.
# We can also use ordering to apply given values in string like {1},{3],{2}
my_string='hello world'
print('Hey guys...{}.....{}'.format(my_string,'mike testing'))
print('Hey guys...{1}{2} {0}'.format(my_string, 'look i am saying', '....'))
#we can also reference format list using names
print('Hey guys....{t1}...{t3}'.format(t1='look what', t2='i did', t3='happened'))
#Format float value {value:width.precision f}
#value = actual value need to be formated
#width=lenght of final string we want as outout
#precision f=number of decimals after . we need in result.
result=100/777
print("result = {0:10.3f}".format(result)) # result will be 'result=      0.129' total string lenght of 10

# formating can be also used in different way starting from python3.6
# put f in front of string and you can directly use variable inside string.
# this is called formatted string.
my_string='hello world'
new_string=f'yo guys...{my_string}'
print(new_string)