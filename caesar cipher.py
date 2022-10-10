alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_end = False

#encoding cipher text
def encrypt(plain_text,shift_amount):
    encoded_text = ""
    for letter in plain_text:
        if letter in alphabet:
            pos = alphabet.index(letter)
            new_pos = pos + shift_amount
            new_letter = alphabet[new_pos]
            encoded_text += new_letter
        if letter not in alphabet:
            letter == letter
            encoded_text += letter
    print("The cipher text is:",encoded_text)

#decoding cipher text
def decrypt(encoded_text,shift_amount):
    plain_text = " "
    for letter in encoded_text:
        if letter in alphabet:
            pos = alphabet.index(letter)
            new_pos = pos - shift_amount
            plain_text += alphabet[new_pos]
        if letter not in alphabet:
            letter == letter
            plain_text += letter
    print("The plain text is:",plain_text)

#while loop to restart program if req.
while not should_end:
    print("\t" "CAESAR CIPHER")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(plain_text=text,shift_amount=shift)
    elif direction == "decode":
        decrypt(encoded_text=text,shift_amount=shift)
    else:
        print("invalid input")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if restart == "no":
        should_end = True
        print("GOODBYE!")
