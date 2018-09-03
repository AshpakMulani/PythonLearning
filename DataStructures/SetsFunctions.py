# sets are un-indexed collection of UNIQUE elements.
#We use sets where we do not want redudent objets in collection.
#Sets does NOT suppoer indexing means we can not access values using my_set[1] etc
# since it is for holding only unique values it does nto support ti embade other data  structures like dict, list etc.

my_set = set('3') # we can not specify multiple values here. Either use only set() or set('1') etc...
my_set.add(2)
print(my_set)
my_set.add('3')  # this wont add new value to set because 3 is already preset.
                # this is wat maily set is. It make sure only unique values are there
print(my_set)

                #set can embade other data structures like list, dict. Ex this will erro my_set.add({'key':'value'})

# wIf we want to get unique value from list then we can cast it to Sets
my_list=[4, 1, 3, 4, 2, 3, 'hello']
print(my_list)
print(set(my_list))