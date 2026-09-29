

while True:
    word = input("Enter a word: ")
    letter = input("Enter a character to search for: ")

    found = False

    for character in word:
            if character.lower() == letter.lower():
                found = True
                break

    if found:
        print("Character Found: ")
    else:
        print("Character Not Found! ")

    again = input("Try again? (Y/N): ")
    if again.upper() != "Y":
        break


#niggga