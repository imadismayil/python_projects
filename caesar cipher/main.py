from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text,shift_amount,method):
    output_text = ""
    if method == "decode":
        shift_amount *= -1
    for ch in original_text:
        if ch in alphabet:
            pos = alphabet.index(ch)
            output_text += alphabet[(pos + shift_amount)%len(alphabet)]
        else:
            output_text += ch
    print(f"the {method}d message is {output_text}.")

control = True
while control:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, method=direction)
    choice =  input("Type 'yes' if you want to continue,Otherwise type 'no'.\n").lower()
    if choice == "no":
        control = False



