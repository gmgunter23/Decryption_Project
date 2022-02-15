from numpy import isin

username = input("What is your name? > ")

while True:
    answer = input("Would you like to encrypt or decrypt? > ")
    if answer == 'encrypt' or answer == 'decrypt':
        break
    else:
        print("Please say either encrypt or decrypt.")

message = input(f"What message would you like to {answer} ").lower()

while True:
    key = input(f"{username}, what key would you like to cipher by? > ")
    if key.isnumeric():
        key = int(key)
        break
    else:
        print("You need to have a number value please.")

alphabet = 'abcdefghijklmnopqrstuvwxyz '

new_message = []

if answer == 'encrypt':
    for character in message:
        for letter in alphabet:
                if character == letter:
                    letter_index = alphabet.index(letter) + key
                    if letter_index >= 27:
                        letter_index = letter_index - 27
                        new_message.append(alphabet[letter_index])
                    else:
                        new_message.append(alphabet[letter_index])
    print(''.join(new_message))

if answer == 'decrypt':
    for character in message:
        for letter in alphabet:
                if character == letter:
                    letter_index = alphabet.index(letter) - key
                    if letter_index < 0:
                        letter_index = letter_index + 27
                        new_message.append(alphabet[letter_index])
                    else:
                        new_message.append(alphabet[letter_index])
    print(''.join(new_message))