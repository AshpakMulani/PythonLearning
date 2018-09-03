###########################################################################################
# try :
#    < this block of code might lead to error
# except:
#    < this block will run when there is error on code
# else :
#     < this block will run where there is no error in code
# finally:
#    < this block will always execute no matter if there is error or not
###########################################################################################


try:
    file=open("text.txt","w")
    file.write("Hello..this is test line")
except TypeError:   # we can capture only specific error as well
     print("There was as type error")
except TimeoutError: # Specific error
    print("there was time out")
except:
    print('All other exceptions')
finally:
    print("I always run")

#we can check default error list of python official website https://docs.python.org/3/library/exceptions.html




