username = input("What is your name? > ")

answer = input(f"{username}, would you like to decrypt or encrypt?")

message = input(f"{username}, what message would you like to {answer}")

key = input(f"{username}, what key would you like to cipher by?")


alphabet = 'abcdefghijklmnopqrstuvwxyz'

new_message = []


for character in message:
    for letter in alphabet:
        if character == letter:
            letter_index = alphabet.index(letter) + key
            new_message.append(alphabet[letter_index])