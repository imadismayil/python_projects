# 🃏 Blackjack Game (Python Terminal Project)

A simple terminal-based Blackjack game built using Python. This project simulates the classic card game where the user plays against a computer dealer following standard Blackjack rules.

## 🎮 Game Features

- Unlimited deck size with cards drawn randomly (cards are not removed after drawing).
- Supports:
  - Aces counting as **1 or 11**.
  - Dealer behavior: draws cards until reaching a score of 17 or more.
  - Detection of **Blackjack**, **Bust**, and **Draw** scenarios.
- Fun emoji feedback based on game results.
- ASCII art logo displayed at game start.

## 🧠 Game Rules

- **Deck**: `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`  
  (Jack, Queen, King = 10; Ace = 11 or 1 depending on hand)
- The deck is **unlimited in size** (cards are drawn with replacement).
- The player can choose to `"Hit"` (draw a card) or `"Stand"` (pass).
- The dealer draws until the total score is **at least 17**.
- A **Blackjack** is a 2-card hand summing to exactly 21.
- If both player and dealer exceed 21, it's a **draw**.

## 🛠️ Setup & Run

### Requirements

- Python 3.x

### Run the Game

Clone this repository and run:

```bash
python blackjack.py
Make sure art.py is in the same directory or adjust the import accordingly.

📁 Project Structure
python_projects/
└── blackjack/
    ├── blackjack.py
    ├── art.py
    └── README.md
📸 Sample Output

Do you want to play a game of Blackjack? Type 'y' or 'n': y



Your cards [10, 11] is a Blackjack! 🂡🎉
Computer's first card is 7

Final Hands:
Your final hand [10, 11] is a Blackjack! 🂡🎉
Computer's final hand [7, 8], final score 15

RESULT
Blackjack! You win 🥳

📄 License
This project is free to use and modify for educational or personal use.

