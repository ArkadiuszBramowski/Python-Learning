# Use tuple and range to make list from 0 to 100.

Value = tuple(range(0, 101))
print(Value)

# Take out only first 10 numbers.

print('First', Value[:10])

# Take out only last 10 number.

print('Last', Value[-10:])

# Take out from the list only odd numbers.

print('Odd', Value[::2])

# Take out from the list only even number in lane from higher to lowest.

print('Even numbers from higher to lowest', Value[::-2])
