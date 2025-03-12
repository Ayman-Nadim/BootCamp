word = input("Enter a word: ")
letter_dict = {}

for index, letter in enumerate(word):
    if letter in letter_dict:
        letter_dict[letter].append(index)
    else:
        letter_dict[letter] = [index]

print(letter_dict)
