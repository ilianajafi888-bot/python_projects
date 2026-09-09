import random 
def deal_card():
    """it returns a random card"""
    card_list = [11 ,2 ,3 ,4 ,5 ,6 ,7 ,8, 9, 10 ,10 ,10 ,10]
    card = random.choice(card_list)
    return card 

user_cards = []
computer_cards = []
for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(list_of_cards):
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0

    if 11 in list_of_cards and sum(list_of_cards) > 21 :
        list_of_cards.remove(11) 
        list_of_cards.append(1)


    return sum(list_of_cards) 

game_over = False

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"your cards: {user_cards} and your current score: {user_score}")
print(f"computer's first card is: {computer_cards[0]}")


if user_score == 0 or computer_score == 0 or user_score > 21 :
    game_over = True
else:
    want_more =input("type 'y' to get another card type 'n' to pass")
    if want_more == 




