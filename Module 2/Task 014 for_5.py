# Ask the user for a number, the result will display information whether
# it is a prime number.

from math import sqrt, ceil

number = int(input('Give a number: '))
is_prime = True
for div in range(2, ceil(sqrt(number))+1):
    if number % div == 0:
        is_prime = False
        break

if is_prime:
    print('Number is prime')
else:
    print('Number is odd')
