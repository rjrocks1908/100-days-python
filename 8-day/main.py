import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

total_alphabet = len(alphabet)

def caesar(text, shift, direction):
    result_text = ""
    text = text.lower()

    for letter in text:
        if letter in alphabet:
            idx = alphabet.index(letter)
            position = 0
            if direction == "encode":
                position = (idx + shift) % total_alphabet
            else:
                position = (idx - shift) % total_alphabet
                if position < 0:
                    position = total_alphabet + position

            result_text += alphabet[position]
        else:
            result_text += letter

    print(f"The {direction}d text is {result_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text=text, shift=shift, direction=direction)

    restart = input("Type 'yes' to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("GoodBye!")
        break