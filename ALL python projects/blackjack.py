print("""     
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|""")

print("welcome to my blackjack game!")

import random 
def deal_card():
    """it returns a random card"""
    card_list = [11 ,2 ,3 ,4 ,5 ,6 ,7 ,8, 9, 10 ,10 ,10 ,10]
    card = random.choice(card_list)
    return card 



def calculate_score(list_of_cards):
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0

    if 11 in list_of_cards and sum(list_of_cards) > 21 :
        list_of_cards.remove(11) 
        list_of_cards.append(1)


    return sum(list_of_cards) 




def compare(user_score ,computer_score):
    if user_score == computer_score:
        return "this is a draw!"
    elif computer_score == 0:
        return "computer wins"
    elif user_score == 0:
        return "you won!"
    elif user_score >21:
        return "you're over 21 computer wins"
    elif computer_score >21:
        return "computer is over 21 you win"
    elif user_score > computer_score:
        return "you win!"
    elif computer_score > user_score:
        return "you lose"

def play_game():
    user_cards = []
    computer_cards = []
    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False
    while not game_over:




        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards} and your current score: {user_score}")
        print(f"computer's first card is: {computer_cards[0]}")



        if user_score == 0 or computer_score == 0 or user_score > 21 :
            game_over = True
        else:
            want_more =input("type 'y' to get another card type 'n' to pass ").lower()
            if want_more == "y":
                user_cards.append(deal_card())
            elif want_more == "n":
                game_over = True
            else:
                print("please choose y or n ") 

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)



    print(f"your final hand: {user_cards}, and your final score: {user_score}")
    print(f"computers final hand: {computer_cards}, and computers final score: {computer_score}")
    print(compare(user_score ,computer_score))

play_game()
while input("Would you like to play another hand? Type 'y' or 'n' ").lower() == "y":
    play_game()


