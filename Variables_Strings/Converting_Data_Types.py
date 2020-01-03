## Converting Data Types ##
# In string interpolation, data types are implicitly converted into string form
# You can also explicitly convert variables by using the name of the builtin type as a function
decimal = 12.56345634534
integer = int(decimal) 
print(integer) # 12 Note: Does not round, just chops off the decimal

# Converting lists to strings
my_list = [1, 2, 3]
my_list_as_a_string = str(my_list)
print(my_list) # [1, 2, 3]
print(my_list_as_a_string) # "[1, 2, 3]"

num = 12
type(num) # int

# Convert num into float
num = float(num)
print(num) # 12.0

# Convert float into int
num = 12.6
type(num) # float
num = int(num)
print(num) # 12 Note: Does not round. Just chops off.

print(int(99.444443)) # 99

# 
print(str(8)) #8 Note: Do not use str as a variable. Already reserverd in python.