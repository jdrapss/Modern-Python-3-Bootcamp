## Number is Odd Exercise ##
# You are provided with a random number in a variable called num
# Use a conditional statement to check if the number is odd.
# If num is odd, print "odd." Otherwise print "even".

# Hint: use modulus % to figure out if the number is odd

num = 7
# from random import randint
# num = randint(1, 1000)
# Using modulo (%) to figure out if it is odd - 2 is an even number, therefore,
# if it is an even number in the random number generator, then it will return 0
# 
if num % 2 != 0: # if the remainder of the num variable using 2 DOES NOT equal 0, then print odd
    print("odd")
else:
    print("even")

if num % 3 == 0:
    print("odd")
else:
    print("even")