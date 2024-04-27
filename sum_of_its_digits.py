number = int(input("Enter a two digit Number : "))

number_string = str(number)
total = 0

for i in number_string:
    total = total + int(i)

print(total)
