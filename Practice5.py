word = input("Enter a word: ")
letter = input("Enter a character to search for: ")

found = False

for character in word:
    if character.lower() == letter.lower():
        found = True
        break