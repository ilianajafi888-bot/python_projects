print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                     ''')
print("welcome to hangman")

stages = ['''

 +---+
 |   |
     |
     |
     |
     | 
======= '''

, 

'''
 +---+
 |   |
 O   |
     |
     |
     |
=======
'''

,  

'''     
 +---+
 |   |
 O   |
 |   |
     |
     |
=======
'''
,

'''       
 +---+
 |   |
 O   |
/|   |
     |
     |
=======
'''
,

'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=======
'''         

,

'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=======

'''
,

'''
 +---+ 
 |   |
 O   |
/|\  |
/ \  |
     |
=======          


    ''']


import random
#import hangman_word_list why it doesnt work 
word_list =["sheep", "queen", "dog", "dimond", "blue", "face", "shark", "bag", "lock", "luck", "easy", "pizza"] 

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(stages[lives])
print(f"pssst, the solution is {chosen_word}.")
display =[]
for x in chosen_word:
    display += "_"
print(display)

the_end  = False 
# while the_end  == False:
#     guess = input("guess a letter: ").lower()
#     if guess not in chosen_word:
#         lives -= 1
#         print(stages[lives])
        

#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     print(display)
#     if "_" not in display:
#         print("you win!")
#         break


    #for painting in stages:
    #    painting += stages
    #print(stages[painting])


stage = 0
print(stages[stage])

while the_end == False:
    guess = input("guess a letter: ").lower()

    if guess not in chosen_word:
        stage += 1

        if stage > 6:
            print("Game over!")
            break

        print(stages[stage])

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        print("you win!")
        break


































#import random
#import hangman_word_list why it doesnt work 
#word_list =["sheep", "queen", "dog", "dimond", "blue", "face", "shark", "bag", "lock", "luck", "easy", "pizza"] 

#chosen_word = random.choice(word_list)
#word_length = len(chosen_word)
#end_of_game = False
#lives = 6
#print(f"pssst, the solution is {chosen_word}.")
#display =[]
#for _ in range(word_length):
#    display += "_"
#while not end_of_game:
#    guess = input("guess a letter: ").lower()
#if guess in display:
#    print(f"you've already guessed {guess}")



#for position in range(word_length):
#    letter = chosen_word[position]
#    #print(f"current position: {position}\n current letter: {letter}\n guess letter: {guess}")
#    if letter == guess:
#        display[position] = letter

#if guess not in chosen_word:
#
 #   print(f"you,ve guessed {guess}, thats bot in the word you lose a life.")
  #  lives -= 1
   # if lives == 0:
    #    end_of_game == True
     #   print("you win!")
      #  
#print(stages[lives])
