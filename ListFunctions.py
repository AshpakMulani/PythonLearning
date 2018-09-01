# list is collection of object of different types

my_list = [1,'hello', 1.28]
print(my_list)
print(len(my_list))
for listitems in my_list:
    print(listitems)

# slicing and indexing on list works same as string.
#so basically string is list of object types characters
my_list = [1,'hello', 1.28]
print(my_list[0])
print(my_list[1:])
print(my_list[::-1])  # reverse list same as string

# concatenation works same as string
my_list =  [1,'hello', 1.28]
my_list1 = [2,3,4]

print(my_list + my_list1)

my_list.append(my_list1) # nesting list
print(my_list)
print(my_list[3][1])  # accessing item at index of nested list

# Main difference with string is we can mutate list unlike string.
my_list = [1,'hello', 1.28]
my_list[2] = 'world'
print(my_list)


# different functions for list insert, remove, reverse, sort, append, pop, clear, copy, count, index
my_list = [1,'hello', 1.28]
my_list.append('world')
print(my_list)

my_list.pop()  # remove last item
print(my_list)
popped_item = my_list.pop(1)  # remove item at index 1
print(my_list)
print(f'Popped Item : {popped_item}')

# sort only works on list containing similar type items
my_list = [1, 8, 2.5]
print(my_list.sort())  # this will return null, because sort does not return anything. It just sorts
                        # items in original list inplace
print(my_list)      # now this will return sorted list.
print(my_list.append('world')) # most of the functions perform operations on list in place
                                # and does not return anything.
print(my_list)          # now this will return list with appended value


# embading other structure like dict in list
my_hybd_list = ['hello',{'key1':'value1','key2':'value2'},'world']
print(my_hybd_list)
print(my_hybd_list[1]['key2']) #accessgin second key from embaded dict at index1


#########################################################################
# List Comprehensions : it is way of quickly creating list with values
#########################################################################

#Traditional way of creating list in loops
my_list=[]
for i in range(0,20,2):
    my_list.append(i)
print(my_list)

#Instead of seperate for loop/ any other loop and .append method we can use below method
# this is called "list comprehensions"

my_list = [i for i in range(0,20,2)]
print(my_list)

my_list = [x for x in 'Hello World']
print(my_list)

# We can also perform operations on x

my_list = [x**2 for x in range(1,10)]
print(my_list)

my_list = [x for x in range(1,10) if x%2==0]  # get only even numbers with if
print(my_list)


my_list = [x if x%2==0 else "Odd" for x in range(1,10) ]  # get only even numbers with if else
print(my_list)


# we can use list comprehentions on multiple lists as well
my_list1 = [1,2,3,4]
my_list2=[100,200,300,400]

my_final_list = [x*y for x in my_list1 for y in my_list2]  # like nested for loop
print(my_final_list)


st = 'Create a list of the first letters of every word in this string'
my_list = st.split()
my_list = [x[0] for x in my_list]
print(my_list)
