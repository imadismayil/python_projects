# Coffee Machine Simulator ☕️

This is a simple Python-based coffee machine simulation that allows a user to choose from espresso, latte, or cappuccino. The program checks for sufficient resources, accepts coin input, dispenses drinks, and tracks earnings.

---

## 📁 Project Structure

```
coffee_machine/
├── data.py       # Contains MENU and resources dictionary
├── main.py       # Main logic to run the coffee machine
└── README.md     # Project documentation
```

---

## 📦 Files Description

### `data.py`

Contains two dictionaries:

```python
MENU = {
    "espresso": { ... },
    "latte": { ... },
    "cappuccino": { ... }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
```

- `MENU` defines each drink’s required ingredients and cost.
- `resources` defines the available raw materials.

### `main.py`

Implements the coffee machine simulation. Key features include:
- Checking resource availability before making a drink.
- Accepting ₹1, ₹2, ₹5, and ₹10 coins from the user.
- Calculating and returning change if overpaid.
- Generating a report showing remaining resources and total money earned.
- Handling shutdown via `"off"` and reporting via `"report"` commands.

---

## 🛠️ How to Run

1. Make sure you have Python 3 installed.
2. Clone or download the project.
3. Run the simulator:

```bash
python main.py
```

---

## ✅ Features

- Choose from `espresso`, `latte`, or `cappuccino`.
- Automatically checks for sufficient ingredients.
- Accepts simulated currency inputs and calculates change.
- Prints machine resource status with `"report"` command.
- Can be turned off with `"off"` command.

---

## 🧪 Sample Usage

```plaintext
What would you like? (espresso/latte/cappuccino): latte
Number of ₹1 coin you are inserting: 2
Number of ₹2 coin you are inserting: 1
Number of ₹5 coin you are inserting: 0
Number of ₹10 coin you are inserting: 0
Making latte... Change = ₹1

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: ₹2.5
```

---

## 📌 Notes

- The machine does not automatically refill resources.
- Error handling is minimal—ensure valid inputs.
- You can modify `data.py` to add new drinks or adjust resources.

---

## 🧰 Future Improvements

- Add refill option for resources.
- Handle invalid coin input with proper error messages.
- Save order history or earnings to a file.

---

## 👨‍💻 Author

Developed by [Your Name].  
For educational or demo use.
