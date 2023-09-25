first_name = ['ToM', 'AlICE', 'CArol', 'ChRIStof']
proper_first_name = []

# maping

for name in first_name:
    proper_first_name.append(name.title())

print(proper_first_name)

# add new element
first_name.append('Erwin')

# add new element on position 3
first_name.insert(3, 'Ed')

# removes one item from the list and assigns it to a variable
# if empty, then the last one, but you can also specify the index
last_first_name = first_name.pop()
third_name = first_name.pop(3)

# last and third element disappear
print(first_name)

# that's how we clear whole list
first_name.clear()
