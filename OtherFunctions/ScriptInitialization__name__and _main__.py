####################################################################################
# __name__ == __main__
# when we run python script directly or using command line it initializes few variables
# before starting code execution in script. One of such variable is __name__
# and its value is set to __main__  at beginning if script execution. this variable gets initialized
# to __main__ only when script is ran and not when script is imported.
# so we cna use logic if __name__ == __ main__to check if script is ran and not imported and run some code accordingly
#####################################################################################

def runalways():
    print('I am executing always, even if imported or ran directly')

def main():  # this function will not run when this script is imported in other script.
    print("I am executing directly and not being imported..!!")

runalways()    # this function will run always while script is being imported in other script (runs on import <script name> code
              # or while being ran direcly


if __name__ == '__main__':
    main()

# now this script will run main() only when ran directly and not when imported in other script
# big codes will have this line at the bottom to run things mentioned in main() function



