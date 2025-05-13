# ☕ Coffee Machine – Python Project

This is a simple **console-based coffee machine simulator** written in Python. It allows users to choose a drink, pay using coins, and receive their beverage if enough resources and money are available.

## 💡 Features

- Choose from 3 drinks: `espresso`, `latte`, or `cappuccino`
- Insert coins: quarters, dimes, nickels, and pennies
- Automatically checks if enough resources are available
- Handles payments and returns change
- Shows current resource levels with the `report` command
- Type `off` to shut down the machine

## 🛠 How It Works

- Each drink has a required amount of water, milk (if needed), and coffee.
- The machine checks if enough resources are available before proceeding.
- If the user inserts enough money, the drink is made and resources are deducted.
- If not enough money is inserted, the transaction is canceled.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Copy the code into a file named `coffee_machine.py`.
3. Run the script:
   ```bash
   python coffee_machine.py
