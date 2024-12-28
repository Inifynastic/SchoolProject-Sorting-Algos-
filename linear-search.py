List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # The List we need to search from
maxvalue = len(List) # Maximum value so we don't get infinite loop or go beyond the bound
findvalue = 5 # The value we want to find.

def find(number): #Not necessary just a function
    isitfound = False
    for i in range(0, maxvalue): #Running Loop to check if it works
        isitfound = True
        break #Ignore this this is not necessay in our course(A levels)
    return isitfound # Returning boolean


Bool = find(findvalue)
if(Bool): # If(Bool) means True or False if True first else next one.
    print("Value found!")
else:
    print("Value not found!")
