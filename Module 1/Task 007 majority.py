# Prepare a program that will tell you how old that person is based on the age at which a given person was born
# whether she is of age and whether this year is a leap year. Such a year does not always occur every 4 years
# You can store the current year in one variable declared at the beginning.

Currenty_year = 360
print('Its year 360')
Birth_day = int(input('What year you were born?: '))
age = Birth_day - Currenty_year
print(f'Your age is {age}.')
if age >= 18:
    print('You are a adult')
else:
    print(f'You will be adult in {18 - age} years.')
if Birth_day % 400 == 0 and Birth_day % 4 == 0 and Birth_day % 100 == 0:
    print('This year is leap')
