print('''
  ___ __ _  ___  ___  __ _ _ __  
 / __/ _` |/ _ \/ __|/ _` | '__| 
| (_| (_| |  __/\__ \ (_| | |    
 \___\__,_|\___||___/\__,_|_|    
  ___(_)_ __ | |__   ___ _ __    
 / __| | '_ \| '_ \ / _ \ '__|   
| (__| | |_) | | | |  __/ |      
 \___|_| .__/|_| |_|\___|_|      
       |_|                       ''')


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"here's the {direction}d result: {end_text}")


should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("type 'encode' to encrypte, type 'decode' to decrypt:\n")
    text = input("type your message:\n").lower()
    shift = int(input("type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input(
        "type 'yes' if you want to go again. otherwise type 'no'.\n ")
    if result == "no":
        should_continue = False
        print("Goodbye")


# def encrypte(real_text , shift_amount):
#     ceasar_text = ""
#     for letter in real_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         ceasar_text += alphabet[new_position]
#     print(f"your encoded text is {ceasar_text}")

# def decrypt(reverse_text , reverse_shift):
#     cipher_text = ""
#     for letter in reverse_text:
#         position = alphabet.index(letter)
#         new_position = position - reverse_shift
#         cipher_text += alphabet[new_position]
#     print(f"your decoded text is {cipher_text}")

# if direction == "encode":
#     encrypte(real_text=text , shift_amount=shift)
# elif direction == "decode":
#     decrypt(reverse_text=text , reverse_shift=shift)
