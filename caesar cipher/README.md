# 🔐 Caesar Cipher Project

A beginner-friendly Python program that implements the **Caesar Cipher**, a classic encryption technique where each letter in a message is shifted by a certain number of places in the alphabet.

---

## 🧠 How It Works

- **Encoding** shifts each letter forward by a user-defined number (wraps from 'z' to 'a').
- **Decoding** shifts each letter backward by the same amount.
- Spaces, numbers, and symbols are preserved and not encrypted.
- Users can repeatedly encrypt/decrypt until they choose to exit.

---

## 🚀 Features

- Handles large shift numbers using modulo to stay within alphabet limits.
- Ignores non-alphabet characters (e.g., punctuation, spaces).
- Allows multiple encrypt/decrypt operations without restarting the program.
- Includes an ASCII art logo (from `art.py`).

---

## 📁 Project Structure

caesar_cipher/
│
├── main.py # Main Caesar Cipher logic
├── art.py # Contains the ASCII logo
├── README.md # This file


---

