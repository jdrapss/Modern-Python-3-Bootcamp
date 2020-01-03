## Variable Assignment ##
# A variable in Python is like a variable in mathematics: it is a named symbol that holds a value.
# Think of variables like jars. Store things in the jar, then give it a name. Name the variable, and inside therer will be data.
# Ex: x = 100 or khaleesi_mother_of_dragons = 1 
# print(khaleesi_mother_of_dragons + x) 
    #returns 101
# Note: Variables are ALWAYS assigned with the variable name on the left and the value on the right of the equals sign.
# Note: Variables must be assigned before they can be used.

# Set variable
num_of_cats = 99
    # Sets the variable num_of_cats equal to 99
# Call the variable
num_of_cats
    # Returns no value to STDOUT, but does not return errors.
# Print the variable
print(num_of_cats)
    # Prints the variable num_of_cats, returning a value of 99 in STDOUT.

print(num_of_cats * 2) 

## Variable Reassignment ##
# Variables can be assigned to other variables
# Variables can be reassigned at any time
# Ex: python_is_awesome = 100
# just_another_var = python_is_awesome
# python_is_awesome = 1337

# Commas separate variable assignments
# Ex: all, at, once = 5, 10, 15

# You can set variables to itself combined with math operators
# Ex: If one of my cats runs away;
# num_of_cats = num_of_cats - 1
    # Returns 98 (Original value of 99)

# Assign new variables to the value of a currently set variable
# Ex: friends = 0
# friends = num_of_cats
    # Returns 98 (set num_of_cats to num_of_cats -1)