import random
player_choice =int(input("what do you choose type 0, for rock 1, for paper or 2, for scissors.\n "))
rock ="🤜"
scissor = "✌️"
paper = "🤚"
hand_sighn= [rock , paper , scissor]
print(hand_sighn[player_choice])
computer_choice=random.randint(0, 2)
print(f"computer chose:")
print(hand_sighn[computer_choice])
if player_choice>2:
    print("you typed an invalid number, you lose")
elif player_choice==0 and computer_choice==2:
    print("you win!")
elif player_choice==computer_choice:
    print("it's a draw.")
elif computer_choice==0 and player_choice==2:
    print("you lose")
elif computer_choice>player_choice:
    print("you lose.")
elif player_choice>computer_choice:
    print("you win")
