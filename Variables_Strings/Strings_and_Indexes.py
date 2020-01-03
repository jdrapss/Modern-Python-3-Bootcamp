#"lol" is an indexed string, meaning that each character has a number that responds to it
# 0,1,2, and so on
# 0 is the first number in any string

print("lol"[0]) # l

name = "Chuck"
print(name[0]) # C
print(name[1]) # h
print(name[4]) # k

print("\n")
# Printing a new line for ease of use
# Using print(name[5]) in this case will return an error related to the string index out of range

# Example: We have an application (a video game) that requires a character to respond yes or no
#          We assume that users will type many different ways to say Yes or No, such as Yeah, yaaa, nay, nooo, nuuuu, etc.
#          To do this, we can use indexed strings to search for the first letter (y or n)

answer = "yaaaaaaaaaaa"
print(answer[0]) # y

answer = "yessir"
print(answer[0]) # y
# We can call characters using negative numbers
print(answer[-1]) # r
print(answer[-2]) # i
