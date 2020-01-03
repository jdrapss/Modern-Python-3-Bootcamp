## String Escape Characters ##
# In Python, there are also "escape characters", which are "metacharacters" - they get 
# interpreted by Python to do something special:
# All escape characters start with a backslash "\"

# \n will create a new line

# Sets variable using the \n string escape character to create a new line
new_line = "hello\nworld"

print(new_line)
# hello
# world

# \ is represented as an escape sequence by Python. Use \\ for backslash
str = "this is a backslash: \\" 
print(str)
# this is a backslash: \