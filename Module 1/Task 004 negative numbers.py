# ask the user for a number and display the information
# whether it is a positive, negative or zero number

value = float(input('Whats the number: '))
if value > 0:
    print('This number is even')
elif value < 0:
    print('This number is odd')
else:
    print('This number is zero')
