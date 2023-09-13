# write a program that displays information whether a number is divisible by 5, 11 or 11 and 5.


value = int(input('Whats the number: '))
if value % 5 == 0 and value % 11 == 0:
    print('This number is divisible by 5 and 11')
elif value % 11 == 0:
    print('This number is divisible by 11')
elif value % 5 == 0:
    print('This number is divisible by 5')
else:
    print('This number is not divisible by 5 or 11')
