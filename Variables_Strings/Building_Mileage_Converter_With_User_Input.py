## Mileage Converter ##
# Building a converter that takes kilometers and converts into miles
# Will ask a user how many kilometers do you want to convert to miles?

print("How many kilometers did you run today?")
kms = input() # Changes the prompt, waits for user to hit the return key. #Kilometers
# print("Ok, you said " + kms) # String
print(f"Ok, you have run {round(float(kms) / 1.609344, 2)} miles today") # Convert kms to a float to have accurate mathematical operations
# Rounded value to 2 decimal places using the round function inside of the f-string
# Note: we cannot use concatenation here because we will have errors regarding strings and floats together

