# None # Python's version of null
# Returns nothing, but the data type is set properly
# none
    # returns NameError: name 'none' is not defined

# Ex: Application requires user PII, such as Name, age, child, child age:
name = "Daisy"
age = 30
child = None # Daisy has no children -> This allows us to call the variable later
    # If the child variable is left with no value, we cannot call it later, as it has not been defined. 

name = "Dusty"
age = 45
child = "Pamela" # Dusty has a child, so we set the variable to the child's name.

type(child)
# <class 'NoneType'>

