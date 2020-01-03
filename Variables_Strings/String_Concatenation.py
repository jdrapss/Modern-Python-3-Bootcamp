## String Concatenation ##
# Concatenation is combining multiple strings togethor. In Python, this is done 
# with the "+" operator
# Ex: 
str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two 
print(str_three) # your face

username = "PaxPrennet"
print("Hello there, and welcome to the game, " + username + ".")

"a" + "b" + "z" # abz

# Cannot combing integers with strings 
# Ex: 8 = "hello" returns TypeError: unsupported operand types(s) for 'int' and 'str'

# You can also use the "+=" operator to add new data to update certain variables.
str_one = "ice"
str_one += " cream" # Updating the variable to add new data to it. Combines with original variable contents.
print(str_one) # ice cream


# Set a variable for your name
name = "Pax"
# Dont forget your last name!
name += " Prennet" # Adding last name to the original variable without having to perform name + " Prennet"
print(name) # Pax Prennet

# Using += with numbers in variables
people = 99
people += 1
print(people) # 100

# Using the -= operator for subtraction in variables
people -= 10
print(people) # 90

# Using the *= operator for multiplication in variables
people *= 10
print(people) # 900