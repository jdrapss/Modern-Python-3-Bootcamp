## Boolean and Conditional Logic ##
# This section will relate mostly to making decisions based on True or False
# Boolean allows us to have branching paths and multiple outcomes

# Objectives #
# Learn how to get user input in Python
# Learn about "Truthiness"
# Learn how to use comparison operators to make a basic program

# Reminder for myself from previous section - Gathering Input
print("What is your name?")
my_name = input()
print("Hello, " + my_name + ".")

# Reminders from section 7
# Using f-strings to format and combine integers, floats, str

print("How old are you?")
dog_years = input()
print(f"Congrats, Oldy McOlderton, you are {float(dog_years) * float(7)} old in dog years.")

x = 10
formatted = f"I've told you {x} times already!" # I've told you 10 times already
print(formatted)
# Interpolates 10 into f-string
# Escape sequences

name = "Dastardly Dog"
guess  = 15
print(f"Nice try {name}, but you've guessed {guess + 10} times now. You're wrong")
message = "word\nup"
print(message)

# format method
# x = 10
# formatted = ("You are {x} years old").format(10)
# print(formatted)

# Udemy Examples requirements: Using the format method rather than f-stings
# fruit = "banana"
# ripeness "unripe"
# print("The {} is {}").format(fruit, ripeness))

# \\ = \
print("Hello\\") # Hello\

# Escaped double quotations

quotation = "Hello there \"Pax\"" # Hello there "Pax"
print(quotation)

# NONE variable saves a value of nothing into a variable so we can call on it later

name = "Daisy"

