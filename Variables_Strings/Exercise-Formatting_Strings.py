## Formatting Strings ##
# Set the variable called first to your first name
first = "Pax"
# Set the variable called last to your last name
last = "Prennet"
# Set the variable called formatted that interpolates both using the .format() method.
# Pattern to follow is "First Name: Colt, Last Name: Steele"
formatted = "First Name: {}, Last Name: {}".format(first, last)
print(formatted) # First Name: Pax, Last Name: Prennet

# f-string way
first = "Pax"
last = "Prennet"
formatted = f"First Name: {first}, Last Name: {last}"
print(formatted)