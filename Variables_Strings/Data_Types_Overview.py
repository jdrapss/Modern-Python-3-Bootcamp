# Data Types
# In any assignment, the assigned value must always be a valid data type

# Most commonly used data types:
    # bool -> True or Fale values (binary, yes or no, true or false)
        # Must be capitalized (True or False)
        # Lowercase true and false will return 'true' is not defined (Python asssumes it is an undefined variable)

# Set variables is_active and game_over and print their output
is_active = True
game_over = False # This is commonly used in basic games such as tic-tac-toe
print(is_active, game_over)

    # int -> an integer (1,2,3)
    # str -> (string) a sequence of Unicode characters, ex: "Pax"
        # Strings are used to set the value of items, ex: setting the value of Jiff_Peanut_Butter = <Insert Product Number>
# Set variable some_string to 8 and print output
some_string = "8"
print(some_string)
type(8)
# <class 'int'>
type(some_string)
# <class 'str'>
    # list (Data Structure) -> an ordered sequence of values of other data types, ex: [1,2,3] or ["a", "b", "c"]
        # Ex: I am sold out of Jiffs Peanut Butter, but I have a waitlist of people who want it.
        #     This must be organized so that the first person who ordered, will get their item first.
    # dict (Data Structure) -> a collection of key: values, ex: { "first_name": "Pax", "last_name": "Prennet"}
        # Used to store multiple variables that would always go togethor.