import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers =['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols =['!', '#', '$', '&', '(', ')', '+', '*', '%']
print("welcome to the pypassword generator!")
letters_times = int(input("how many letters would you like in your password?\n"))
numbers_times = int(input("how many numbers would you like in your password?\n"))
symbols_times = int(input("how many symbols would you like in your password?\n"))
password_list = []
for charachter in range(1, letters_times + 1):
    password_list += random.choice(letters)

for charachter in range(1, numbers_times + 1):
    password_list += random.choice(numbers)

for charachter in range(1, symbols_times + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for charachter in password_list:
    password += charachter
print(f"your password is: {password}")
