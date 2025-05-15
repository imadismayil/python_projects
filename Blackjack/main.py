from art import logo
import random

def deal_cards():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    """calculate the total score in the hand of player/computer and also switch value of ace b/w 1 and 11"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0 #blackjack
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1
    return sum(hand)
def compare(user_score,comp_score):
    if user_score > 21 and comp_score > 21:
        return "Both went over! It's a draw 🙃"
    elif user_score > 21:
        return "You went over! You lose 😭"
    elif comp_score > 21:
        return "computer went over. You win 😁"
    elif user_score == comp_score:
        return "It's a draw 🙃"
    elif user_score == 0:
        return "Blackjack! You win 🥳"
    elif comp_score == 0:
        return "Dealer has Blackjack! You lose 😱"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def start_game():
    """starts the game and initializes all values to zero"""
    print("\n" * 5)
    print(logo)
    user_dec = []
    comp_dec =[]

    for i in range(2):
        user_dec.append(deal_cards())
        comp_dec.append(deal_cards())
    game_over = False
    while not game_over:
        user_score = calculate_score(user_dec)
        comp_score = calculate_score(comp_dec)
        if user_score == 0:
            print(f"Your cards {user_dec} is a Blackjack! 🂡🎉")
        else:
            print(f"Your cards {user_dec}, current score : {user_score}")
        print(f"Computers first card is {comp_dec[0]}")
        if user_score == 0 or comp_score == 0 or  user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card or type 'n' to pass").lower()
            if choice == 'y':
                user_dec.append(deal_cards())
            else:
                game_over = True
#     computer's turn
    while calculate_score(comp_dec) < 17:
        comp_dec.append(deal_cards())
    comp_score = calculate_score(comp_dec)
    user_score = calculate_score(user_dec)
    print("\n Final Hands:\n")
    if user_score == 0:
        print(f"Your final hand {user_dec}  is a Blackjack! 🂡🎉")
    else:
        print(f"Your final hand {user_dec}, final score {user_score}")

    if comp_score == 0:
        print(f"Computer's final hand {comp_dec}  is a Blackjack! 🂡🎉")
    else:
        print(f"Computer's final hand {comp_dec}, final score {comp_score}")

    print("\n RESULT \n")
    print(compare(user_score,comp_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    start_game()
