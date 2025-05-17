import art
import random
import game_data

def select_option(data_list):
    out = random.choice(data_list)
    data_list.remove(out)
    return out

def choosing(compare,option_a,option_b):
    return option_a if compare == 'a' else option_b

def play_game():
    print("\n" * 10)
    print(art.logo)
    data_copy = game_data.data
    option_a = select_option(data_copy)
    option_b = select_option(data_copy)
    current_score = 0
    game_over = False

    while not game_over:
        print(f"Compare A: {option_a['name']} a {option_a['description']} from {option_a['country']}")
        print(art.vs)
        print(f"Compare B: {option_b['name']} a {option_b['description']} from {option_b['country']}")

        choice = input("who has more followers 'A' or 'B' ?").lower()
        user_choice = choosing(choice,option_a, option_b)

        if option_a['follower_count'] > option_b['follower_count']:
            correct_choice = option_a
        else:
            correct_choice = option_b

        if user_choice == correct_choice:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
            option_a = correct_choice
            if len(data_copy) == 0:
                print("You've gone through all the data! Great job!")
                break
            option_b = select_option(data_copy)
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            print(f"{option_a['name']}: {option_a['follower_count']} million followers")
            print(f"{option_b['name']}: {option_b['follower_count']} million followers")
            game_over = True

while input("Do you wanna play 'Higher or Lower' Game? Enter 'y' or 'n'").lower() == 'y':
    play_game()
