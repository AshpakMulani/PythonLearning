################################################
# Range function : generates range of numbers
################################################
my_list = list(range(2,10))  # we are converting returned value in list format
print(my_list)



################################################
# enumerate function : use of object collections to return index and value in tupil format
################################################

my_list = ['a','b','c','d','e','f','g','h']

# if we have to get index as well as vlaue in list the normally we use
#counter = 0
#for item in my_list:
    #print(f"value at  index {counter} is {item}")
    #counter+=1
# but we can use enumerate function here

for item in enumerate(my_list):
    print(item)   # every item will contain tupil of index and value

# can also use tupli unpacking
for index,value in enumerate(my_list):
    print(f"value at {index} is {value}")




################################################
# zip function : combines two or more lists together (not append) and return sets in for of tupil
################################################

my_list1= [1,2,3,4]
my_list2 = ['a','b','c','d']
my_list3 = ['I','II','III','IV']

for item in zip(my_list1,my_list2,my_list3):
   print(item)

for val1,val2,val3 in zip(my_list1,my_list2,my_list3):
    print(f"{val1} - {val2} - {val3}")

################################################
# in function : return true if specified value exists in collection
################################################

if 'a' in 'Ashpak':
    print('exists')

my_list = ['a','b','c','d']
if 'a' in my_list:
    print('exists')

my_dict = {'key1':'val1', 'key2':'val2'}

if 'val2' in my_dict.values():
    print('exists')



################################################
# Random Library in python : this library has got lots of python functions
# below are frequently used functions
################################################


from random import shuffle
my_list = [1,2,3,4,5,6,7,8,9]
shuffle(my_list)   # this will randomly shuffle values in list and update original list.
print(my_list)


from random import randint
my_random_number = randint(1, 10)  # this will return random number from lower and upper range
print(my_random_number)



#####################################################################
# capitalize method : It makes first letter capital for given string
#####################################################################

my_string='macdonalds'

print(my_string[:3].capitalize() + my_string[3:].capitalize())  # output MacDonalds


######################################################################
# .join method : it joins items of list with specified separator
#######################################################################

my_list =  'Hello world i am ashpak'.split()
print(my_list)
print(' '.join(my_list))  # join list contents with separator space.
print(' '.join(my_list[::-1]))  # return reversed string



######################################################################
# in operator : it returns true if given value is present if specified collection
#######################################################################

#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(n1,n2):
    return n1+n2==20 or 20 in (n1,n2)  # this will directly return true/false depending on condition evaluation

print(makes_twenty(10,10))
print(makes_twenty(20,3))


