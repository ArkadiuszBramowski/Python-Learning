# Write a program that will count the words and characters in the sentence provided by the user

word = input('Give a list of words: ')
words = word.split(' ')
print('Words count', len(words))
print('Characters count', len(word))

# Write a program in which you ask the user for 5 numbers
# 1. We add each number to the list
# 2. We return the smallest, highest element and the arithmetic mean of all entered numbers

number_of_numbers = 5
list_of_numbers = []
for counter in range(number_of_numbers):
    value = int(input(f'Give number {(counter + 1)} / {number_of_numbers}: '))
    list_of_numbers.append(value)

print(list_of_numbers)

print('Smallest number is', min(list_of_numbers))
print('Highest number is', max(list_of_numbers))
print('Average number is', sum(list_of_numbers) / number_of_numbers)
