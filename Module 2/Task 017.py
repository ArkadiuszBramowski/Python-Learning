# Write a program that will receive any number of characters from the user
# and enter it on the screen in reverse.

sentence = input('Write a sentence to flip: ')
print('Sentence to flip: ', sentence[::-1])

# write a program that will download a string of characters from the user
# and return the same text without spaces and punctuation.

sentence_1 = '1Be, or, not to be; that, a, question'
new_sentence_1 = ''
for char in sentence_1:
    if char.isnumeric() or char.isalpha():
        new_sentence_1 = new_sentence_1 + char

print(new_sentence_1)
