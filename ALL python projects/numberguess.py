print(""""
                                        __  .__                                 ___.                 
   ____  __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
  / ___\|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
 / /_/  >  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \___  /|____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
/_____/             \/     \/     \/             \/     \/       \/            \/    \/     \/      """)


import random

the_number = random.randint(1, 100)

print("welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    choice = input("choose a difficulty. 'easy' or 'hard': ").lower()
    if choice == "easy":
        attempts = 8
        break
    elif choice == "hard":
        attempts = 5
        break
    else:
        print("invalid choice! please choose between easy or hard")

print(f"you have {attempts} attempts to guess the number.")


def arrived(choosen):
    if choosen == the_number:
        return f"you win! the answer was {the_number}"
    elif choosen < the_number:
        return "higher"
    else:
        return "lower"


while attempts > 0:
    choosen = int(input("guess a number: "))
    attempts -= 1
    result = arrived(choosen)
    print(result)

    if choosen == the_number:
        break

    if attempts > 0:
        print(f"{attempts} attempts left.")
    else:
        print(f"you used all your guesses, you lose. the number was {the_number}")
