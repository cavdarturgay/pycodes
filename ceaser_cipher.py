alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

import ceaser_art
print(ceaser_art.logo)

user_want = True
while user_want:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    run_again = input("Do you want to restart the cipher program? Type: yes/no\n").lower()
    if run_again == "no":
        print("Bye bye !!!")
        user_want = False

