# Receive 3 numbers from the user, display which of them is the largest and which is the smallest.

a = int(input('Number 1: '))
b = int(input('Number 2: '))
c = int(input('Number 3: '))

max_value = c
min_value = c

if a > b:
    if a > c:
        max_value = a
    else:
        max_value = c
else:
    if b > c:
        max_value = b
    else:
        max_value = c

if a < b:
    if a < c:
        min_value = a
    else:
        min_value = c
else:
    if b < c:
        min_value = b
    else:
        min_value = c
print(f'Max value is {max_value}')
print(f'Min value is {min_value}')
