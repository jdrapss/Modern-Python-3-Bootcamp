## Dynamic Typing ##
# Python is highly flexible about reassigning variables to different types:
awesomeness = True
print(awesomeness) # True

awesomeness = "a dog"
print(awesomeness) # a dog

awesomeness = None
print(awesomeness) # None -> Pythons way of saying nothing. This is a data type that represents a blank value.

awesomeness = 22 / 7
print(awesomeness) # 3.142857142857143

# We call this "dynamic typing", since variables can change types readily.
# Other languages, such as C++, are statically-typed, and variables are stuck with
# their originally-assigned type:

# C++
#int not_awesomeness = 5;
    # Data type had to be defined first
#not_awesomeness = "cool"; // !Error