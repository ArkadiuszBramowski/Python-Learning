# Prepare a tuple storing the name, surname and age of the person.Then display this data as:
# Name: John
# Surname: Smith
# Age: 40

person = ('John', 'Smith', 40)
print(f'Name: {person [0]}')
print(f'Surname: {person[1]}')
print(f'Age: {person[-1]}')


# declare tuples in the form a = ((1,2,3), (4,5,6), (7,8,9,) and next:
# traversing them using a for display loop.
# 1 + 2 + 3 = 6
# 4 + 5 + 6 = 15
# 7 + 8 + 9 = 24

print('---' * 50)
calculations = (1, 2, 3), (4, 5, 6), (7, 8, 9)

for calculation in calculations:
    print(f'{calculation[0]} + {calculation[1]} + {calculation[2]} = {sum(calculation)}')
