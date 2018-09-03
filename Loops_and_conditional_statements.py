#############################################
# if     elif    else
#############################################
my_name = 'Ashpak'

if my_name == 'Ashpak':
    print("Hello Ashpak!!!")
elif my_name == 'mulani':
    print("Hello Mr. mulani")
else:
    print("Hello Stranger")

#############################################
# For loop
#############################################
for i in range(0,5):
    print(i)



my_name = 'Ashpak Mulani' #similarly we can iterate list, tuple, every key in dictionary
for char in my_name:
    print(char)

# For loops for fetching dictionary
my_dict = {'key1':'value1', 'key2':'value2','key3':'value3'}
for key in my_dict:
    print(my_dict[key])

for key,value in my_dict.items():   # Tupli unpackaging explained below
    print(key + ' : ' + value)

#Tuples has some extra functionality in loop
my_tup_list = [(1,2),(3,4),(5,6),(7,8,9)]

for item in my_tup_list:
    print(item)  # this will print list of tuplis

# This is called TUPIL UNPACKAGING
for (a,b) in my_tup_list:  # we can refer individual item in tupil in side parent look for list.
    print(a)               # this wont print last tupil because it has 3 values and we are taking
    print(b)               # only two values in for loop



#############################################
# While Loop
#############################################
'''
while bool_condition:
    do this
else:
    do this
'''
x=0
while x < 5:
   print(f"current value of x is : {x}")
   x+=1



#############################################
# break    continue   pass
#############################################

'''
Pass : does nothing, it just continue with execution. Used while troubleshooting if we need to comment cll conde from loops
'''

for i in range(0,5):
    pass         # Do nothing

'''
Continue : tell loop to skip code below continue and go back to top for next iteration
'''

for i in range(0,5):
    if (i == 2):
        continue        # if we use pass instead of continue the it will print all values 0,1,2,3,4
    print(i)   # this will print 0,1,3,4

'''
break : ends current loop
'''
for i in range(0, 5):
    if i == 2:
        break
    print(i)   # this will print 0,1


