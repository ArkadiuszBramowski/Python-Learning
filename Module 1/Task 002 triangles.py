# prepare a program that will calculate the area of a triangle
# with the given vertices (ask about each vertex separately)

base_a = float(input('Whats the number a: '))
base_b = float(input('Whats the number b: '))
base_c = float(input('Whats the number c: '))
p = base_a + base_b + base_c / 2
print('Half of the pool', p)
base_A = p - base_a
print('A totals', base_A)
base_B = p - base_b
print('B totals', base_B)
base_C = p - base_c
print('C totals', base_C)
P = abs(0.5 * (base_A + base_B + base_C))
print('total field is', P)
