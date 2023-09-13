# Receive an integer from the user and
# then display all even numbers from 2 to that number on the screen

num1 = int(input('Enter first number: '))

for counter in range(2, num1, 2):
    if counter % 2 == 0:
        print(counter, end=', ')

# Below, display the sum, number, average and product of these numbers

num1 = int(input('Enter first number: '))
total = 0
length = 0
multiply = 1
for counter in range(2, num1+1, 2):
    total += counter
    # total = total + counter
    length += 1
    multiply *= counter
    print(counter, end=', ')

print(f'Total of this numbers is {total}')
print(f'Average of numbers is {total / length}')
print(f'Multiply of numbers is {multiply}')
print(f'Average of numbers is {total / len(range(2, num1, 2))}')
