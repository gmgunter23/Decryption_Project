username = input("What is your name? > ")

answer = input(f"{username}, would you like to decrypt or encrypt?")

message = input(f"{username}, what message would you like to {answer}")

def Convert(string):
    li = list(string.split("-"))
    return li

list_message = Convert(message)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in list_message:
    num = list_message[i]
    if answer == 'encrypt':
        for i in alphabet:
            num2 = alphabet[i]
            if num == num2:
                
        