# Below enter lowercase letters only those words from the given sentence
# that start and end with the same letter.

sentence = input('Give a sentence: ')

for word in sentence.split(' '):
    # if word[0].lower() == word[-1].lower():
    if word.lower().startswith(word[-1].lower()):
        print(word)

# Below display all sentences with vowels removed.

new_sentence = ''
vowels = 'aeiouy'

for char in sentence:
    if char.lower() not in vowels:
        new_sentence += char

print(new_sentence)
