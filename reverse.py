# Get user input for the integer
number = int(input("Enter an integer: "))

# Initialize variables
reversed_number = 0

# Reverse the integer using a while loop
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

print("The reversed integer is: ",reversed_number)
