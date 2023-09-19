# receive the task from the user, and then enter it in such a way that individual words are
# written once in Lowercase and once in Uppercase letters.
# 1st way

sentence = input('Write a sentence with four words: ')

sentence_1 = sentence.split()
print(sentence_1[0].lower(), sentence_1[1].upper(), sentence_1[2].lower(), sentence_1[3].upper())

print('---' * 50)

# 2nd way

user = input('Write a sentence: ')
user_1 = ''
for counter, word in enumerate(user.split(' ')):
    if counter % 2 == 0:
        user_1 = f'{user_1} {word.upper()}'
    else:
        user_1 = f'{user_1} {word.lower()}'

print(user_1)

print('---' * 50)

# 3rd way

sent = input('Write a sentence: ')
sent_1 = ''

for counter, word in enumerate(sent.split(' ')):
    new_word = word.upper()
    if counter % 2 == 0:
        new_word = word.lower()

    sent_1 = f'{sent_1} {new_word}'

print(sent_1)
