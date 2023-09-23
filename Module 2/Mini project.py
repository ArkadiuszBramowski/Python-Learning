from math import ceil

# How many walls to paint? 3
# If you want to take last height press enter.
# Give a width 1 wall :
# Give a height 1 wall:
# Give a width 2 wall :
# Give a height 2 wall:
# Give a width 3 wall :
# Give a height 3 wall:
# Surface to be painted:
# Number of soil layers: 2
# # Number of layers of paint: 3
# # For 1 painting you need:
# # soil 5mkw = 1l
# # paint 13mkw = 1l

Walls = int(input('Give a number of walls: '))
print('The number of walls to paint is', Walls)
print('All values are given in meters e.g. 3.2')
previous_height = 3
total_area = 0

for counter in range(Walls):
    width = float(input(f'give me the width of the wall nr {counter + 1}: '))
    height = input(f'give me the height of the wall nr {counter + 1}: ')

    if height == '':
        height = previous_height
    else:
        height = float(height)
        previous_height = height

    total_area += height + width

print(f'Total area to paint is {total_area}')

layers_of_base = int(input('How many layers of base: '))
layers_of_paint = int(input('How many layers of paint: '))

liters_of_base = ceil(layers_of_base * total_area / 5)
liters_of_paint = ceil(layers_of_paint * total_area / 13)

print(f'You need this many liters of base: {liters_of_base}.')
print(f'You need this many liters of paint: {liters_of_paint}.')
