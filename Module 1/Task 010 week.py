# Write a program that will receive the day of the week number from the user and then display the value 1
# "Monday", and for the value 7 it shows "Sunday".

number = int(input('Choose the number from 1-7: '))
if number == 1:
    print('Its Monday today.')
elif number == 2:
    print('Its Tuesday today.')
elif number == 3:
    print('Its Wednesday today.')
elif number == 4:
    print('Its Thursday today.')
elif number == 5:
    print('Its Friday today.')
elif number == 6:
    print('Its Saturday today')
elif number == 7:
    print('Its Sunday today')
else:
    print('This value is incorrect')


match number:
    case 1: print('Its monday today')
    case 2: print('Its Tuesday today.')
    case 3: print('Its Wednesday today.')
    case 4: print('Its Thursday today.')
    case 5: print('Its Friday today.')
    case 6: print('Its Saturday today')
    case 7: print('Its Sunday today')
