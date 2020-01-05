## Conditional Statements ##

# Conditional logic using if statements represents different paths a program
# can take based on some type of comparison of input

# Pseudo-Code for conditional statements:
# if some condition is True:
#   do something
# elif some other condition is True:
#   do something
# else:
#   do something

# Example idea: If high_score = 99, then end game, elif high_score < 99, then keep going

# Note: You do not have to have an elif or else condition.
# You can have multiple elif conditions

# Conditional Checks
# Tying in previous understanding of input
print("What is your name?") # What is your name?
name = input() # Pax

if name == "Arya Stark": # Colons tell Python there will be an indented function below
    print("Valar Morghulis")
elif name == "Jon Snow":
    print("You know nothing")
else:
    print("Carry on") # Carry on

# == checks for equality; = is for variables