## Formatting Strings ##
# Remember that concatenating numbers and strings returned errors
# There are also several ways to format strings in Python to interpolate variables

# We use F-Strings to incorporate numbers and strings

x = 10
formatted = f"I've told you {x} times already!"
print(formatted) # I've told you 10 times already!
#{x} is interpolated into the f-string

x = 15
formatted = f"I've been on this earth for {x} billion years!"
print(formatted) # I've been on this earth for 15 billion years!

# Using print function without defining a second variable
guess = 10
print(f"your guess of {guess} was correct!")

# Performing mathematical operations inside f-strings
guess = 10
print(f"Your guess of {guess + 1 } was correct!") # Your guess of 11 was correct!

# Combining name and number functions togethor
name = "Dastardly Dog"
guess = 15
print(f"Nice try, {name}, but your guess of {guess + 1 } was incorrect. You have been fed to the master_merge shell monster.")
# Returns Nice try, Dastardly Dog, but your guess of 16 was incorrect. You have been fed to the master_merge shell monster.

# The tried-and-true way (Python 2 -> 3.5) => .format method
# x = 10
# formatted = "I've told you {x} times already!".format(10)
# print(formatted)

# Udemy Examples requirements: Using the format method rather than f-stings
# fruit = "banana"
# ripeness "unripe"
# print("The {} is {}").format(fruit, ripeness))