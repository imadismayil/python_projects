import random
import hangman_words
import hangman_art
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to Guess:"+placeholder)


display = ["_"] * word_length
lives = 6
guessed_letters = []
output = ''
while output != chosen_word and lives !=0:
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("Already guessed this letter!")
        print(''.join(display))
        print(hangman_art.stages[lives])
        continue
    correct_guess = False
    for i in range(word_length):
        if chosen_word[i] == guess:
            display[i] = guess
            guessed_letters.append((guess))
            correct_guess = True
            print(hangman_art.stages[lives])
    if not correct_guess:
        print(f"You guessed {guess}, thhat's not in the word.You lost a life")

        lives -=1
        print(hangman_art.stages[lives])
    output =''.join(display)
    print(output)
if "_" not in output:
    print("You Win")
else:
    print("You lost")
    print(f"The word was {chosen_word}")
