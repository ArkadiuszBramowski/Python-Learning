# Make IDE program where tuple will show which notes student get.
# Show sorted notes from lowest to highest.
# Count medium range nots and answer if student is remarkable or not >= 4.75.

Notes = 3, 4, 6, 6, 1, 3, 4

print('Students Notes', sorted(Notes))

average = sum(Notes) / len(Notes)
print(f'Medium range of nots is {average:.2f}')

if average >= 4.75:
    print('You are a remarkable student')
else:
    print('You need to try again')
