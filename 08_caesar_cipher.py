alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def xcrypt(message: list, shift: int) -> list:

    xcrypted = []
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            xcrypted.append(alphabet[new_position % len(alphabet)])
        else:
            xcrypted.append(letter)
    return xcrypted


def execute():
    print("WELCOME TO CAESAR CIPHER")

    while True:

        mode = input("Type 'encode' to encrypt, 'decode' to decrypt: ")
        message = input("Type your message:\n").lower()
        shift = input("Type the shift number: ")

        if mode == 'encode':
            print("Encoded string:")
            encoded = xcrypt(list(message), int(shift))
            print(''.join(encoded))
        elif mode == 'decode':
            print("Decoded string:")
            decoded = xcrypt(list(message), -int(shift))
            print(''.join(decoded))

        again = input("Type 'yes' to go again, otherwise type 'no': ")
        if again == 'no':
            break


if __name__ == '__main__':
    execute()
