# From the given field, display the numbers that are divisible by 4 and those that are divisible by 5.

numbers = 3, 6, 10, 15, 22, 173, 2440, 750, 33333

for number in numbers:
    if number % 4 == 0 or number % 5 == 0:
        print(number)


names = 'Alexandra', 'Wojciech', 'Bjorn', 'Przemyslaw', 'Grzmichuj', 'Adolf'

for name in names:
    if len(name) > 5:
        print(name)

for counter in reversed(range(1, 5)):
    print(counter)
    for digit in range(1, counter + 1):
        print(digit)

print('wait for it')

for counter in reversed(range(1, 5)):
    print(counter)
    for digit in range(1, counter + 1):
        print(digit, end=' ')
