################################################################################################
# Library : lib/pdb.py
# Supports setting breakpoints, watch for variables etc..
################################################################################################

import pdb   # importing debugger

x = [1,2,3]
y= 4
z = 2

a = y + z
print(a)   # this is correct and it will print 6

'''
b = x+z   # this is incorrect because we can no add list and integer
          # hti swill throw error and terminate program with TypeError exception
'''

# we can set break point using debugger to se what is happening when we feel error might occur.
# this will provide us prompt to check what variable values are and see what all things are set
# till this line which help us in debugging
# enter q to quit debugger
pdb.set_trace()
b = x + z
