#Tuples are similar to lists but these are immutable means we can NOT alter values inside.
#constructed similar to list but instead of [] we use ()
#tuples are mainly used over list where we need a list of values which wont be ever change in code.

my_tup = (1,'hello world', 3)
print(my_tup)
print(my_tup[1])

# we can embade different data structures as well inside like list, dist etc
my_hubd_tup = (1, {'key1':'val1'}, [3,4.5,'hello world'])
print(my_hubd_tup)
print(my_hubd_tup[1:]) # since it stored data indexed we cna use all functions of slicing and indexing like string/list
print(my_hubd_tup[::-1]) #reverse tuple


#tuple have only two methods index and count

my_tup=(1, 2, 3, 4, 3)
print(my_tup.count(3))  #thsi returns number of times 3 is present
print(my_tup.index(3))  # this returns index of first occurrence ot 3


myl=['0', 3]
print(myl)