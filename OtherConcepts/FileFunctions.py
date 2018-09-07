# Python does not require any object to perform file operations like VB script FileSystem object
# In Python we can directly use open() function to open file.

my_file = open("c:\\ashfaque\\PythonTest.txt")
print(my_file.read())  # returns all contents

# after every read file cursor moves to at the end of file which cause all other operations
# performed after read() to return blank. Hence we need to use seek(0) to move pointer
# to the beginning of file every time after we perform read()
my_file.seek(0)
print(my_file.readlines()) # return list with each line as individual item.


# once we performed 'open' operation on file in python we need to manually perform 'close'
# operation as well in code otherwise it will cause file in use for other operations.
my_file.close()


# To avoid this approach of closing file manually in code after open we can use below method of
# opening file which python closes automatically for us.

with open("c:\\ashfaque\\PythonTest.txt") as my_file:
    print(my_file.readlines())


#File open types
# read(r) : only for reading, no writing. (Default)
# write(w) : only for writing, no reading. Overwrite existing or create new if does not exists.
# append(a) : only add contents at the end of file
# read plus (r+) : is reading and writing. Does nto create new file if does not exists.
# write plus (w+) is for writing and reading. Creates a new file if does not exists.

with open("c:\\ashfaque\\PythonTest.txt", mode='w') as my_file:
    my_file.write("hello world \n. How are you")  # this will overwrite existing file.





