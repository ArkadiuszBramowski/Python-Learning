# Receive a number from the user and then raise it to the power of 2,3,4,5. Use a for loop

number = int(input('Give a number : '))
result = number
for power in range(4):
    result = result * number
    print(f'Number {number} raised to power {power + 2} is {result}')

# write the code that will go through all the characters.
# strings of characters and will display each character separately and
# equivalent from an ASCII table using the ord() function.

sentence = input('Give a name: ')

for char in sentence:
    print(char, ord(char))
