#  Ask the user for a name and write whether it is a female or male name.
name = input('Give a name: ')

if name.endswith('a'):
    print('Welcome lady')
else:
    print('Welcome mister')

# write a program that generates very strong passwords by replacing "a" with @ and all "s" letters with $.

Password = input('Give me a password to (amplification): ')

Password = Password.lower().replace('a', '@')
Password = Password.lower().replace('s', '$')
print(Password)

# count how many times the word dog appears in a sentence.

sentence = 'A dog is mans best friend, but not every dog a knows about it'
sentence = sentence.lower().count('dog')
print(f'Dog occurred in the sentence {sentence} times')

# try other features upper and lower do tuple.
fruits = '12 kg apples, 10 kg plums, 20 kg pears'
total = 0
for word in fruits.split(' '):
    if word.isnumeric():
        total = total + int(word)

print(f'Total of fruits is {total} kg.')
