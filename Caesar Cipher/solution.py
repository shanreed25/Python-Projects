# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    # if encode_or_decode == "decode":
    #     user_shift_amount *= -1
    for letter in original_text:
        #because when decoding we change the number from positive to negative
        #we need to save the original shift amount to a variable so it resets to that value on every loop
        # or we could move the if statement out the for loop
        user_shift_amount = shift_amount
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                user_shift_amount  *= -1
            shifted_position = alphabet.index(letter) + user_shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
            # shift_amount = 0
    print(f"Here is the {encode_or_decode}d result: {output_text.capitalize()}")


# TODO-3: Can you figure out a way to restart the cipher program?
continue_cipher = True
while continue_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # when the function is finish running
    go_again =input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

    if go_again == "no":
        continue_cipher = False
        print("Exiting cipher..... Goodbye!")
        # if go_again is any other value it will skip this and continue to the next iteration of the while loop








caesar("khoor%", 3, "decode")  # Call the function