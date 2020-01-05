## Lucky Number 7 ##
# The top of the file is starter code that randomly picks a number between 1 and 10
# and saves it to a variable called choice.

# Write a simple conditional to check if choice is 7. 
# If choise is 7, print out "lucky". Otherwise, print out "unlucky"

from random import randint
choice = randint(1,10)

if choice == 7:
    print("lucky")
else:
    print("unlucky")